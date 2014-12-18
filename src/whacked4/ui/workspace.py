#!/usr/bin/env python
#coding=utf8

"""
Workspaces describe the position and state of windows opened in it, as well as the position and state of the main
window and any auxiliary information required to restore a user's workspace to a former state.
"""

import json
import os.path


class Workspace:
    """
    Describes a workspace, and provides functionality for it to be saved and restored.
    """

    WINDOW_STATE_NORMAL = 0
    WINDOW_STATE_MAXIMIZED = 1

    def __init__(self):
        self.engine = None

        self.iwad = None
        self.pwads = None

        self.windows = None

    def load(self, base_filename):
        """
        Loads a workspace from a JSON file.

        @param base_filename: the filename of the file that this workspace belongs to.
        """

        filename = self.get_filename(base_filename)

        with open(filename, 'r') as f:
            data = json.load(f)

        self.engine = data['engine']

        self.iwad = data['iwad']
        self.pwads = data['pwads']

        self.windows = data['windows']

    def save(self, base_filename):
        """
        Writes a workspace to a JSON file.

        @param base_filename: the filename of the file that this workspace belongs to.
        """

        data = {
            'engine': self.engine,
            'iwad': self.iwad,
            'pwads': self.pwads,
            'windows': self.windows
        }

        filename = self.get_filename(base_filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def restore_windows(self, workspace_windows):
        """
        Restores all editor windows' state.

        @param workspace_windows: a dict containing window names and window objects to restore.
        """

        for window_name, window in workspace_windows.iteritems():
            if window_name not in self.windows:
                continue

            window_data = self.windows[window_name]

            # Set window dimensions.
            x = int(get_dict_value(window_data, 'x', 0))
            y = int(get_dict_value(window_data, 'y', 0))
            width = int(get_dict_value(window_data, 'width', 640))
            height = int(get_dict_value(window_data, 'height', 480))
            window.SetDimensions(x, y, width, height)

            # Set window visibility.
            visible = int(int(get_dict_value(window_data, 'visible', 0)))
            if visible:
                window.Show(True)
            else:
                window.Show(False)

        # Maximize only one window.
        if 'maximized' in self.windows:
            max_window = self.windows['maximized']
            window = workspace_windows[max_window]
            window.Maximize(True)

        # Focus on one window.
        if 'active' in self.windows:
            active_window = self.windows['active']
            window = workspace_windows[active_window]
            window.Raise()
            window.SetFocus()

    def store_windows(self, frame, workspace_windows):
        """
        Stores all editor windows' state.

        @param frame: the MDI parent frame to store windows from.
        @param workspace_windows: a dict containing window names and window objects to store.
        """

        self.windows = {}
        for window_name, window in workspace_windows.iteritems():
            # Store dimensions.
            window_data = {
                'x': window.workspace_data['x'],
                'y': window.workspace_data['y'],
                'width': window.workspace_data['width'],
                'height': window.workspace_data['height']
            }

            # Store visibility.
            if window.IsShown():
                window_data['visible'] = 1
            else:
                window_data['visible'] = 0

            # Store one window name as maximized.
            if window.IsMaximized():
                self.windows['maximized'] = window_name

            # Store the active window name.
            if frame.GetActiveChild() == window:
                self.windows['active'] = window_name

            self.windows[window_name] = window_data

    def get_filename(self, base_filename):
        """
        Returns a workspace filename from any full path.
        """

        # Replace the path's file extension with .whacked
        return os.path.splitext(base_filename)[0] + '.whacked'


def get_dict_value(src, value, default):
    """
    Returns a default value for a dict key if it was not found, otherwise returns the dict item.
    """

    if value in src:
        return src[value]
    else:
        return default
