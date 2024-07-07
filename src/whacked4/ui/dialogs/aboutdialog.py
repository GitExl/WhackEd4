"""
Generic about dialog interface.
"""

import wx
from wx import Window, CommandEvent

from whacked4 import config
from whacked4.ui import windows


class AboutDialog(windows.AboutDialogBase):
    """
    About dialog.
    """

    def __init__(self, parent: Window):
        windows.AboutDialogBase.__init__(self, parent)

        self.SetEscapeId(windows.ABOUT_OK)

        if config.APP_BETA:
            self.Version.SetLabel('Version ' + config.APP_VERSION + ' beta')
        else:
            self.Version.SetLabel('Version ' + config.APP_VERSION)

        with open('LICENSE', 'r', encoding='utf-8') as f:
            self.license_text: str = f.read()

    def ok(self, event: CommandEvent):
        self.EndModal(0)

    def license(self, event: CommandEvent):
        wx.MessageBox(message=self.license_text, caption='License', style=wx.OK, parent=self)
