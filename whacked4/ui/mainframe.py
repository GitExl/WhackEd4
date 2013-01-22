#!/usr/bin/env python
#coding=utf8

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
    """
    The main MDI parent window.
    """

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
        self.editor_windows = {
            windows.MAIN_TOOL_THINGS: thingframe.ThingFrame(self),
            windows.MAIN_TOOL_STATES: statesframe.StatesFrame(self) 
        }
        self.menu_windows = {
            windows.MAIN_MENU_THINGS: windows.MAIN_TOOL_THINGS,
            windows.MAIN_MENU_STATES: windows.MAIN_TOOL_STATES,
        }
        self.workspace_windows = {
            'things': self.editor_windows[windows.MAIN_TOOL_THINGS],
            'states': self.editor_windows[windows.MAIN_TOOL_STATES]
        }
        
        # Reset editor window states.
        self.editor_windows_show(False)
        self.toolbar_set_enabled(False)
        
        # Dialogs.
        self.start_dialog = startdialog.StartDialog(self)
        self.about_dialog = aboutdialog.AboutDialog(self)
        
        self.Show()

        self.update_recent_files_menu()        
        config.settings.main_window_state_restore(self)
        
        wx.EndBusyCursor()
        
        self.parse_options(arguments)
        
        # Late bind these to prevent bad workspace data from being saved.
        self.Bind(wx.EVT_MOVE, self.workspace_update_data)
        self.Bind(wx.EVT_SIZE, self.workspace_update_data)
    
    
    def parse_options(self, args):
        """
        Parses commandline options and acts on them.
        """
        
        for arg in sys.argv[1:]:
            if os.path.exists(arg):
                self.open_file(arg)
                return
                
        self.start_dialog.ShowModal()
    
        
    def load_engines(self):
        """
        Loads all engine configuration files. These are kept in memory for patch compatibility auto-detection.
        """
        
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
                    
        
    def view_patch_settings(self, event):
        """
        Displays the patch settings dialog.
        """
        
        self.patch_info.set_state(self.patch, self.engines, self.workspace, modify_engine=False)
        self.patch_info.ShowModal()
        
        # Alter workspace settings if the user clicked Ok.
        if self.patch_info.selected_engine is not None:
            self.workspace.iwad = self.patch_info.selected_iwad
            self.workspace.pwads = self.patch_info.selected_pwads
            self.load_wads()
            
            self.set_modified(True)
            self.workspace_modified = True
            
            self.editor_windows[windows.MAIN_TOOL_STATES].tools_update()
    
    
    def open_file_dialog(self, force_show_settings=False):
        """
        Displays an open file dialog to open a patch file.
        """
        
        if self.save_if_needed() == False:
            return
        
        filename = wx.FileSelector('Choose a Dehacked file to open.',
            wildcard='All supported files|*.deh;*.bex|Dehacked files (*.deh)|*.deh|Extended Dehacked files (*.bex)|*.bex|All files|*.*',
            flags=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        
        if filename != '':
            self.open_file(filename, force_show_settings)
            
    
    def open_file(self, filename, force_show_settings=False):
        """
        Opens and reads a new Dehacked patch.
        
        @param filename: the filename of the file to open.
        @param force_show_settings: if True, will always display the patch settings dialog.  
        """
        
        # Load the accompanying workspace file if it exists.
        new_workspace = workspace.Workspace()
        workspace_file = new_workspace.get_filename(filename)
        if os.path.exists(workspace_file):
            new_workspace.load(filename)
        
        # Analyze the patch file to determine what engines support it.
        new_patch = patch.Patch()
        new_patch.analyze_patch(filename, self.engines)
        
        # Display the patch info dialog to let the user select patch settings.
        # Do not show the info dialog if a workspace was found, unless forced.
        patch_info = patchinfodialog.PatchInfoDialog(self)
        patch_info.set_state(new_patch, self.engines, new_workspace)
        if new_workspace.engine is None or force_show_settings == True:
            patch_info.ShowModal()
            
            # User cancelled out of the patch info dialog.
            if patch_info.selected_engine is None:
                return
            
            # Store patch info in the new workspace.
            new_workspace.iwad = patch_info.selected_iwad
            new_workspace.pwads = patch_info.selected_pwads
            new_workspace.engine = patch_info.selected_engine
            new_workspace.save(workspace_file)
            
        # Initialize the patch with tables from the selected engine.
        engine = self.engines[new_workspace.engine]
        new_patch.initialize_from_engine(engine)

        # Attempt to parse the patch file.
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
        
        # Refresh user interface contents.
        self.load_wads()
        self.update_ui()

        # Store potentially updated workspace.
        self.workspace_save()
        
        # Add item to recent files.
        config.settings.recent_files_add(filename)
        self.update_recent_files_menu()
        
        
    def load_wads(self):
        """
        Loads the WAD files that are selected in the current workspace.
        """
        
        self.iwad = None
        self.pwads.clear()
        
        if self.workspace.iwad is None:
            return
        
        # Verify if the IWAD file exists at all.
        if os.path.exists(self.workspace.iwad) == False:
            wx.MessageBox(message='The IWAD {} could not be found. Sprite previews will be disabled.'.format(self.workspace.iwad),
                caption='Missing IWAD',
                style=wx.OK | wx.ICON_INFORMATION,
                parent=self)
            self.workspace.iwad = None
            self.patch_modified = True
            return
        
        wx.BeginBusyCursor()
        
        # Load and add the IWAD to the WAD list.
        self.iwad = wad.WADReader(self.workspace.iwad)
        self.pwads.add_wad(self.iwad)
        
        # Load PWADs.
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
        
        # Build the sprite lookup tables.
        self.pwads.build_sprite_list()
        if self.pwads.palette is None:
            wx.MessageBox(message='No PLAYPAL lump could be found in any of the loaded WAD files. Sprite previews will be disabled.',
                caption='Missing PLAYPAL',
                style=wx.OK | wx.ICON_INFORMATION,
                parent=self)
            self.workspace.iwad = None
        
        wx.EndBusyCursor()
        
        
    def save_file_dialog(self):
        """
        Displays a save file dialog to save the current patch file.
        """
        
        # Use the patch filename if it was saved before.
        if self.patch.filename is not None:
            use_filename = self.patch.filename
            default_ext = os.path.splitext(self.patch.filename)[1]
        
        # Otherwise use a default filename and extension.
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
        """
        Saves a Dehacked patch file.
        """
        
        wx.BeginBusyCursor()
        
        # Create a backup of the existing file.
        if os.path.exists(filename):
            shutil.copyfile(filename, filename + '.bak')
        
        # Write patch.
        self.patch.write_dehacked(filename)
        self.patch.filename = filename
        self.set_modified(False)
        
        # Store workspace info.
        self.workspace_save()

        # Add to recent files.        
        config.settings.recent_files_add(filename)
        self.update_recent_files_menu()
        
        wx.EndBusyCursor()
        
        
    def update_recent_files_menu(self):
        """
        Updates the recent files submenu.
        """
        
        # Remove the old items.
        while(self.MenuFileRecent.GetMenuItemCount() > 0):
            item = self.MenuFileRecent.FindItemByPosition(0)
            self.MenuFileRecent.DestroyItem(item)
        
        # Add all recent files again.
        recent_files = config.settings['recent_files']
        for recent_file in recent_files:
            item = self.MenuFileRecent.Append(wx.ID_ANY, recent_file, '', wx.ITEM_NORMAL)
            self.Bind(wx.EVT_MENU, self.file_open_recent, id=item.GetId())
        
    
    def update_ui(self):
        """
        Updates the user interface contents of this main window and all available editor windows.
        """
        
        wx.BeginBusyCursor()
        
        # Update editor window contents.
        for window in self.editor_windows.itervalues():
            window.build(self.patch)
        
        # Store new workspace window data, or apply existing data.
        if self.workspace.windows is None:
            self.workspace.store_windows(self, self.workspace_windows)
        else:
            self.workspace.restore_windows(self.workspace_windows)

        self.toolbar_set_enabled(True)            
        self.toolbar_update_state()
        
        self.set_modified(self.patch_modified)
        
        wx.EndBusyCursor()
        
    
    def set_modified(self, is_modified):
        """
        Used to mark the current patch as modified.
        
        Upon attempting to exit, the user will be asked to save the patch before doing so, if it has been modified.
        """
        
        self.patch_modified = is_modified
        self.update_label()
    
    
    def update_label(self):
        """
        Updates this window's label (titlebar text).
        """
        
        label = config.APP_NAME + ' - '
        if self.patch.filename is not None:
            label += self.patch.filename
        else:
            label += 'New file'

        if self.patch_modified == True:
            label += ' *' 
            
        self.SetLabel(label)
    
    
    def new_file(self):
        """
        Creates a new Dehacked patch file.
        """
        
        new_workspace = workspace.Workspace()
        
        new_patch = patch.Patch()
        new_patch.filename = None
        
        # Ask the user to provide patch details.
        patch_info = patchinfodialog.PatchInfoDialog(self)
        patch_info.set_state(new_patch, self.engines, new_workspace)
        patch_info.ShowModal()
        
        if patch_info.selected_engine is None:
            return
        
        # Store patch details in the new workspace.
        new_workspace.iwad = patch_info.selected_iwad
        new_workspace.pwads = patch_info.selected_pwads
        new_workspace.engine = patch_info.selected_engine
        
        # Initialize patch table data.
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
        self.editor_windows_show(False)
        self.update_ui()
            
            
    def save_if_needed(self):
        """
        Requests the user to save the current patch file if it has been modified.
        """
        
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
        """
        Called when this window is being closed.
        """
        
        if self.save_if_needed() == False:
            return
        
        if self.workspace_modified == True:
            self.workspace_save()
        
        config.settings.save()
        
        self.DestroyChildren()
        self.Destroy()
                    
            
    def editor_window_toolid_for_instance(self, window):
        """
        Returns a toolbar tool id for an editor window instance.
        
        @return: a toolbar id if the window instance was found, wx.NOT_FOUND if none was found.
        """
        
        for tool_id, editor_window in self.editor_windows.iteritems():
            if window == editor_window:
                return tool_id
            
        return wx.NOT_FOUND
        
        
    def editor_window_show(self, tool_id):
        """
        Shows an editor window.
        
        @param tool_id: the toolbar id of the window to show.
        """ 
        
        window = self.editor_windows[tool_id]
        window.Maximize(False)
        window.Show(True)
        
        self.MainToolbar.ToggleTool(tool_id, True)
        self.workspace_modified = True
    
    
    def editor_window_menutoggle(self, event):
        """
        Toggles the visibility of an editor window from a menu item.
        """

        tool_id = self.menu_windows[event.GetId()]
        window = self.editor_windows[tool_id]       
        if window is not None:
            state = not self.MainToolbar.GetToolState(tool_id)
            window.Maximize(False)
            window.Show(state)
            
            self.MainToolbar.ToggleTool(tool_id, state)
            self.workspace_modified = True
    
     
    def editor_window_tooltoggle(self, event):
        """
        Toggles the visibility of an editor window from a toolbar item.
        """
        
        window = self.editor_windows[event.GetId()]
        if window is not None:
            state = self.MainToolbar.GetToolState(event.GetId())
            window.Maximize(False)
            window.Show(state)
            
            self.workspace_modified = True
            
            
    def editor_windows_show(self, show):
        """
        Sets the visibility of all editor windows at once.
        """
        
        for window in self.editor_windows.itervalues():
            window.Show(show)
            
    
    def editor_window_closed(self, window):
        tool_id = self.editor_window_toolid_for_instance(window)
        if tool_id == wx.NOT_FOUND:
            return
            
        self.MainToolbar.ToggleTool(tool_id, False)
        window.Show(False)
        self.workspace_modified = True


    def toolbar_set_enabled(self, enabled):
        """
        Sets the toolbar button and menu item enabled states.
        """
        
        # Set toolbar states.
        for tool_id in self.editor_windows.iterkeys():
            self.ToolBar.EnableTool(tool_id, enabled)
        
        # TODO: Remove when all editors are implemented.
        self.ToolBar.EnableTool(windows.MAIN_TOOL_AMMO, False)
        self.ToolBar.EnableTool(windows.MAIN_TOOL_CHEATS, False)
        self.ToolBar.EnableTool(windows.MAIN_TOOL_STRINGS, False)
        self.ToolBar.EnableTool(windows.MAIN_TOOL_WEAPONS, False)
        self.ToolBar.EnableTool(windows.MAIN_TOOL_SOUNDS, False)
        self.ToolBar.EnableTool(windows.MAIN_TOOL_MISC, False)
        
        # Set menu states.
        self.MenuViewThings.Enable(enabled)
        self.MenuViewStates.Enable(enabled)
        self.MenuViewAmmo.Enable(False)
        self.MenuViewCheats.Enable(False)
        self.MenuViewStrings.Enable(False)
        self.MenuViewWeapons.Enable(False)
        self.MenuViewSounds.Enable(False)
        self.MenuViewMiscellaneous.Enable(False)
        self.MenuViewPatchSettings.Enable(enabled)
        
        if self.patch is not None and self.patch.extended == True:
            self.ToolBar.EnableTool(windows.MAIN_TOOL_PAR, False)
            self.MenuViewPar.Enable(False)
        else:
            self.ToolBar.EnableTool(windows.MAIN_TOOL_PAR, False)
            self.MenuViewPar.Enable(False)
                
                
    def toolbar_update_state(self):
        """
        Updates the toolbar button's state to reflect whether they are shown or not.
        """
        
        for tool_id, window in self.editor_windows.iteritems():
            self.MainToolbar.ToggleTool(tool_id, window.IsShown())
    
    
    def workspace_save(self):
        """
        Stores window positions and saves the current workspace.
        """
        
        if self.workspace is None or self.patch.filename is None:
            return
        
        self.workspace.store_windows(self, self.workspace_windows)
        self.workspace.save(self.patch.filename)
        self.workspace_modified = False
    
        
    def workspace_update_data(self, event):
        """
        Update the current workspace with this window's size, position and state.
        """
        
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
    
    
    def file_new(self, event):
        self.new_file()
    
    def file_save(self, event):
        if self.patch.filename is None:
            self.save_file_dialog()
        else:
            self.save_file(self.patch.filename)
            
    def file_save_as(self, event):
        self.save_file_dialog()
        
    def file_open(self, event):
        self.open_file_dialog()
        
    def file_open_as(self, event):
        self.open_file_dialog(force_show_settings=True)
        
    def file_open_recent(self, event):
        item = self.FindItemInMenuBar(event.GetId())
        filename = item.GetItemLabel()
        self.open_file(filename)
        
    
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
        
    
    def help_about(self, event):
        self.about_dialog.ShowModal()