from app import config
from ui import windows


class AboutDialog(windows.AboutDialogBase):

    def __init__(self, parent):
        windows.AboutDialogBase.__init__(self, parent)
    
        self.Version.SetLabel('Version ' + config.APP_VERSION)
    
    
    def ok(self, event):
        self.Hide()