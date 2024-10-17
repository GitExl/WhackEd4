"""
Contains program configuration constants and a settings object which contains
user-definable configuration details.
"""

import os.path
import sys

import wx

from whacked4 import settingshandler


# Application info.
APP_NAME = 'WhackEd4'
APP_SIMPLE_NAME = 'whacked4'
APP_VERSION = '1.3.2'
APP_BETA = False

# Monospaced font for displays that use them.
FONT_MONOSPACED_NAME = 'DejaVu Sans Mono'
FONT_MONOSPACED = None
FONT_MONOSPACED_BOLD = None

# Application configuration path.
if sys.platform == 'win32':
    CONFIG_DIR = os.environ['APPDATA'] + '/' + APP_SIMPLE_NAME
else:
    CONFIG_DIR = os.path.join(os.path.expanduser("~"), '.' + APP_SIMPLE_NAME)

# Path to the settings file.
SETTINGS_PATH = CONFIG_DIR + '/settings.json'

# Path of the program's log output.
LOG_PATH = CONFIG_DIR + '/log.txt'

# Enable debugging functions.
DEBUG = False

# The highest allowed sprite frame index.
MAX_SPRITE_FRAME = 29


class WhackEd4Settings(settingshandler.SettingsHandler):
    """
    Settings for WhackEd4.
    """

    def __init__(self, path: str):
        settingshandler.SettingsHandler.__init__(self, path)

        self.recent_files_clean()

    def register(self):
        self.register_setting('main_window_state', {
            'x': 0,
            'y': 0,
            'width': 1024,
            'height': 560,
            'maximized': True
        })
        self.register_setting('recent_files', [])
        self.register_setting('undo_size', 256)
        self.register_setting('recent_files_count', 10)

    def main_window_state_store(self, x: int, y: int, width: int, height: int, is_maximized: bool):
        """
        Stores the state of the main window.
        """

        main_window = {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'maximized': is_maximized
        }
        self.put_setting('main_window_state', main_window)

    def main_window_state_restore(self, window: wx.MDIChildFrame):
        """
        Restores the main window's state from these settings.
        """

        main_window = self.get_setting('main_window_state')

        window.SetSize(
            main_window['x'],
            main_window['y'],
            main_window['width'],
            main_window['height']
        )
        window.Maximize(main_window['maximized'])
        window.Refresh()

    def recent_files_add(self, filename: str):
        """
        Adds a filename to the list of recent filenames.
        """

        recent_files = self.get_setting('recent_files')

        # Remove the file from the list if it already exists elsewhere.
        if filename in recent_files:
            recent_files.remove(filename)

        # Trim the list if it has reached it's maximum length.
        if len(recent_files) > self['recent_files_count']:
            del recent_files[len(recent_files) - 1]

        recent_files.insert(0, filename)

        self.put_setting('recent_files', recent_files)

    def recent_files_clean(self):
        """
        Filters missing files from the recent files list and removes duplicates.
        """

        recent_files = self.get_setting('recent_files')

        new_recent_lower = set()
        new_recent = []
        for filename in recent_files:
            filename_lower = filename.lower()

            if os.path.exists(filename) and filename_lower not in new_recent_lower:
                new_recent.append(filename)
                new_recent_lower.add(filename_lower)

        self.put_setting('recent_files', new_recent)


# Global settings object.
settings = WhackEd4Settings(SETTINGS_PATH)
