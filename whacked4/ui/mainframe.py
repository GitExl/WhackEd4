from app import config
from collections import OrderedDict
from dehacked import engine, patch
from doom import wad, wadlist
from ui import windows, thingframe, statesframe, patchinfodialog, workspace, startdialog, aboutdialog
import glob
import os.path
import shutil
import sys
import wx


class MainFrame(windows.MainFrameBase):

    def __init__(self, parent, arguments):
        windows.MainFrameBase.__init__(self, parent)
        
        wx.BeginBusyCursor()
        
        self.SetIcon(wx.Icon(u'res/icon-hatchet.ico'))
        
        # Patch-related data.
        self.patch = None
        self.patch_info = None
        self.patch_modified = False
        
        # Workspace info.
        self.workspace = None
        self.workspace_modified = False
        
        # WAD\lump management.
        self.iwad = None
        self.pwads = wadlist.WADList()
        
        # Engine configuration related data.
        self.engines = OrderedDict()
        self.load_engines()
        
        # Window\ID relationships.
        self.tool_windows = {
            windows.MAIN_TOOL_THINGS: thingframe.ThingFrame(self),
            windows.MAIN_TOOL_STATES: statesframe.StatesFrame(self) 
        }
        self.menu_windows = {
            windows.MAIN_MENU_THINGS: windows.MAIN_TOOL_THINGS,
            windows.MAIN_MENU_STATES: windows.MAIN_TOOL_STATES,
        }
        self.workspace_windows = {
            'things': self.tool_windows[windows.MAIN_TOOL_THINGS],
            'states': self.tool_windows[windows.MAIN_TOOL_STATES]
        }
        
        self.tool_windows_hide()
        self.set_toolbar_enabled(False, False)
        self.update_recent_files()
        
        # Dialogs.
        self.start_dialog = startdialog.StartDialog(self)
        self.about_dialog = aboutdialog.AboutDialog(self)
        
        self.Show()
        
        config.settings.main_window_state_restore(self)
        
        wx.EndBusyCursor()
        
        self.parse_options(arguments)
        
        self.Bind(wx.EVT_MOVE, self.update_window_data)
        self.Bind(wx.EVT_SIZE, self.update_window_data)
    
    
    def parse_options(self, args):
        for arg in sys.argv[1:]:
            if os.path.exists(arg):
                self.open_file(arg)
                return
                
        self.start_dialog.ShowModal()
    
        
    def load_engines(self):
        for file_name in glob.glob('cfg/tables_*.json'):
            new_engine = engine.Engine()
            try:
                new_engine.read_table(file_name)
            except engine.DehackedEngineError:
                wx.MessageBox(message='Invalid engine configuration file {}'.format(file_name),
                    caption='Engine configuration error',
                    style=wx.OK | wx.ICON_EXCLAMATION,
                    parent=self)
            else:
                name = os.path.basename(file_name)
                name = os.path.splitext(name)[0]
                self.engines[name] = new_engine
                    
        
    def set_toolbar_enabled(self, enabled, extended):
        self.ToolBar.EnableTool(windows.MAIN_TOOL_THINGS, enabled)
        self.ToolBar.EnableTool(windows.MAIN_TOOL_STATES, enabled)
        self.ToolBar.EnableTool(windows.MAIN_TOOL_AMMO, False)
        self.ToolBar.EnableTool(windows.MAIN_TOOL_CHEATS, False)
        self.ToolBar.EnableTool(windows.MAIN_TOOL_STRINGS, False)
        self.ToolBar.EnableTool(windows.MAIN_TOOL_WEAPONS, False)
        self.ToolBar.EnableTool(windows.MAIN_TOOL_SOUNDS, False)
        self.ToolBar.EnableTool(windows.MAIN_TOOL_MISC, False)
        
        self.MenuViewThings.Enable(enabled)
        self.MenuViewStates.Enable(enabled)
        self.MenuViewAmmo.Enable(False)
        self.MenuViewCheats.Enable(False)
        self.MenuViewStrings.Enable(False)
        self.MenuViewWeapons.Enable(False)
        self.MenuViewSounds.Enable(False)
        self.MenuViewMiscellaneous.Enable(False)
        self.MenuViewPatchSettings.Enable(enabled)
        
        if extended == True:
            self.ToolBar.EnableTool(windows.MAIN_TOOL_PAR, False)
            self.MenuViewPar.Enable(False)
        else:
            self.ToolBar.EnableTool(windows.MAIN_TOOL_PAR, False)
            self.MenuViewPar.Enable(False)
    
    
    def edit_undo(self, event):
        window = self.GetActiveChild()
        if window is None:
            return
        window.undo_do_undo()
        
        
    def edit_redo(self, event):
        window = self.GetActiveChild()
        if window is None:
            return
        window.undo_do_redo()
    
            
    def edit_copy(self, event):
        window = self.GetActiveChild()
        if window is None:
            return
        window.edit_copy()
        
        
    def edit_paste(self, event):
        window = self.GetActiveChild()
        if window is None:
            return
        window.edit_paste()
        
        
    def view_patch_settings(self, event):
        self.patch_info.set_state(self.patch, self.engines, self.workspace, modify_engine=False)
        self.patch_info.ShowModal()
        
        if self.patch_info.selected_engine is not None:
            self.workspace.iwad = self.patch_info.selected_iwad
            self.workspace.pwads = self.patch_info.selected_pwads
            self.load_wads()
            
            self.set_modified(True)
            self.workspace_modified = True
            self.tool_windows[windows.MAIN_TOOL_STATES].tools_update()
    
    
    def file_open(self, event):
        self.open_file_dialog()
        
        
    def file_open_as(self, event):
        self.open_file_dialog(force_show_settings=True)
        
        
    def file_open_recent(self, event):
        event_id = event.GetId()
        item = self.FindItemInMenuBar(event_id)
        filename = item.GetItemLabel()
        
        self.open_file(filename)
        
        
    def open_file_dialog(self, force_show_settings=False):
        if self.save_if_needed() == False:
            return
        
        filename = wx.FileSelector('Choose a Dehacked file to open.',
            wildcard='All supported files|*.deh;*.bex|Dehacked files (*.deh)|*.deh|Extended Dehacked files (*.bex)|*.bex|All files|*.*',
            flags=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        
        if filename != '':
            self.open_file(filename, force_show_settings)
            
    
    def open_file(self, filename, force_show_settings=False):
        # Load a workspace file if it exists.
        workspace_file = workspace.get_filename(filename)
        new_workspace = workspace.Workspace()
        if os.path.exists(workspace_file):
            new_workspace.load(workspace_file)
        
        # Analyze the patch file to determine what engines support it.
        new_patch = patch.Patch()
        new_patch.analyze_patch(filename, self.engines)
        
        # Display the patch info dialog to let the user select patch settings.
        # Do not show the info dialog if a workspace was found, unless forced.
        patch_info = patchinfodialog.PatchInfoDialog(self)
        patch_info.set_state(new_patch, self.engines, new_workspace)
        if new_workspace.engine is None or force_show_settings == True:
            patch_info.ShowModal()
            
            if patch_info.selected_engine is None:
                return
            
            new_workspace.iwad = patch_info.selected_iwad
            new_workspace.pwads = patch_info.selected_pwads
            new_workspace.engine = patch_info.selected_engine
            new_workspace.save(workspace_file)
            
        engine = self.engines[new_workspace.engine]
        new_patch.initialize_from_engine(engine)

        # Attempt to load the patch file.
        try:
            messages = new_patch.read_dehacked(filename)
        except patch.DehackedVersionError as e:
            wx.MessageBox(message=e.__str__(),
                caption='Patch version error',
                style=wx.OK | wx.ICON_ERROR,
                parent=self)
            return
        except patch.DehackedPatchError as e:
            wx.MessageBox(message=e.__str__(),
                caption='Patch error',
                style=wx.OK | wx.ICON_ERROR,
                parent=self)
            return
        
        # Display any messages from the patch load process.
        for message in messages.itervalues():
            wx.MessageBox(message=message,
                caption='Patch message',
                style=wx.OK | wx.ICON_EXCLAMATION,
                parent=self)

        # Store new patch info.
        self.patch = new_patch
        self.patch_modified = False
        self.patch_info = patch_info
        self.workspace = new_workspace
        
        # Load WAD files for this new patch.
        self.load_wads()
        
        # Refresh UI contents and state.
        self.init_ui()

        # Store potentially updated workspace.
        self.save_workspace()
        
        # Add item to recent files.
        config.settings.recent_files_add(filename)
        self.update_recent_files()
        
        
    def load_wads(self):
        self.iwad = None
        self.pwads.clear()

        if self.workspace.iwad is None:
            return
        
        if os.path.exists(self.workspace.iwad) == False:
            wx.MessageBox(message='The IWAD {} could not be found. Sprite previews will be disabled.'.format(self.workspace.iwad),
                caption='Missing IWAD',
                style=wx.OK | wx.ICON_INFORMATION,
                parent=self)
            self.workspace.iwad = None
            self.patch_modified = True
            return
        
        wx.BeginBusyCursor()
        self.iwad = wad.WADReader(self.workspace.iwad)
        
        # Create the WAD list.
        self.pwads.clear()
        self.pwads.add_wad(self.iwad)
        for pwad_file in self.workspace.pwads:
            if os.path.exists(pwad_file) == False:
                wx.MessageBox(message='The PWAD {} could not be found.'.format(pwad_file),
                    caption='Missing PWAD',
                    style=wx.OK | wx.ICON_EXCLAMATION,
                    parent=self)
                self.workspace.pwads.remove(pwad_file)
                self.patch_modified = True
            else:
                pwad = wad.WADReader(pwad_file)
                self.pwads.add_wad(pwad)
        
        # Generate sprite list.
        self.pwads.build_sprite_list()
        if self.pwads.palette is None:
            wx.MessageBox(message='No PLAYPAL lump could be found in any of the loaded WAD files. Sprite previews will be disabled.',
                caption='Missing PLAYPAL',
                style=wx.OK | wx.ICON_INFORMATION,
                parent=self)
            self.workspace.iwad = None
        
        wx.EndBusyCursor()
        
        
    def file_save(self, event):
        if self.patch.filename is None:
            self.save_file_dialog()
        else:
            self.save_file(self.patch.filename)
            
            
    def file_save_as(self, event):
        self.save_file_dialog()
            
            
    def save_file_dialog(self):
        if self.patch.filename is not None:
            use_filename = self.patch.filename
            default_ext = os.path.splitext(self.patch.filename)[1]
        else:
            if self.patch.extended == True:
                use_filename = 'unnamed.bex'
                default_ext = 'bex'
            else:
                use_filename = 'unnamed.deh'
                default_ext = 'deh'
        
        filename = wx.FileSelector('Save Dehacked file.', default_filename=use_filename, default_extension=default_ext,
            wildcard='All supported files|*.deh;*.bex|Dehacked files (*.deh)|*.deh|Extended Dehacked files (*.bex)|*.bex|All files|*.*',
            flags=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        
        if filename != '':
            self.save_file(filename)
        
        
    def save_file(self, filename):
        wx.BeginBusyCursor()
        
        filename = os.path.abspath(filename)
        
        # Create a backup of the existing file.
        if os.path.exists(filename):
            shutil.copyfile(filename, filename + '.bak')
        
        # Write patch.
        self.patch.write_dehacked(filename)
        
        # Store workspace info.
        self.save_workspace()

        self.patch.filename = filename
        self.set_modified(False)
        
        config.settings.recent_files_add(filename)
        self.update_recent_files()
        
        wx.EndBusyCursor()
        
        
    def save_workspace(self):
        if self.workspace is None or self.patch.filename is None:
            return
        
        workspace_file = workspace.get_filename(self.patch.filename)
        self.workspace.store_windows(self, self.workspace_windows)
        self.workspace.save(workspace_file)
        self.workspace_modified = False
        
        
    def update_recent_files(self):
        while(self.MenuFileRecent.GetMenuItemCount() > 0):
            item = self.MenuFileRecent.FindItemByPosition(0)
            self.MenuFileRecent.DestroyItem(item)
            
        recent_files = config.settings['recent_files']
        for recent_file in recent_files:
            item = self.MenuFileRecent.Append(wx.ID_ANY, recent_file, '', wx.ITEM_NORMAL)
            self.Bind(wx.EVT_MENU, self.file_open_recent, id=item.GetId())
        
    
    def init_ui(self):
        wx.BeginBusyCursor()
        
        self.set_toolbar_enabled(True, self.patch.engine.extended)
        self.build_editors()
        
        if self.workspace.windows is None:
            self.workspace.store_windows(self, self.workspace_windows)
        else:
            self.workspace.apply_windows(self, self.workspace_windows)
            
        self.update_toolbar_state()
        self.set_modified(self.patch_modified)
        
        wx.EndBusyCursor()
        
    
    def set_modified(self, is_modified):
        self.patch_modified = is_modified
        self.update_label()
    
    
    def update_label(self):
        label = config.APP_NAME + ' - '
        if self.patch.filename is not None:
            label += self.patch.filename
        else:
            label += 'New file'

        if self.patch_modified == True:
            label += ' *' 
            
        self.SetLabel(label)
    
    
    def file_new(self, event):
        self.new_file()
        
        
    def new_file(self):
        new_workspace = workspace.Workspace()
        
        new_patch = patch.Patch()
        new_patch.filename = None
                
        patch_info = patchinfodialog.PatchInfoDialog(self)
        patch_info.set_state(new_patch, self.engines, new_workspace)
        patch_info.ShowModal()
        
        if patch_info.selected_engine is None:
            return
        
        new_workspace.iwad = patch_info.selected_iwad
        new_workspace.pwads = patch_info.selected_pwads
        new_workspace.engine = patch_info.selected_engine
        
        engine = self.engines[patch_info.selected_engine]
        new_patch.version = max(engine.versions)
        new_patch.extended = engine.extended
        new_patch.initialize_from_engine(engine)
        
        # Store new patch info.        
        self.patch = new_patch
        self.patch_info = patch_info
        self.workspace = new_workspace
        self.set_modified(False)
        
        # Initialize the UI.
        self.load_wads()
        self.init_ui()
    
    
    def build_editors(self):
        for window in self.tool_windows.itervalues():
            window.build(self.patch)
            
            
    def save_if_needed(self):
        if self.patch_modified == True:
            result = wx.MessageBox(message='The file has been modified. Save changes?',
                caption='Save file',
                style=wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION,
                parent=self)
            
            if result == wx.YES:
                self.save_file(self.patch.filename)
            elif result == wx.CANCEL:
                return False
        
        return True
    
    
    def close(self, event):
        if self.save_if_needed() == False:
            return
        
        if self.workspace_modified == True:
            self.save_workspace()
        
        # Write program settings.
        config.settings.save()
        
        self.DestroyChildren()
        self.Destroy()
        
        
    def tool_windows_hide(self):
        for window in self.tool_windows.itervalues():
            window.Show(False)
            
            
    def tool_windows_get_id_from_instance(self, window):
        for window_id, tool_window in self.tool_windows.iteritems():
            if window == tool_window:
                return window_id
            
        return 0
        
        
    def tool_window_show(self, tool_id):
        window = self.tool_windows[tool_id]
        window.Maximize(False)
        window.Show(True)
        
        self.MainToolbar.ToggleTool(tool_id, True)
        self.workspace_modified = True
    
    
    def set_menu_state(self, event):
        event_id = event.GetId()
        tool_id = self.menu_windows[event_id]
        window = self.tool_windows[tool_id]
                
        if window is not None:
            state = self.MainToolbar.GetToolState(tool_id)
            window.Maximize(False)
            window.Show(state)
            self.MainToolbar.ToggleTool(tool_id, state)
            self.workspace_modified = True
    
     
    def set_toolbar_state(self, event):
        window = self.tool_windows[event.GetId()]
                
        if window is not None:
            state = self.MainToolbar.GetToolState(event.GetId())
            window.Maximize(False)
            window.Show(state)
            
            self.workspace_modified = True
                
                
    def update_toolbar_state(self):
        for tool_id, window in self.tool_windows.iteritems():
            self.MainToolbar.ToggleTool(tool_id, window.IsShown())
    
                    
    def window_closed(self, window):
        tool_id = self.tool_windows_get_id_from_instance(window)

        if tool_id != 0:
            self.MainToolbar.ToggleTool(tool_id, False)
            window.Show(False)
            self.workspace_modified = True
            
    
    def help_about(self, event):
        self.about_dialog.ShowModal()
        
        
    def update_window_data(self, event):
        # Only update size and position if the window is not maximized.
        if self.IsMaximized() == True or self.IsShown() == False:
            main_window_state = config.settings['main_window_state']
            
            pos = (main_window_state['x'], main_window_state['y'])
            size = (main_window_state['width'], main_window_state['height'])
        else:
            pos = self.GetPositionTuple()
            size = self.GetSizeTuple()

        config.settings.main_window_state_store(pos[0], pos[1], size[0], size[1], self.IsMaximized())
        
        event.Skip()