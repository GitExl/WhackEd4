import platform

from whacked4 import app


if __name__ == '__main__':

    # Enable better High DPI support for Windows Vista and later.
    if platform.system() == 'Windows':
        from ctypes import windll
        win_version = platform.version().split('.')
        if int(win_version[0]) >= 6:
            windll.shcore.SetProcessDpiAwareness(1)

    main_app = app.WhackEd4App()
    main_app.MainLoop()
