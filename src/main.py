"""
Application entrypoint.
"""

import platform
import sys

from whacked4 import app


if __name__ == '__main__':

    # If running from Mac app bundle, change to Resources directory
    if hasattr(sys, 'frozen') and sys.platform == 'darwin':
        import os
        bundle_dir = os.path.dirname(sys.executable)
        resources_dir = os.path.join(bundle_dir, '..', 'Resources')
        if os.path.exists(resources_dir):
            os.chdir(resources_dir)

    # Enable better High DPI support for Windows Vista and later.
    if platform.system() == 'Windows':
        from ctypes import windll
        win_version = platform.version().split('.')
        if int(win_version[0]) >= 6:
            windll.shcore.SetProcessDpiAwareness(1)

    main_app = app.WhackEd4App()
    main_app.MainLoop()
