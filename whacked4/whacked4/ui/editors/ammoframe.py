#!/usr/bin/env python
#coding=utf8

from whacked4 import utils
from whacked4.ui import editormixin, windows
import copy
import wx


class AmmoFrame(editormixin.EditorMixin, windows.AmmoFrameBase):
    """
    Ammo editor window.
    """
    
    # Text control to internal key mappings.
    PROPS_VALUES = {
        windows.AMMO_VAL_MAXIMUM: 'maximum',
        windows.AMMO_VAL_PICKUP: 'clip'
    }
    
    
    def __init__(self, params):
        windows.AmmoFrameBase.__init__(self, params)
        editormixin.EditorMixin.__init__(self)
        
        self.SetIcon(wx.Icon('res/editor-ammo.ico'))


    def build(self, patch):
        """
        @see: EditorMixin.build
        """
        
        self.patch = patch
        
        self.selected_index = -1
        
        self.ammolist_build()
        
        
    def ammolist_build(self):
        """
        Builds the ammo list from scratch.
        """
        
        self.AmmoList.ClearAll()
        
        # Add column headers if necessary.
        if self.AmmoList.GetColumnCount() == 0:
            self.AmmoList.InsertColumn(0, 'Name', width=76)
            self.AmmoList.InsertColumn(1, 'Maximum', width=67)
            self.AmmoList.InsertColumn(2, 'Pickup', width=49)
        
        for ammo_index in range(len(self.patch.ammo)):
            self.AmmoList.InsertStringItem(ammo_index, '')            
            
            self.ammolist_update_row(ammo_index)
        
        self.list_autosize(self.AmmoList)
        self.AmmoList.Select(0, True)
        
        
    def ammolist_update_row(self, row_index):
        """
        Updates a row in the ammo list.
        """
        
        ammo = self.patch.ammo[row_index]
        ammo_name = self.patch.ammo.names[row_index]
            
        self.AmmoList.SetStringItem(row_index, 0, ammo_name)
        self.AmmoList.SetStringItem(row_index, 1, str(ammo['maximum']))
        self.AmmoList.SetStringItem(row_index, 2, str(ammo['clip']))
        
        
    def ammolist_resize(self, event):
        """
        Resize the ammo name column as wide as possible.
        """
        
        column_width = self.AmmoList.GetClientSizeTuple()[0] - 4
        self.AmmoList.SetColumnWidth(0, column_width / 3)
        self.AmmoList.SetColumnWidth(1, column_width / 3)
        self.AmmoList.SetColumnWidth(2, column_width / 3)
        
        
    def ammo_select(self, event):
        """
        Selects a new ammo entry.
        """
        
        self.selected_index = event.GetIndex()
        self.update_properties()
        
    
    def ammo_rename(self, event):
        """
        Called when the current ammo entry needs to be renamed.
        """
        
        self.ammo_rename_action()


    def ammo_rename_action(self):
        """
        Renames the currently selected ammo entry.
        """
        
        ammo_name = self.patch.ammo.names[self.selected_index]
        new_name = wx.GetTextFromUser('Enter a new name for ' + ammo_name, caption='Change name', default_value=ammo_name, parent=self)
        
        if new_name != '':
            self.undo_add()
            
            self.patch.ammo.names[self.selected_index] = new_name
            self.update_properties()
            self.is_modified(True)
            
            
    def ammo_restore(self, event):
        """
        Restores the currently selected ammo entry to it's engine state.
        """
        
        self.undo_add()
        
        self.patch.ammo[self.selected_index] = copy.deepcopy(self.patch.engine.ammo[self.selected_index])
        self.patch.ammo.names[self.selected_index] = copy.copy(self.patch.engine.ammo.names[self.selected_index])
        
        self.update_properties()
        self.ammolist_update_row(self.selected_index)
        
        
    def update_properties(self):
        """
        Updates the displayed properties of the currently selected entry.
        """
        
        ammo = self.patch.ammo[self.selected_index]
        
        self.Maximum.ChangeValue(str(ammo['maximum']))
        self.Pickup.ChangeValue(str(ammo['clip']))
        self.AmmoList.SetStringItem(self.selected_index, 0, self.patch.get_ammo_name(self.selected_index))
        
        # Disable rename\restore for hardcoded entries.
        if self.selected_index >= len(self.patch.ammo):
            self.Restore.Disable()
            self.Rename.Disable()
        else:
            self.Restore.Enable()
            self.Rename.Enable()
            
            
    def set_value(self, event):
        """
        Sets the currently selected ammo entry's property value.
        """
        
        self.undo_add()
        
        window_id = event.GetId()
        window = self.FindWindowById(window_id)
        value = utils.validate_numeric(window)
        
        key = self.PROPS_VALUES[window_id]
        self.patch.ammo[self.selected_index][key] = value
        
        self.ammolist_update_row(self.selected_index)
        self.is_modified(True)

        
    def undo_restore_item(self, item):
        """
        @see: EditorMixin.undo_restore_item
        """
        
        index = item['index']
        self.patch.ammo[index] = item['item']
        self.patch.ammo.names[index] = item['name']
        
        self.ammolist_update_row(index)
        self.update_properties()
        
        
    def undo_store_item(self):
        """
        @see: EditorMixin.undo_store_item
        """
        
        return {
            'item': copy.deepcopy(self.patch.ammo[self.selected_index]),
            'name': copy.copy(self.patch.ammo.names[self.selected_index]),
            'index': self.selected_index
        }