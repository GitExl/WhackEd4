from app import config
from ui import utils
import wx


class EditorMixin():
    """
    Adds common editor window functionality to any wx.Frame object.
    """
    
    def __init__(self):
        self.Bind(wx.EVT_MOVE, self.update_workspace_data)
        self.Bind(wx.EVT_SIZE, self.update_workspace_data)
        
        self.Bind(wx.EVT_CLOSE, self.close)
        
        # Stores the position of this editor window.
        self.workspace_data = {
            'x': 0,
            'y': 0,
            'width': self.GetMinWidth(),
            'height': self.GetMinHeight()
        }
        
        
    def build(self, patch):
        """
        Called when this editor window needs to build it's UI contents.
        """
        
        raise NotImplementedError()
        
    
    def undo_add(self):
        """
        Adds an undo item to the undo stack.
        """
        
        # If the undo stack has reached it's maximum size, prune off the first item.
        if len(self.undo) == config.settings['undo_size']:
            self.undo = self.undo[1:]
            self.undo_index -= 1
        
        # Prune the stack up to and including the current item.
        self.undo = self.undo[0:self.undo_index + 1]

        self.undo.append(self.undo_store_item())
        self.undo_index += 1
        
        
    def undo_do_undo(self):
        """
        Restores an item from the undo stack.
        """
        
        if self.undo_index == -1:
            return

        undo_item = self.undo[self.undo_index]
        self.undo_index -= 1
        self.undo_restore_item(undo_item)
        
        
    def undo_restore_item(self, item):
        """
        Called when an undo item needs to be restored.
        """
        
        raise NotImplementedError()
        
    def undo_store_item(self):
        """
        Called when an undo item needs to be stored.
        """
        
        raise NotImplementedError()
    
    
    def update_workspace_data(self, event):
        """
        Updates this editor window's position data.
        """
        
        self.GetParent().workspace_modified = True
        
        if self.IsMaximized() == True:
            event.Skip()
            return
        
        position = self.GetPositionTuple()
        size = self.GetSizeTuple()
        
        self.workspace_data['x'] = position[0]
        self.workspace_data['y'] = position[1]
        self.workspace_data['width'] = size[0]
        self.workspace_data['height'] = size[1]
        
        event.Skip()
                
        
    def enter_state(self, event):
        """
        Called when the mouse enters a state label.
        """
        
        window = self.GetParent().FindWindowById(event.GetId())
        window.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        window.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        window.Refresh()
        
        
    def leave_state(self, event):
        """
        Called when the mouse leaves a state label.
        """ 
        
        window = self.GetParent().FindWindowById(event.GetId())
        window.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        window.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        window.Refresh()
        
        
    def focus_text(self, event):
        """
        Focuses an entire text control.
        """
        
        utils.focus_text(event, self)
        event.Skip()
            
        
    def close(self, event):
        """
        Called when this editor window is closed.
        """
        
        self.Maximize(False)
        self.GetParent().window_closed(self)