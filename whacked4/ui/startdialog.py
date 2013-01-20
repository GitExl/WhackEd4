from app import config
from ui import windows

class StartDialog(windows.StartDialogBase):

    def __init__(self, parent):
        windows.StartDialogBase.__init__(self, parent)
        
        recent_files = config.settings['recent_files']
        for filename in recent_files:
            self.FileList.Append(filename)
        
        
    def new_file(self, event):
        self.Hide()
        self.GetParent().new_file()
        
        
    def open_file(self, event):
        self.Hide()
        self.GetParent().open_file_dialog()
        
        
    def open_file_list(self, event):
        self.Hide()
        filename = self.FileList.GetString(self.FileList.GetSelection())
        self.GetParent().open_file(filename)
        
    
    def cancel(self, event):
        self.Hide()
        