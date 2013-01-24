#!/usr/bin/env python
#coding=utf8

from ui import editormixin, windows
import wx


class StringsFrame(editormixin.EditorMixin, windows.StringsFrameBase):
    """
    Strings editor window.
    """
    
    def __init__(self, params):
        windows.StringsFrameBase.__init__(self, params)
        editormixin.EditorMixin.__init__(self)
        
        self.SetIcon(wx.Icon('res/icon-weapons-small.png'))


    def build(self, patch):
        """
        @see: EditorMixin.build
        """
        
        self.patch = patch
        self.pwads = self.GetParent().pwads

        
    def undo_restore_item(self, item):
        """
        @see: EditorMixin.undo_restore_item
        """
        
        pass
        
        
    def undo_store_item(self):
        """
        @see: EditorMixin.undo_store_item
        """
        
        return None