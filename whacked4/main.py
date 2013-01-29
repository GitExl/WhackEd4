#!/usr/bin/env python
#coding=utf8

from whacked4 import config
from whacked4.ui import mainwindow
import argparse
import sys
import wx


if __name__ == '__main__':
    
    # Parse common commandline arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('-debug', action='store_true', help='Enable debug mode.')
    args = parser.parse_known_args()[0]
    
    # Enable debugging mode.
    if args.debug:
        config.DEBUG = True
        print 'Debug mode enabled. Only writing exceptions to stdout.'
 
    # Redirect all console output to a single log file.
    if config.DEBUG == False:
        log_file = open(config.LOG_PATH, 'a')
        sys.stderr = log_file
        sys.stdout = log_file
    
    # Start application.
    config.settings.load()
    app = wx.App(redirect=False)
    
    # Set monospaced font.
    font_size = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT).GetPointSize()
    config.FONT_MONOSPACED = wx.Font(
        font_size,
        wx.FONTFAMILY_DEFAULT,
        wx.FONTSTYLE_NORMAL,
        wx.FONTWEIGHT_NORMAL,
        faceName=config.FONT_MONOSPACED_NAME
    )
    
    main_window = mainwindow.MainWindow(None, args)
    app.MainLoop()