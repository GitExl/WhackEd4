#!/usr/bin/env python
#coding=utf8

from app import config
from ui import windows


class StartDialog(windows.StartDialogBase):
    """
    This dialog is meant to be displayed on startup of the application. It allows the user to quickly
    access some common functions without having to dig down into a menu first.
    """

    def __init__(self, parent):
        windows.StartDialogBase.__init__(self, parent)
        
        # Populate the list of recently accessed Dehacked patches.
        recent_files = config.settings['recent_files']
        for filename in recent_files:
            self.FileList.Append(filename)


    def open_file_list(self, event):
        """
        Opens a Dehacked patch directly from the file list.
        """
        
        self.Hide()
        filename = self.FileList.GetString(self.FileList.GetSelection())
        self.GetParent().open_file(filename)
        
        
    def new_file(self, event):
        self.Hide()
        self.GetParent().new_file()
        
    def open_file(self, event):
        self.Hide()
        self.GetParent().open_file_dialog()        
    
    def cancel(self, event):
        self.Hide()
        