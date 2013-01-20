from doom import wad
from ui import windows
import os.path
import wx

class PatchInfoDialog(windows.PatchInfoDialogBase):

    def __init__(self, parent):
        windows.PatchInfoDialogBase.__init__(self, parent)
        
        
    def setup(self):
        self.selected_engine = None
        self.selected_iwad = None
        self.selected_pwads = None
        
        self.patch_file = None
        self.engines = None
        self.workspace = None
        
        self.pwads = []
        
        self.EngineList.Clear()
        self.PWADList.Clear()
        
    
    def set_state(self, patch_file, engines, workspace, modify_engine=True):
        self.setup()
        
        self.patch_file = patch_file
        self.engines = engines
        self.workspace = workspace
        
        if patch_file.filename is not None:
            self.SetLabel('Patch settings - ' + os.path.basename(patch_file.filename))
        else:
            self.SetLabel('Patch settings')
        
        if workspace.iwad is not None:
            self.IWAD.SetValue(workspace.iwad)
        else:
            self.IWAD.SetValue('')
            
        if workspace.pwads is not None:
            for pwad in workspace.pwads:
                self.pwads.append(pwad)
                self.PWADList.Append(pwad)
        
        # Display a list of engines that are supported by the patch.
        for name, engine in self.engines.iteritems():
            if engine.is_compatible(self.patch_file) or self.patch_file.version == 0:
                self.EngineList.Append(engine.name, clientData=name)
                
                if workspace.engine == name:
                    self.EngineList.Select(self.EngineList.GetCount() - 1)
        
        if self.EngineList.GetSelection() == wx.NOT_FOUND and self.EngineList.GetCount() > 0:
            self.EngineList.Select(0)
        
        if modify_engine == False:
            self.EngineList.Disable()
        else:
            self.EngineList.Enable()

    
    def cancel(self, event):
        self.Hide()
        
        
    def ok(self, event):
        if self.EngineList.GetSelection() == -1:
            wx.MessageBox(message='No engine selected.',
                caption='Patch settings',
                style=wx.OK | wx.ICON_EXCLAMATION,
                parent=self)
            return
        
        if self.IWAD.GetValue() == '':
            result = wx.MessageBox(message='No IWAD selected. Sprite previews will not be available.',
                caption='Missing IWAD',
                style=wx.OK | wx.CANCEL | wx.ICON_EXCLAMATION,
                parent=self)
            if result == wx.CANCEL:
                return
            
        self.selected_engine = self.EngineList.GetClientData(self.EngineList.GetSelection())
        
        self.selected_iwad = self.IWAD.GetValue()
        if self.selected_iwad == '':
            self.selected_iwad = None
        self.selected_pwads = self.pwads
        
        self.Hide()
        
    
    def browse_iwad(self, event):
        self.Show(False)
        
        filename = wx.FileSelector('Choose an IWAD.', default_extension='.wad',
            wildcard='WAD files (*.wad)|*.wad|All files|*.*',
            flags=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        
        if filename != '':
            try:
                iwad = wad.WADReader(filename)
            except wad.WADTypeError:
                wx.MessageBox(message='The selected WAD is not a valid WAD file.',
                    caption='Invalid WAD file',
                    style=wx.OK | wx.ICON_EXCLAMATION,
                    parent=self)
            else:
                if iwad.type != 'IWAD':
                    wx.MessageBox(message='The selected WAD is not an IWAD.',
                        caption='Invalid WAD file',
                        style=wx.OK | wx.ICON_EXCLAMATION,
                        parent=self)
                else:
                    self.IWAD.SetValue(filename)
        
        self.Show(True)
            
    
    def pwad_add(self, event):
        self.Show(False)
        
        filename = wx.FileSelector('Choose a PWAD.', default_extension='.wad',
            wildcard='WAD files (*.wad)|*.wad|All files|*.*',
            flags=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        
        if filename != '':
            try:
                pwad = wad.WADReader(filename)
            except wad.WADTypeError:
                wx.MessageBox(message='The selected WAD is not a valid WAD file.',
                    caption='Invalid WAD file',
                    style=wx.OK | wx.ICON_EXCLAMATION,
                    parent=self)
            else:
                if pwad.type != 'PWAD':
                    wx.MessageBox(message='The selected WAD is not a PWAD.',
                        caption='Invalid WAD file',
                        style=wx.OK | wx.ICON_EXCLAMATION,
                        parent=self)
                else:
                    self.pwads.append(filename)
                    self.PWADList.Append(filename)
            
        self.Show(True)
        
            
    def pwad_remove(self, event):
        if self.PWADList.GetSelection() == wx.NOT_FOUND:
            return
        
        del self.pwads[self.PWADList.GetSelection()]
        self.PWADList.Delete(self.PWADList.GetSelection())
