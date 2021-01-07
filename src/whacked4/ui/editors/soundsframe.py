#!/usr/bin/env python
#coding=utf8

from whacked4 import config, utils
from whacked4.ui import editormixin, windows
import copy
import wx


class SoundsFrame(editormixin.EditorMixin, windows.SoundsFrameBase):
    """
    Sounds editor window.
    """

    # The colour used for color-coding priorities.
    PRIORITY_COLOUR = wx.Colour(red=255, green=48, blue=0)

    def __init__(self, parent):
        windows.SoundsFrameBase.__init__(self, parent)
        editormixin.EditorMixin.__init__(self)

        # A list of all tool windows for simple mass operations.
        self.WINDOWS_TOOLS = [
            self.Priority,
            self.PrioritySpinner,
            self.Singular,
            self.Restore
        ]

        self.SetIcon(wx.Icon('res/editor-sounds.ico'))

        self.priority_colours = []
        self.build_colours()

        self.patch = None
        self.pwads = None

        self.selected_index = -1
        self.selected_row = -1

    def activate(self, event):
        """
        Called when this editor window is activated by the user.
        """

        # Call the editor mixin function that we are overriding.
        editormixin.EditorMixin.activate(self, event)

        if not self:
            return

        # Update sound names only.
        self.SoundList.SetItem(0, 1, '-')
        for index, sound in enumerate(self.patch.sounds):
            self.SoundList.SetItem(index + 1, 1, sound.name.upper())

    def build_colours(self):
        """
        Builds priority colour coding colours and blends them with the system's window background color.
        """

        sys_col = self.SoundList.GetBackgroundColour()

        for index in range(4):
            factor = 0.06 * index
            sys_factor = 1 - factor

            colour = wx.Colour(
                int(self.PRIORITY_COLOUR.Red() * factor + sys_col.Red() * sys_factor),
                int(self.PRIORITY_COLOUR.Green() * factor + sys_col.Green() * sys_factor),
                int(self.PRIORITY_COLOUR.Blue() * factor + sys_col.Blue() * sys_factor)
            )
            self.priority_colours.append(colour)

    def build(self, patch):
        """
        @see: EditorMixin.build
        """

        self.patch = patch
        self.pwads = self.GetMDIParent().pwads

        self.selected_index = -1
        self.selected_row = -1

        self.soundlist_build()

    def update(self):
        """
        @see: EditorMixin.update
        """

        self.pwads = self.GetMDIParent().pwads

    def soundlist_build(self):
        """
        Builds the contents of the sounds list from scratch.
        """

        self.SoundList.ClearAll()

        # Add column headers if necessary.
        if self.SoundList.GetColumnCount() == 0:
            self.SoundList.InsertColumn(0, 'Index', width=41)
            self.SoundList.InsertColumn(1, 'Name', width=54)
            self.SoundList.InsertColumn(2, 'Priority', width=50)
            self.SoundList.InsertColumn(3, 'Singular', width=58)

        # Add dummy sound.
        self.SoundList.InsertItem(0, '0')
        self.SoundList.SetItemFont(0, config.FONT_MONOSPACED)
        self.soundlist_update_row(0, 0)

        # Add real sounds.
        for sound_index in range(len(self.patch.sounds)):
            self.SoundList.InsertItem(sound_index + 1, str(sound_index + 1))
            self.SoundList.SetItemFont(sound_index + 1, config.FONT_MONOSPACED)

            self.soundlist_update_row(sound_index + 1, sound_index)

        self.list_autosize(self.SoundList)
        self.SoundList.Select(0, True)

    def soundlist_update_row(self, row_index, sound_index):
        """
        Updates a sound list row with the data for that sound.
        """

        if row_index == 0:
            self.SoundList.SetItem(row_index, 1, '-')
            self.SoundList.SetItem(row_index, 2, '')
            self.SoundList.SetItem(row_index, 3, '')

            # Colour-code rows by priority.
            self.SoundList.SetItemBackgroundColour(row_index, self.priority_colours[0])

        else:
            sound = self.patch.sounds[sound_index]

            if sound['isSingular'] == 1:
                singular = '◾'
            else:
                singular = ''

            self.SoundList.SetItem(row_index, 1, sound.name.upper())
            self.SoundList.SetItem(row_index, 2, str(sound['priority']))
            self.SoundList.SetItem(row_index, 3, singular)

            # Colour-code rows by priority.
            color_index = int(sound['priority'] / 32)
            self.SoundList.SetItemBackgroundColour(row_index, self.priority_colours[color_index])

    def sound_select_index(self, row_index, sound_index):
        """
        Selects a sound by sound index.
        """

        self.selected_index = sound_index
        self.selected_row = row_index
        self.update_properties()

    def sound_restore(self, event):
        """
        Restores the currently selected sound to it's engine state.
        """

        self.undo_add()

        self.patch.sounds[self.selected_index] = self.patch.engine.sounds[self.selected_index].clone()
        self.soundlist_update_row(self.selected_row, self.selected_index)
        self.update_properties()
        self.is_modified(True)

    def sound_play(self, event):
        """
        Plays the currently selected sound.
        """

        if self.selected_row == 0:
            return

        utils.sound_play(self.patch.sounds[self.selected_index].name, self.pwads)

    def update_properties(self):
        """
        Update the displayed property controls.
        """

        if self.selected_row == 0:
            self.Priority.ChangeValue('')
            self.Singular.SetValue(False)

            self.tools_set_state(False)

        else:
            sound = self.patch.sounds[self.selected_index]
            singular = (sound['isSingular'] == 1)

            self.Priority.ChangeValue(str(sound['priority']))
            self.Singular.SetValue(singular)

            self.tools_set_state(True)

    def tools_set_state(self, enabled):
        """
        Sets the state of all tool controls.
        """

        # Override editing controls if sound support is disabled.
        if 'nosupport.sounds' in self.patch.engine.features:
            enabled = False

        for window in self.WINDOWS_TOOLS:
            window.Enable(enabled)

    def set_singular(self, event):
        """
        Sets the singularity flag for the currently selected sound.
        """

        self.undo_add()

        value = self.Singular.GetValue()
        sound = self.patch.sounds[self.selected_index]

        if value:
            sound['isSingular'] = 1
        else:
            sound['isSingular'] = 0

        self.soundlist_update_row(self.selected_row, self.selected_index)
        self.is_modified(True)

    def set_priority(self, event):
        """
        Validates and sets a property of the current sound.
        """

        self.undo_add()

        window = self.FindWindowById(windows.SOUNDS_PRIORITY)
        value = utils.validate_numeric(window)

        # Clamp sprite to valid range.
        if value < 0:
            value = 0
        elif value >= 127:
            value = 127
        if window.GetValue() != value:
            window.ChangeValue(str(value))

        sound = self.patch.sounds[self.selected_index]
        sound['priority'] = value

        self.soundlist_update_row(self.selected_row, self.selected_index)
        self.is_modified(True)

    def goto_sound_index(self, sound_index):
        """
        Selects a sound from the list.
        """

        self.SoundList.Select(sound_index, True)
        self.SoundList.EnsureVisible(sound_index)
        self.SoundList.SetFocus()

    def undo_restore_item(self, item):
        """
        @see: EditorMixin.undo_restore_item
        """

        self.patch.sounds[item['index']] = item['item']
        self.soundlist_update_row(item['index'] + 1, item['index'])
        self.update_properties()

        self.is_modified(True)

    def undo_store_item(self):
        """
        @see: EditorMixin.undo_store_item
        """

        return {
            'item': self.patch.sounds[self.selected_index].clone(),
            'index': self.selected_index
        }

    def sound_select(self, event):
        """
        Called when a sound row is selected from the list.
        """

        self.sound_select_index(event.GetIndex(), event.GetIndex() - 1)

    def priority_spin_up(self, event):
        priority = int(self.Priority.GetValue())
        self.Priority.SetValue(str(priority + 1))

    def priority_spin_down(self, event):
        priority = int(self.Priority.GetValue())
        self.Priority.SetValue(str(priority - 1))
