#!/usr/bin/env python
#coding=utf8

from whacked4.ui import editormixin, windows
from whacked4.ui.dialogs import stringdialog
import copy
import wx


class CheatsFrame(editormixin.EditorMixin, windows.CheatsFrameBase):
    """
    Cheats editor window.
    """
    
    def __init__(self, params):
        windows.CheatsFrameBase.__init__(self, params)
        editormixin.EditorMixin.__init__(self)
        
        self.SetIcon(wx.Icon('res/editor-cheats.ico'))


    def build(self, patch):
        """
        @see: EditorMixin.build
        """
        
        self.patch = patch
        self.selected_index = 0
        
        self.string_dialog = stringdialog.StringDialog(self.GetParent())
        
        self.cheatlist_build()
        
        
    def cheatlist_build(self):
        """
        Builds the cheat list from scratch.
        """
        
        self.CheatList.ClearAll()
        
        # Add column headers if necessary.
        if self.CheatList.GetColumnCount() == 0:
            self.CheatList.InsertColumn(0, 'Name', width=185)
            self.CheatList.InsertColumn(1, 'Code', width=138)
        
        for cheat_index, cheat in enumerate(self.patch.engine.cheat_data.itervalues()):
            self.CheatList.InsertStringItem(cheat_index, cheat['name'])
            
            self.cheatlist_update_row(cheat_index)
            
        self.list_autosize(self.CheatList)
        self.CheatList.Select(0, True)
        
        
    def cheatlist_update_row(self, row_index):
        """
        Updates a row in the cheats list.
        """
        
        key = self.cheat_get_key(row_index)
        cheat = self.patch.cheats[key]
        self.CheatList.SetStringItem(row_index, 1, cheat)
        
        
    def cheatlist_resize(self, row_index):
        """
        Called when the cheats list is resized.
        
        Expands the last cheat column to fill the available space.
        """
        
        width = self.CheatList.GetClientSizeTuple()[0] - self.CheatList.GetColumnWidth(0) - 4 
        self.CheatList.SetColumnWidth(1, width)
                
        
    def cheat_edit(self, event):
        """
        Edit a cheat string by displaying a strings dialog.
        """
        
        row_index = event.GetIndex()
        key = self.cheat_get_key(row_index)
        
        engine_cheat = self.patch.engine.cheats[key]
        cheat = self.patch.cheats[key]
        name = self.patch.engine.cheat_data[key]['name']
        
        self.string_dialog.set_state(engine_cheat, cheat, self.patch.extended, name, cheat=True)
        self.string_dialog.ShowModal()
        
        if self.string_dialog.new_string != None:
            self.undo_add()
            
            self.patch.cheats[key] = self.string_dialog.new_string
            
            self.cheatlist_update_row(row_index)
            self.is_modified(True)
            
            
    def cheat_restore(self, event):
        """
        Restores a cheat to it's engine state.
        """
        
        self.undo_add()
        
        key = self.cheat_get_key(self.selected_index)
        self.patch.cheats[key] = copy.deepcopy(self.patch.engine.cheats[key])
        
        self.cheatlist_update_row(self.selected_index)
        self.is_modified(True)
        
        
    def cheat_select(self, event):
        """
        Stores the index of the currently selected cheat.
        """
        
        self.selected_index = event.GetIndex()
        
        
    def cheat_get_key(self, index):
        """
        Returns a cheat dict key for a cheat index.
        """
        
        return self.patch.cheats.keys()[index]

    
    def undo_restore_item(self, item):
        """
        @see: EditorMixin.undo_restore_item
        """
        index = item['index']
        key = self.cheat_get_key(index)
        
        self.patch.cheats[key] = item['item']
        
        self.cheatlist_update_row(index)
        self.is_modified(True)
        
        
    def undo_store_item(self):
        """
        @see: EditorMixin.undo_store_item
        """
        
        key = self.cheat_get_key(self.selected_index)
        
        return {
            'item': copy.deepcopy(self.patch.cheats[key]),
            'index': self.selected_index
        }