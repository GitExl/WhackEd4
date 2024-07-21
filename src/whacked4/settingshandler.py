"""
Settings handler base class.
"""

import json
import os
from typing import Dict


class SettingsHandler:
    """
    Stores application related settings.
    """

    def __init__(self, path: str):
        self.path: str = path

        self.settings: Dict[str, any] = {}
        self.defaults: Dict[str, any] = {}

        self.register()
        self.load()

    def register(self):
        """
        Called when an implementing class needs to register all of its settings.
        """

        raise NotImplementedError

    def register_setting(self, name: str, default: any):
        """
        Registers a setting with this handler.
        """

        self.defaults[name] = default

    def get_setting(self, name: str) -> any:
        """
        Returns a setting from this handler.

        @return: a default value if the setting has not yet been altered, otherwise
        it will return the current setting.

        @raise LookupError: if the setting has not been registered with this handler.
        """

        if name in self.settings:
            return self.settings[name]

        if name in self.defaults:
            return self.defaults[name]

        raise LookupError(f'The setting with name {name} has not been registered.')

    def put_setting(self, name: str, value: any):
        """
        Stores a setting in this handler.

        @raise LookupError: if the setting has not been registered with this handler.
        """

        if name in self.defaults:
            self.settings[name] = value
        else:
            raise LookupError(f'The setting with name {name} has not been registered.')

    def load(self):
        """
        Loads settings data from a JSON file.

        Creates a new settings file and the directories leading up to it if
        the path does not exist.
        """

        # Create config directory if needed.
        dirname = os.path.split(self.path)[0]
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        # Create a new configuration file if needed.
        if not os.path.exists(self.path):
            self.save()
            return

        with open(self.path, 'r', encoding='utf-8') as f:
            try:
                settings = json.load(f)
            except (ValueError, json.JSONDecodeError):
                print('Could not decode settings, using defaults.')
                settings = {}

            # Store only known settings.
            for setting_name in settings.keys():
                if setting_name in self.defaults:
                    self.settings[setting_name] = settings[setting_name]
                else:
                    print(f'Ignoring unknown setting {setting_name}')

    def save(self):
        """
        Saves these settings to a JSON file.

        Settings that have not yet been altered are not saved.
        """

        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.settings, f, indent=4)

    def __getitem__(self, name):
        return self.get_setting(name)

    def __setitem__(self, name, value):
        self.put_setting(name, value)
