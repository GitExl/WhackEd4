"""
wxWidgets app entrypoint.
"""

import argparse
import sys
import traceback
import os
import locale
from typing import TextIO, Optional

import wx
import pyaudio

from whacked4 import config
from whacked4.ui import mainwindow
from whacked4.ui.dialogs import errordialog


class WhackEd4App(wx.App):
    """
    The main wxWidgets application object.

    See http://wiki.wxpython.org/CustomExceptionHandling
    """

    def __init__(self):
        super().__init__()

        self.log: Optional[TextIO] = None
        self.pyaudio_instance = pyaudio.PyAudio()

    def OnExit(self):
        """
        App exit event.
        """

        self.pyaudio_instance.terminate()

    def OnInit(self):
        """
        Run after the wxWidgets app has initialized.
        """

        # Parse common commandline arguments.
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-debug',
            action='store_true',
            help='Enable debug mode.'
        )
        parser.add_argument(
            '-open',
            action='store',
            help='Open patch file.'
        )
        parser.add_argument(
            '-workdir',
            action='store',
            help='Set application working directory (for opening from shell).'
        )
        args = parser.parse_known_args()[0]

        # Enable debugging mode.
        if args.debug:
            config.DEBUG = True
            print('Debug mode enabled. Only writing exceptions to stdout.')
        else:
            self.redirect_logs()
            sys.excepthook = self.exception_handler

        # Set working directory.
        if args.workdir:
            os.chdir(args.workdir)

        set_monospace_font()

        config.settings.load()

        mainwind = mainwindow.MainWindow(None)
        self.SetTopWindow(mainwind)

        if config.APP_BETA:
            wx.MessageBox(
                message='This is a beta version. Please beware of bugs, and report them on the ' \
                'GitHub issue tracker.',
                caption=config.APP_NAME,
                style=wx.OK | wx.ICON_INFORMATION,
                parent=mainwind
            )

        if args.open and os.path.exists(args.open):
            mainwind.open_file(args.open)
        else:
            mainwind.show_start()

        return True

    def InitLocale(self):
        if sys.platform.startswith('win') and sys.version_info > (3, 8):
            locale.setlocale(locale.LC_ALL, "C")

    def redirect_logs(self):
        """
        Redirects stdout and stderr to a single text file.
        """

        self.log = open(config.LOG_PATH, 'w+', encoding='utf-8')

        sys.stdout = self.log
        sys.stderr = self.log

    def exception_handler(self, exception_type, value, trace_back):
        """
        Handles exceptions thrown from wxWidgets MainLoop.
        """

        traceback.print_exception(exception_type, value, trace_back, file=sys.stderr)

        try:
            dialog = errordialog.ErrorDialog(None)
            dialog.set_log(self.log)
            dialog.ShowModal()
            dialog.Destroy()
        except Exception:
            pass

        sys.exit(-1)


def set_monospace_font():
    """
    Sets the monospaced font to use in dialogs.
    """

    font_size = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT).GetPointSize()

    # On macOS, use the wxPython suggested monospace font
    # On other platforms, use the configured font name
    if sys.platform == 'darwin':
        config.FONT_MONOSPACED = wx.Font(
            font_size,
            wx.FONTFAMILY_TELETYPE,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL
        )
        config.FONT_MONOSPACED_BOLD = wx.Font(
            font_size,
            wx.FONTFAMILY_TELETYPE,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD
        )
    else:
        config.FONT_MONOSPACED = wx.Font(
            font_size,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL,
            faceName=config.FONT_MONOSPACED_NAME
        )
        config.FONT_MONOSPACED_BOLD = wx.Font(
            font_size,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD,
            faceName=config.FONT_MONOSPACED_NAME
        )
