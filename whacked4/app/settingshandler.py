#!/usr/bin/env python
#coding=utf8

import json
import os


class SettingsHandler():
    """
    Stores application related settings.
    """
    
    def __init__(self, path):
        self.path = path
        
        self.settings = {}
        self.defaults = {}
        
        self.register()
        self.load()

        
    def register(self):
        """
        Called when an implementing class needs to register all of it's settings.
        """
        
        raise NotImplementedError


    def register_setting(self, name, default):
        """
        Registers a setting with this handler.
        """
        
        self.defaults[name] = default
        
        
    def get_setting(self, name):
        """
        Returns a setting from this handler.
        
        @return: a default value if the setting has not yet been altered, otherwise it will return the current setting.
        
        @raise LookupError: if the setting has not been registered with this handler.
        """
        
        if name in self.settings:
            return self.settings[name]
        elif name in self.defaults:
            return self.defaults[name]
        else:
            raise LookupError('The setting with name {} has not been registered.'.format(name))
        
        
    def put_setting(self, name, value):
        """
        Stores a setting in this handler.
        
        @raise LookupError: if the setting has not been registered with this handler.
        """
        
        if name in self.defaults:
            self.settings[name] = value
        else:
            raise LookupError('The setting with name {} has not been registered.'.format(name))
        
        
    def load(self):
        """
        Loads settings data from a JSON file.
        
        Creates a new settings file and the directories leading up to it if the path does not exist.
        """
        
        # Create config directory if needed.
        dirname = os.path.split(self.path)[0]
        if os.path.exists(dirname) == False:
            os.makedirs(dirname)
        
        # Create a new configuration file if needed.
        if os.path.exists(self.path) == False:
            self.save()
            return
        
        with open(self.path, 'r') as f:
            settings = json.load(f)
            
            # Store only known settings.
            for setting_name in settings.iterkeys():
                if setting_name in self.defaults:
                    self.settings[setting_name] = settings[setting_name]
                else:
                    print 'Ignoring unknown setting {}'.format(setting_name)

    
    def save(self):
        """
        Saves these settings to a JSON file.
        
        Settings that have not yet been altered are not saved.
        """
        
        with open(self.path, 'w') as f:
            json.dump(self.settings, f, indent=4) 
            
    
    def __getitem__(self, name):
        return self.get_setting(name)
    
    def __setitem__(self, name, value):
        self.put_setting(name, value)