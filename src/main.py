#!/usr/bin/env python
#coding=utf8

import platform
import locale

from whacked4 import app
from ctypes import windll


if __name__ == '__main__':

    # Enable better High DPI support for Windows Vista and later.
    if platform.system() == 'Windows':
        win_version = platform.version().split('.')
        if int(win_version[0]) >= 6:
            windll.user32.SetProcessDPIAware()

    # Workaround for https://github.com/wxphp/wxphp/issues/108
    locale.setlocale(locale.LC_ALL, 'C')

    main_app = app.WhackEd4App()
    main_app.MainLoop()
    