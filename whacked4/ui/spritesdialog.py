#!/usr/bin/env python
#coding=utf8

from app import config
from ui import windows, utils
import wx


class SpritesDialog(windows.SpritesDialogBase):
    """
    This dialog displays a list of sprites and sprite frames, and lets the user select one of them.
    """

    def __init__(self, parent):
        windows.SpritesDialogBase.__init__(self, parent)
                
        
    def ok(self, event):
        """
        Called when the user clicks the Ok button.
        """
        
        window = self.FindWindowById(windows.SPRITES_NAMES)
        
        # Store selected details.
        selection = window.GetSelection()
        if selection == wx.NOT_FOUND:
            self.selected_sprite = -1
            self.selected_frame = -1
            
        else:
            self.selected_sprite = self.filter_list[selection]
            
            # Store the frame index if one was selected.
            frame_index = self.FrameIndex.GetValue()
            if frame_index == '':
                self.selected_frame = -1
            else:
                self.selected_frame = int(frame_index)
                 
        self.Hide()
        
        
    def sprite_select_list(self, event):
        """
        Called when a sprite name is selected in the list.
        """
        
        self.FrameIndex.SetValue('0')
        self.update_preview()
        
        
    def sprite_select_index(self, list_index):
        """
        Selects a sprite name from the list based on a list index.
        """
        
        if list_index < 0:
            list_index = 0
        elif list_index >= self.SpriteNames.GetCount():
            list_index = self.SpriteNames.GetCount() - 1
                
        self.SpriteNames.Select(list_index)
        self.update_preview()
        
        
    def update_preview(self):
        """
        Updates the displayed sprite.
        """
        
        selected = self.SpriteNames.GetSelection()
        if selected != wx.NOT_FOUND:
            sprite_name = self.SpriteNames.GetString(selected)
            sprite_frame = self.FrameIndex.GetValue()
            if sprite_frame != '':
                sprite_frame = int(sprite_frame)
            else:
                sprite_frame = 0
            
            self.SpritePreview.show_sprite(sprite_name, sprite_frame)
        
        
    def set_state(self, patch, pwads, sprite_index=None, frame_index=None):
        """
        Sets this dialog's user interface state.
        """
        
        self.patch = patch
        self.pwads = pwads

        self.selected_sprite = -1
        self.selected_frame = -1
        
        self.Filter.ChangeValue('')
        self.filter_build('')
        
        if sprite_index is not None:
            self.SpriteNames.Select(sprite_index)
        
        # Set the right frame index, or leave it blank if none was specified.
        if frame_index is not None:
            self.FrameIndex.ChangeValue(str(frame_index))
        else:
            self.FrameIndex.ChangeValue('')
        
        self.Filter.SetFocus()
        
        self.SpritePreview.set_source(self.pwads)
        self.SpritePreview.set_baseline_factor(0.7)
        self.update_preview()
        
    
    def update_frame(self, event):
        """
        Called when the frame index text control is updated.
        
        Updates the frame index value, ensuring it is a valid integer.
        """
        
        window_id = event.GetId() 
        window = self.FindWindowById(window_id)
        value = utils.validate_numeric(window)

        if value < 0:
            value = 0
        elif value > config.MAX_SPRITE_FRAME:
            value = config.MAX_SPRITE_FRAME
            
        if str(value) != window.GetValue():
            window.ChangeValue(str(value))
            
        self.update_preview()
            
            
    def filter_key(self, event):
        """
        Called when a key is pressed in the filter text control.
        
        Catches up and down keys to move through the filter list without giving the names list focus.
        """
        
        key = event.GetKeyCode()
        list_index = self.SpriteNames.GetSelection()
        
        # Move selection up.
        if key == wx.WXK_UP:
            self.sprite_select_index(list_index - 1)
            
        # Move selection down.
        elif key == wx.WXK_DOWN:
            self.sprite_select_index(list_index + 1)
            
        event.Skip()
        
        
    def filter_build(self, filter_string):
        """
        Builds a newly filtered sprite list.
        """
        
        # Create a filtered list of sprite name indices.
        index = 0
        self.filter_list = []
        for name in self.patch.sprite_names:
            if name.startswith(filter_string):
                self.filter_list.append(index)
            index += 1
        
        # Add the filtered sprite names to the names list.
        list_index = 0
        self.SpriteNames.Clear()
        for index in self.filter_list:
            self.SpriteNames.Insert(self.patch.sprite_names[index], list_index)
            list_index += 1
        
        # Select the first item by default.
        if len(self.filter_list) > 0:
            self.SpriteNames.Select(0)
        
        self.update_preview()
    
    
    def frameindex_set(self, modifier):
        """
        Modifies the frame index value by a specified amount.
        """ 
        
        if self.FrameIndex.GetValue() == '':
            self.FrameIndex.SetValue('0')
        else:    
            index = int(self.FrameIndex.GetValue())
            self.FrameIndex.SetValue(str(index + modifier))
    
    
    def frameindex_spin_up(self, event):
        self.frameindex_set(1)
    
    def frameindex_spin_down(self, event):
        self.frameindex_set(-1)
        
    def focus_text(self, event):
        utils.focus_text(event, self)
        event.Skip()
            
    def cancel(self, event):
        self.Hide()
        
    def filter_update(self, event):
        window = self.FindWindowById(event.GetId())
        self.filter_build(window.GetValue().upper())