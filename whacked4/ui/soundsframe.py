#!/usr/bin/env python
#coding=utf8

from app import config
from ui import editormixin, windows, utils
import copy
import wx


class SoundsFrame(editormixin.EditorMixin, windows.SoundsFrameBase):
    """
    Sounds editor window.
    """
    
    # The colour used for color-coding priorities.
    PRIORITY_COLOUR = wx.Colour(red=255, green=48, blue=0)
    
    
    def __init__(self, params):
        windows.SoundsFrameBase.__init__(self, params)
        editormixin.EditorMixin.__init__(self)
        
        self.SetIcon(wx.Icon('res/icon-weapons-small.png'))
        
        self.priority_colours = []
        self.build_colours()
        
        
    def activate(self, event):
        """
        Called when this editor window is activated by the user.
        """
        
        # Call the editor mixin function that we are overriding.
        editormixin.EditorMixin.activate(self, event)
        
        if self.IsBeingDeleted():
            return
        
        # Update sound names only.
        for index, name in enumerate(self.patch.sound_names):
            self.SoundList.SetStringItem(index, 1, name.upper())
        
        
    def build_colours(self):
        """
        Builds priority colour coding colours and blends them with the system's window background color.
        """
        
        sys_col = self.SoundList.GetBackgroundColour()
        factor = 0
        sys_factor = 0
        
        for index in range(128 / 32):
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
        self.pwads = self.GetParent().pwads
        
        self.selected_index = -1
        
        self.soundlist_build()
        
        
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
        
        for sound_index in range(len(self.patch.sounds)):
            self.SoundList.InsertStringItem(sound_index, str(sound_index))            
            self.SoundList.SetItemFont(sound_index, config.FONT_MONOSPACED)
            
            self.soundlist_update_row(sound_index)
            
        self.SoundList.Select(0, True)
            
            
    def soundlist_update_row(self, row_index):
        """
        Updates a sound list row with the data for that sound.
        """
        
        sound = self.patch.sounds[row_index]
        sound_name = self.patch.sound_names[row_index]
            
        if sound['isSingular'] == 1:
            singular = 'X'
        else:
            singular = ''
        
        self.SoundList.SetStringItem(row_index, 1, sound_name.upper())
        self.SoundList.SetStringItem(row_index, 2, str(sound['priority']))
        self.SoundList.SetStringItem(row_index, 3, singular)
        
        # Colour-code rows by priority.
        self.SoundList.SetItemBackgroundColour(row_index, self.priority_colours[sound['priority'] / 32])
        
        
    def sound_select_index(self, sound_index):
        """
        Selects a sound by sound index.
        """
        
        sound = self.patch.sounds[sound_index]
        self.selected_index = sound_index
        
        self.Priority.ChangeValue(str(sound['priority']))
        self.Singular.SetValue(sound['isSingular'] == True)
        
        
    def sound_restore(self, event):
        """
        Restores the currently selected sound to it's engine state.
        """

        self.undo_add()
        
        self.patch.sounds[self.selected_index] = copy.deepcopy(self.patch.engine.sounds[self.selected_index])
        self.soundlist_update_row(self.selected_index)
        self.is_modified(True)
        
        
    def sound_play(self, event):
        """
        Plays the currently selected sound.
        """
        
        sound_name = 'DS' + self.patch.sound_names[self.selected_index].upper()
        sound_data = self.pwads.get_sound(sound_name)
        if sound_data != None:
            sound_data.play()


    def set_singular(self, event):
        """
        Sets the singularity flag for the currently selected sound.
        """
        
        self.undo_add()
        
        value = self.Singular.GetValue()
        sound = self.patch.sounds[self.selected_index]
        
        if value == True:
            sound['isSingular'] = 1
        else:
            sound['isSingular'] = 0
            
        self.soundlist_update_row(self.selected_index)
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
        
        self.soundlist_update_row(self.selected_index)
        self.is_modified(True)
        
                
    def undo_restore_item(self, item):
        """
        @see: EditorMixin.undo_restore_item
        """
        
        self.patch.sounds[item['index']] = item['item']
        self.soundlist_update_row(item['index'])
        
        
    def undo_store_item(self):
        """
        @see: EditorMixin.undo_store_item
        """
        
        return {
            'item': copy.deepcopy(self.patch.sounds[self.selected_index]),
            'index': self.selected_index
        }
    
    
    def sound_select(self, event):
        """
        Called when a sound row is selected from the list.
        """
        
        self.sound_select_index(event.GetIndex())