"""
Sound editor UI.
"""

from math import floor
from typing import List, Optional

import wx
from wx import Colour, Window, Control, ActivateEvent, CommandEvent, ListEvent, SpinEvent

from whacked4 import config, utils
from whacked4.dehacked.patch import Patch
from whacked4.doom.wadlist import WADList
from whacked4.ui import editormixin, windows
from whacked4.ui.editormixin import UndoItem


class SoundsFrame(editormixin.EditorMixin, windows.SoundsFrameBase):
    """
    Sounds editor window.
    """

    # The colour used for color-coding priorities.
    PRIORITY_COLOUR: Colour = Colour(red=255, green=48, blue=0)

    UNUSED_TEXT_COLOUR: Colour = Colour(red=127, green=127, blue=127)
    UNUSED_BACKGROUND_COLOUR: Colour = Colour(red=243, green=243, blue=243)

    def __init__(self, parent: Window):
        windows.SoundsFrameBase.__init__(self, parent)
        editormixin.EditorMixin.__init__(self)

        # A list of all tool windows for simple mass operations.
        self.windows_tools: List[Control] = [
            self.Priority,
            self.PrioritySpinner,
            self.Singular,
            self.Restore
        ]

        self.SetIcon(wx.Icon('res/editor-sounds.png'))

        self.priority_colours = []
        self.build_colours()

        self.patch: Optional[Patch] = None
        self.pwads: Optional[WADList] = None

        self.selected_index: int = -1
        self.selected_row: int = -1

    def activate(self, event: ActivateEvent):
        """
        Called when this editor window is activated by the user.
        """

        # Call the editor mixin function that we are overriding.
        editormixin.EditorMixin.activate(self, event)

        if not self:
            return

        # Update sound names only.
        self.SoundList.SetItem(0, 1, self.patch.get_sound_name(0))
        for index, _ in enumerate(self.patch.sounds):
            self.SoundList.SetItem(index + 1, 1, self.patch.get_sound_name(index + 1))

    def build_colours(self):
        """
        Builds priority colour coding colours and blends them with the system's window
        background color.
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

    def build(self, patch: Patch):
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
            self.SoundList.InsertColumn(0, 'Index', width=floor(41 * self.GetDPIScaleFactor()))
            self.SoundList.InsertColumn(1, 'Name', width=floor(54 * self.GetDPIScaleFactor()))
            self.SoundList.InsertColumn(2, 'Priority', width=floor(50 * self.GetDPIScaleFactor()))
            self.SoundList.InsertColumn(3, 'Singular', width=floor(58 * self.GetDPIScaleFactor()))

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

    def soundlist_update_row(self, row_index: int, sound_index: int):
        """
        Updates a sound list row with the data for that sound.
        """

        sound = self.patch.sounds[sound_index]

        if row_index == 0 or sound.unused:
            self.SoundList.SetItem(row_index, 1, self.patch.get_sound_name(0))
            self.SoundList.SetItem(row_index, 2, '')
            self.SoundList.SetItem(row_index, 3, '')

            self.SoundList.SetItemTextColour(row_index, self.UNUSED_TEXT_COLOUR)
            self.SoundList.SetItemBackgroundColour(row_index, self.UNUSED_BACKGROUND_COLOUR)

        else:
            if sound['isSingular'] == 1:
                singular = '◾'
            else:
                singular = ''

            self.SoundList.SetItem(row_index, 1, self.patch.get_sound_name(row_index))
            self.SoundList.SetItem(row_index, 2, str(sound['priority']))
            self.SoundList.SetItem(row_index, 3, singular)

            # Colour-code rows by priority.
            color_index = int(sound['priority'] / 32)
            if color_index >= len(self.priority_colours):
                color_index = len(self.priority_colours) - 1
            self.SoundList.SetItemBackgroundColour(row_index, self.priority_colours[color_index])

    def sound_select_index(self, row_index: int, sound_index: int):
        """
        Selects a sound by sound index.
        """

        self.selected_index = sound_index
        self.selected_row = row_index
        self.update_properties()

    def sound_restore(self, event: CommandEvent):
        """
        Restores the currently selected sound to its engine state.
        """

        self.undo_add()

        sound_clone = self.patch.engine.sounds[self.selected_index].clone()
        self.patch.sounds[self.selected_index] = sound_clone
        self.soundlist_update_row(self.selected_row, self.selected_index)
        self.update_properties()
        self.is_modified(True)

    def sound_play(self, event: CommandEvent):
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

        if not self.patch:
            return

        sound = self.patch.sounds[self.selected_index]

        if self.selected_row == 0 or sound.unused:
            self.Priority.ChangeValue('')
            self.PrioritySpinner.SetValue(0)
            self.Singular.SetValue(False)

            self.tools_set_state(False)

        else:
            singular = sound['isSingular'] == 1

            self.Priority.ChangeValue(str(sound['priority']))
            self.PrioritySpinner.SetValue(sound['priority'])
            self.Singular.SetValue(singular)

            self.tools_set_state(True)

    def tools_set_state(self, enabled: bool):
        """
        Sets the state of all tool controls.
        """

        # Override editing controls if sound support is disabled.
        if 'nosupport.sounds' in self.patch.engine.features:
            enabled = False

        for window in self.windows_tools:
            window.Enable(enabled)

    def set_singular(self, event: CommandEvent):
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

    def set_priority(self, event: CommandEvent):
        """
        Validates and sets a property of the current sound.
        """

        self.undo_add()

        window = self.FindWindowById(windows.SOUNDS_PRIORITY)
        value = utils.validate_numeric(window)

        # Clamp priority to valid range.
        if value < 0:
            value = 0
            wx.Bell()
        elif value >= 0x7FFFFFFF:
            value = 0x7FFFFFFF
            wx.Bell()
        if window.GetValue() != value:
            window.ChangeValue(str(value))

        sound = self.patch.sounds[self.selected_index]
        sound['priority'] = value

        self.soundlist_update_row(self.selected_row, self.selected_index)
        self.is_modified(True)

    def goto_sound_index(self, sound_index: int):
        """
        Selects a sound from the list.
        """

        self.SoundList.Select(sound_index, True)
        self.SoundList.EnsureVisible(sound_index)
        self.SoundList.SetFocus()

    def undo_restore_item(self, item: UndoItem):
        """
        @see: EditorMixin.undo_restore_item
        """

        self.patch.sounds[item['index']] = item['item']
        self.soundlist_update_row(item['index'] + 1, item['index'])
        self.update_properties()

        self.is_modified(True)

    def undo_store_item(self) -> UndoItem:
        """
        @see: EditorMixin.undo_store_item
        """

        return {
            'item': self.patch.sounds[self.selected_index].clone(),
            'index': self.selected_index
        }

    def sound_select(self, event: ListEvent):
        """
        Called when a sound row is selected from the list.
        """

        self.sound_select_index(event.GetIndex(), event.GetIndex() - 1)

    def priority_spin_up(self, event: SpinEvent):
        priority = int(self.Priority.GetValue())
        self.Priority.SetValue(str(priority + 1))

    def priority_spin_down(self, event: SpinEvent):
        priority = int(self.Priority.GetValue())
        self.Priority.SetValue(str(priority - 1))
