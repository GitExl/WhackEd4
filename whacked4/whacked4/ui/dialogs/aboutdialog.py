#!/usr/bin/env python
#coding=utf8

"""
Generic about dialog interface.
"""

from whacked4 import config
from whacked4.ui import windows


class AboutDialog(windows.AboutDialogBase):

    def __init__(self, parent):
        windows.AboutDialogBase.__init__(self, parent)
    
        self.Version.SetLabel('Version ' + config.APP_VERSION)
        
        with open('LICENSE', 'r') as f:
            license_text = f.read()
        self.License.SetValue(license_text)
    
    
    def ok(self, event):
        self.Hide()