#!/usr/bin/env python
#coding=utf8

import platform

from whacked4 import app
from ctypes import windll


if __name__ == '__main__':

    # Enable better High DPI support for Windows Vista and later.
    if platform.system() == 'Windows':
        win_version = platform.version().split('.')
        if int(win_version[0]) >= 6:
            windll.user32.SetProcessDPIAware()

    main_app = app.WhackEd4App()
    main_app.MainLoop()