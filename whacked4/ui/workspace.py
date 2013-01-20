import json
import os.path


def get_filename(base_filename):
    return os.path.splitext(base_filename)[0] + '.whacked'


class Workspace():
    WINDOW_STATE_NORMAL = 0
    WINDOW_STATE_MAXIMIZED = 1

    def __init__(self):
        self.engine = None
        
        self.iwad = None
        self.pwads = None
        
        self.windows = None
        
        
    def load(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.engine = data['engine']
        
        self.iwad = data['iwad']
        self.pwads = data['pwads']
        
        self.windows = data['windows']
              
        
    def save(self, filename):
        data = {
            'engine': self.engine,
            'iwad': self.iwad,
            'pwads': self.pwads,
            'windows': self.windows
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        
    def apply_windows(self, frame, workspace_windows):
        for window_name, window in workspace_windows.iteritems():
            window_data = self.windows[window_name]
            
            x = int(self.get_dict_value(window_data, 'x', 0))
            y = int(self.get_dict_value(window_data, 'y', 0))
            width = int(self.get_dict_value(window_data, 'width', 640))
            height = int(self.get_dict_value(window_data, 'height', 480))
            window.SetDimensions(x, y, width, height)
            
            visible = int(int(self.get_dict_value(window_data, 'visible', 0)))
            if visible == True:
                window.Show(True)
            else:
                window.Show(False)
            
        if 'maximized' in self.windows:
            max_window = self.windows['maximized']
            window = workspace_windows[max_window]
            window.Maximize(True)
            
        if 'active' in self.windows:
            active_window = self.windows['active']
            window = workspace_windows[active_window]
            window.Raise()
            window.SetFocus()
            
            
    def get_dict_value(self, src, value, default):
        if value in src:
            return src[value]
        else:
            return default
                
    
    def store_windows(self, frame, workspace_windows):
        self.windows = {}
        for window_name, window in workspace_windows.iteritems():
            window_data = {}
            
            window_data['x'] = window.workspace_data['x']
            window_data['y'] = window.workspace_data['y']
            window_data['width'] = window.workspace_data['width']
            window_data['height'] = window.workspace_data['height']
            
            if window.IsShown() == True:
                window_data['visible'] = 1
            else:
                window_data['visible'] = 0
                
            if window.IsMaximized() == True:
                self.windows['maximized'] = window_name
                
            if frame.GetActiveChild() == window:
                self.windows['active'] = window_name
                
            self.windows[window_name] = window_data