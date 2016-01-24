#!/usr/bin/env python
#coding=utf8

"""
Error dialog interface.
"""

from whacked4.ui import windows
import wx


class ErrorDialog(windows.ErrorDialogBase):

    def __init__(self, parent):
        windows.ErrorDialogBase.__init__(self, parent)

        self.SetEscapeId(windows.ERROR_CLOSE)

        if wx.IsBusy():
            wx.EndBusyCursor()

    def set_log(self, log_file):
        """
        Shows the log file's contents in the report field.
        """

        log_file.flush()
        log_file.seek(0)

        self.Report.ChangeValue(log_file.read())

    def copy(self, event):
        self.Report.SelectAll()
        self.Report.Copy()
        self.Report.SetSelection(-1, -1)

    def close(self, event):
        self.EndModal(0)
