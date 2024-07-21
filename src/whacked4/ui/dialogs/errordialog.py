"""
Error dialog UI.
"""

from typing import TextIO, Optional

import wx
from wx import Window, CommandEvent

from whacked4 import config
from whacked4.ui import windows


class ErrorDialog(windows.ErrorDialogBase):
    """
    Error reporting dialog.
    """

    def __init__(self, parent: Optional[Window]):
        windows.ErrorDialogBase.__init__(self, parent)

        self.SetEscapeId(windows.ERROR_CLOSE)
        self.Report.SetFont(config.FONT_MONOSPACED)

        if wx.IsBusy():
            wx.EndBusyCursor()

    def set_log(self, log_file: TextIO):
        """
        Shows the log file's contents in the report field.
        """

        log_file.flush()
        log_file.seek(0)

        self.Report.ChangeValue(log_file.read())

    def copy(self, event: CommandEvent):
        self.Report.SelectAll()
        self.Report.Copy()
        self.Report.SetSelection(-1, -1)

    def close(self, event: CommandEvent):
        self.EndModal(0)
