#!/usr/bin/env python
#coding=utf8

from whacked4.ui import editormixin, windows
import wx


class MiscFrame(editormixin.EditorMixin, windows.MiscFrameBase):
    """
    Misc editor window.
    """
    
    def __init__(self, params):
        windows.MiscFrameBase.__init__(self, params)
        editormixin.EditorMixin.__init__(self)
        
        self.SetIcon(wx.Icon('res/editor-misc.ico'))


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