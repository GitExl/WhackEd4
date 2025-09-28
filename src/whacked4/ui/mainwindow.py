"""
Main UI frame.
"""

from collections import OrderedDict
import glob
import os.path
import shutil
import webbrowser
import sys
from typing import Optional, Dict

import wx
from wx import Frame, MDIChildFrame, MenuEvent, CloseEvent, CommandEvent, Event

from whacked4 import config, utils
from whacked4.dehacked import engine, patch
from whacked4.dehacked.engine import Engine
from whacked4.dehacked.patch import Patch
from whacked4.doom import wadlist
from whacked4.doom.wad import WAD
from whacked4.doom.wadlist import WADList
from whacked4.ui import windows, workspace
from whacked4.ui.dialogs import startdialog, aboutdialog, patchinfodialog
from whacked4.ui.dialogs.aboutdialog import AboutDialog
from whacked4.ui.dialogs.patchinfodialog import PatchInfoDialog
from whacked4.ui.dialogs.startdialog import StartDialog
from whacked4.ui.editors import thingsframe, statesframe, soundsframe, stringsframe, \
    weaponsframe, ammoframe, cheatsframe, miscframe, parframe
from whacked4.ui.workspace import Workspace


class MainWindow(windows.MainFrameBase):
    """
    The main MDI parent window.
    """

    def __init__(self, parent):
        windows.MainFrameBase.__init__(self, parent)
        self._adjust_mac_ui()

        wx.BeginBusyCursor()

        self.SetIcon(wx.Icon('res/icon-hatchet.ico'))

        # Patch-related data.
        self.patch: Optional[Patch] = None
        self.patch_info: Optional[PatchInfoDialog] = None
        self.patch_modified: bool = False

        # Workspace info.
        self.workspace: Optional[Workspace] = None
        self.workspace_modified: bool = False

        # WAD\lump management.
        self.iwad: Optional[WAD] = None
        self.pwads: WADList = wadlist.WADList()

        # Engine configuration related data.
        self.engines: Dict[str, Engine] = OrderedDict()
        self.load_engines()

        # Window\ID relationships.
        self.editor_windows: Dict[int, MDIChildFrame] = {
            windows.MAIN_TOOL_THINGS: thingsframe.ThingsFrame(self),
            windows.MAIN_TOOL_STATES: statesframe.StatesFrame(self),
            windows.MAIN_TOOL_SOUNDS: soundsframe.SoundsFrame(self),
            windows.MAIN_TOOL_STRINGS: stringsframe.StringsFrame(self),
            windows.MAIN_TOOL_WEAPONS: weaponsframe.WeaponsFrame(self),
            windows.MAIN_TOOL_AMMO: ammoframe.AmmoFrame(self),
            windows.MAIN_TOOL_CHEATS: cheatsframe.CheatsFrame(self),
            windows.MAIN_TOOL_MISC: miscframe.MiscFrame(self),
            windows.MAIN_TOOL_PAR: parframe.ParFrame(self)
        }
        self.menu_windows: Dict[int, int] = {
            windows.MAIN_MENU_THINGS: windows.MAIN_TOOL_THINGS,
            windows.MAIN_MENU_STATES: windows.MAIN_TOOL_STATES,
            windows.MAIN_MENU_SOUNDS: windows.MAIN_TOOL_SOUNDS,
            windows.MAIN_MENU_STRINGS: windows.MAIN_TOOL_STRINGS,
            windows.MAIN_MENU_WEAPONS: windows.MAIN_TOOL_WEAPONS,
            windows.MAIN_MENU_AMMO: windows.MAIN_TOOL_AMMO,
            windows.MAIN_MENU_CHEATS: windows.MAIN_TOOL_CHEATS,
            windows.MAIN_MENU_MISC: windows.MAIN_TOOL_MISC,
            windows.MAIN_MENU_PAR: windows.MAIN_TOOL_PAR
        }
        self.workspace_windows: Dict[str, Frame] = {
            'things': self.editor_windows[windows.MAIN_TOOL_THINGS],
            'states': self.editor_windows[windows.MAIN_TOOL_STATES],
            'sounds': self.editor_windows[windows.MAIN_TOOL_SOUNDS],
            'strings': self.editor_windows[windows.MAIN_TOOL_STRINGS],
            'weapons': self.editor_windows[windows.MAIN_TOOL_WEAPONS],
            'ammo': self.editor_windows[windows.MAIN_TOOL_AMMO],
            'cheats': self.editor_windows[windows.MAIN_TOOL_CHEATS],
            'misc': self.editor_windows[windows.MAIN_TOOL_MISC],
            'par': self.editor_windows[windows.MAIN_TOOL_PAR]
        }

        # Reset editor window states.
        self.editor_windows_show(False)
        self.toolbar_set_enabled(False)

        self.Show()

        # Dialogs.
        self.start_dialog: StartDialog = startdialog.StartDialog(self)
        self.about_dialog: AboutDialog = aboutdialog.AboutDialog(self)

        self.update_recent_files_menu()
        config.settings.main_window_state_restore(self)

        wx.EndBusyCursor()

        # Late bind these to prevent bad workspace data from being saved.
        self.Bind(wx.EVT_MOVE, self.workspace_update_data)
        self.Bind(wx.EVT_SIZE, self.workspace_update_data)

        self.editor_window_set_edit()
        self.file_set_state()

    def show_start(self):
        """
        Displays starting dialog.
        """

        self.start_dialog.ShowModal()

    def load_engines(self):
        """
        Loads all engine configuration files. These are kept in memory for patch
        compatibility auto-detection.
        """

        for file_name in sorted(glob.glob('cfg/tables_*.json')):
            new_engine = engine.Engine()
            try:
                new_engine.merge_data(file_name)
                new_engine.apply_defaults()
            except engine.DehackedEngineError as e:
                wx.MessageBox(
                    message=f'Invalid engine configuration file "{file_name}". Exception: {e}',
                    caption='Engine configuration error',
                    style=wx.OK | wx.ICON_EXCLAMATION,
                    parent=self
                )
            else:
                name = os.path.basename(file_name)
                name = os.path.splitext(name)[0]
                self.engines[name] = new_engine

    def view_patch_settings(self, event):
        """
        Displays the patch settings dialog.
        """

        self.patch_info.set_state(
            self.patch.filename,
            self.patch.version,
            self.patch.extended,
            self.engines,
            self.workspace,
            modify_engine=False
        )
        self.patch_info.ShowModal()

        # Alter workspace settings if the user clicked Ok.
        if self.patch_info.selected_engine is not None:
            self.workspace.iwad = self.patch_info.selected_iwad
            self.workspace.pwads = self.patch_info.selected_pwads
            self.load_wads()

            self.set_modified(True)
            self.workspace_modified = True

            self.editor_windows[windows.MAIN_TOOL_STATES].update_properties()

    def open_file_dialog(self, force_show_settings: bool = False):
        """
        Displays an open file dialog to open a patch file.
        """

        if not self.save_if_needed():
            return

        filename = utils.file_dialog(
            self,
            message='Choose a Dehacked file to open',
            wildcard='All supported files|*.deh;*.bex|Dehacked files (*.deh)|*.deh|'
                     'Extended Dehacked files (*.bex)|*.bex|All files|*.*',
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        )

        if filename is not None:
            self.open_file(filename, force_show_settings)

    def open_file_merge_dialog(self):
        """
        Displays an open file dialog to open a patch file.
        """

        result = wx.MessageBox(
            message='Merging a patch cannot be undone, so make sure you have saved this file '
                    'before attempting a merge. Canceling a merge will not restore this patch to '
                    'its original state.\n\nDo you want to continue?',
            caption='Merge patch',
            style=wx.YES_NO | wx.ICON_EXCLAMATION,
            parent=self
        )
        if result == wx.NO:
            return

        filename = utils.file_dialog(
            self,
            message='Choose a Dehacked file to merge',
            wildcard='All supported files|*.deh;*.bex|Dehacked files (*.deh)|*.deh|'
                     'Extended Dehacked files (*.bex)|*.bex|All files|*.*',
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        )

        if filename is not None:
            self.merge_file(filename)

    def open_file(self, filename: str, force_show_settings: bool = False):
        """
        Opens and reads a new Dehacked patch.

        @param filename: the filename of the file to open.
        @param force_show_settings: if True, will always display the patch
        settings dialog.
        """

        # Load the accompanying workspace file if it exists.
        new_workspace = workspace.Workspace()
        workspace_file = workspace.get_filename(filename)
        if os.path.exists(workspace_file):
            new_workspace.load(filename)

        # Analyze the patch file to determine what engines support it.

        try:
            version, is_extended = Patch.analyze(filename, self.engines)
        except patch.DehackedPatchError as e:
            wx.MessageBox(
                message=str(e),
                caption='Patch error',
                style=wx.OK | wx.ICON_ERROR,
                parent=self
            )
            return

        # Display the patch info dialog to let the user select patch settings.
        # Do not show the info dialog if a workspace was found, unless forced.
        patch_info = patchinfodialog.PatchInfoDialog(self)
        patch_info.set_state(filename, version, is_extended, self.engines, new_workspace)
        if new_workspace.engine is None or force_show_settings:
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
        selected_engine = self.engines[new_workspace.engine]
        new_patch = Patch(selected_engine)
        new_patch.filename = filename
        new_patch.extended = is_extended
        new_patch.version = version

        # Attempt to parse the patch file.
        try:
            messages = new_patch.read_dehacked(filename)
        except patch.DehackedVersionError as e:
            wx.MessageBox(
                message=str(e),
                caption='Patch version error',
                style=wx.OK | wx.ICON_ERROR,
                parent=self
            )
            return
        except patch.DehackedPatchError as e:
            wx.MessageBox(
                message=str(e),
                caption='Patch error',
                style=wx.OK | wx.ICON_ERROR,
                parent=self
            )
            return

        # Display any messages from the patch load process.
        for message in messages.values():
            message += '\n\nPress Yes to continue loading, No to stop displaying messages or ' \
                       'Cancel to abort loading this patch.'
            result = wx.MessageBox(
                message=message,
                caption='Patch message',
                style=wx.YES_NO | wx.CANCEL | wx.ICON_EXCLAMATION,
                parent=self
            )
            if result == wx.NO:
                break
            if result == wx.CANCEL:
                return

        # Store new patch info.
        self.patch = new_patch
        self.patch_modified = False
        self.patch_info = patch_info
        self.workspace = new_workspace

        # Refresh user interface contents.
        self.load_wads()
        self.update_ui()
        self.file_set_state()

        # Store potentially updated workspace.
        self.workspace_save()

        # Add item to recent files.
        config.settings.recent_files_add(filename)
        self.update_recent_files_menu()

    def merge_file(self, filename: str):
        """
        Opens and reads a new Dehacked patch then merges it into the current patch.

        @param filename: the filename of the file to open.
        """

        # Analyze the patch file to determine what engines support it.
        try:
            version, is_extended = Patch.analyze(filename, self.engines)
        except patch.DehackedPatchError as e:
            wx.MessageBox(
                message=str(e),
                caption='Patch error',
                style=wx.OK | wx.ICON_ERROR,
                parent=self
            )
            return

        # Check for compatibility.
        if version != self.patch.version or is_extended != self.patch.extended:
            wx.MessageBox(
                message='The patch is not compatible with the currently loaded patch. Check '
                        'the patch version and any extended features.',
                caption='Patch not compatible',
                style=wx.OK | wx.ICON_ERROR,
                parent=self
            )
            return

        # Attempt to parse the patch file.
        try:
            messages = self.patch.read_dehacked(filename)
        except patch.DehackedVersionError as e:
            wx.MessageBox(
                message=str(e),
                caption='Patch version error',
                style=wx.OK | wx.ICON_ERROR,
                parent=self
            )
            return
        except patch.DehackedPatchError as e:
            wx.MessageBox(
                message=str(e),
                caption='Patch error',
                style=wx.OK | wx.ICON_ERROR,
                parent=self
            )
            return

        # Display any messages from the patch load process.
        for message in messages.values():
            message += '\n\nPress Yes to continue loading, No to stop displaying messages ' \
                       'or Cancel to abort loading this patch.'
            result = wx.MessageBox(
                message=message,
                caption='Patch message',
                style=wx.YES_NO | wx.CANCEL | wx.ICON_EXCLAMATION,
                parent=self
            )
            if result == wx.NO:
                break
            if result == wx.CANCEL:
                return

        # Store new patch info.
        self.patch_modified = True

        # Refresh user interface contents.
        self.load_wads()
        self.update_ui()
        self.file_set_state()

    def load_wads(self):
        """
        Loads the WAD files that are selected in the current workspace.
        """

        self.iwad = None
        self.pwads.clear()

        if self.workspace.iwad is None:
            return

        # Verify if the IWAD file exists at all.
        if not os.path.exists(self.workspace.iwad):
            wx.MessageBox(
                message=f'The IWAD {self.workspace.iwad} could not be found. Sprite previews '
                        ' will be disabled.',
                caption='Missing IWAD',
                style=wx.OK | wx.ICON_INFORMATION,
                parent=self
            )
            self.workspace.iwad = None
            self.patch_modified = True
            return

        wx.BeginBusyCursor()

        # Load and add the IWAD to the WAD list.
        self.iwad = WAD.from_file(self.workspace.iwad)
        self.pwads.add_wad(self.iwad)

        # Load PWADs.
        for pwad_file in self.workspace.pwads:
            if not os.path.exists(pwad_file):
                wx.MessageBox(
                    message=f'The PWAD {pwad_file} could not be found.',
                    caption='Missing PWAD',
                    style=wx.OK | wx.ICON_EXCLAMATION,
                    parent=self
                )
                self.workspace.pwads.remove(pwad_file)
                self.patch_modified = True

            else:
                pwad = WAD.from_file(pwad_file)
                self.pwads.add_wad(pwad)

        # Build the sprite lookup tables.
        self.pwads.build_sprite_list()
        if self.pwads.palette is None:
            wx.MessageBox(
                message='No PLAYPAL lump could be found in any of the loaded WAD files. '
                        'Sprite previews will be disabled.',
                caption='Missing PLAYPAL',
                style=wx.OK | wx.ICON_INFORMATION,
                parent=self
            )
            self.workspace.iwad = None

        wx.EndBusyCursor()

    def save_file_dialog(self):
        """
        Displays a save file dialog to save the current patch file.
        """

        # Use the patch filename if it was saved before.
        if self.patch.filename is not None:
            use_filename = self.patch.filename

        # Otherwise use a default filename and extension.
        else:
            if self.patch.extended:
                use_filename = 'unnamed.bex'
            else:
                use_filename = 'unnamed.deh'

        filename = utils.file_dialog(
            self,
            message='Save Dehacked file',
            default_file=use_filename,
            wildcard='All supported files|*.deh;*.bex|Dehacked files (*.deh)|*.deh|'
                     'Extended Dehacked files (*.bex)|*.bex|All files|*.*',
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        )

        if filename is not None:
            self.save_file(filename)
            return True

        return False

    def save_file(self, filename: str):
        """
        Saves a Dehacked patch file.
        """

        wx.BeginBusyCursor()

        for window in self.editor_windows.values():
            window.before_save()

        # Create a backup of the existing file.
        if os.path.exists(filename):
            shutil.copyfile(filename, filename + '.bak')

        # Write patch.
        message = self.patch.write_dehacked(filename)
        if message is not None:
            wx.MessageBox(
                message=message,
                caption='Patch write error',
                style=wx.OK | wx.ICON_ERROR,
                parent=self
            )
            return

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
        while self.MenuFileRecent.GetMenuItemCount() > 0:
            item = self.MenuFileRecent.FindItemByPosition(0)
            self.MenuFileRecent.DestroyItem(item)

        # Add all recent files again.
        recent_files = config.settings['recent_files']
        for recent_file in recent_files:
            item = self.MenuFileRecent.Append(wx.ID_ANY, recent_file, '', wx.ITEM_NORMAL)
            self.Bind(wx.EVT_MENU, self.file_open_recent, id=item.GetId())

    def update_ui(self):
        """
        Updates the user interface contents of this main window and all
        available editor windows.
        """

        wx.BeginBusyCursor()

        # Update editor window contents.
        for window in self.editor_windows.values():
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

    def set_modified(self, is_modified: bool):
        """
        Used to mark the current patch as modified.

        Upon attempting to exit, the user will be asked to save the patch before
        doing so, if it has been modified.
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

        if self.patch_modified:
            label += ' *'

        self.SetLabel(label)

        # On Mac, also mark the close button as dirty
        self.OSXSetModified(self.patch_modified)

    def new_file(self):
        """
        Creates a new Dehacked patch file.
        """

        new_workspace = workspace.Workspace()

        # Ask the user to provide patch details.
        patch_info = patchinfodialog.PatchInfoDialog(self)
        patch_info.set_state(
            None,
            None,
            None,
            self.engines,
            new_workspace
        )
        patch_info.ShowModal()

        if patch_info.selected_engine is None:
            return

        # Store patch details in the new workspace.
        new_workspace.iwad = patch_info.selected_iwad
        new_workspace.pwads = patch_info.selected_pwads
        new_workspace.engine = patch_info.selected_engine

        # Initialize patch table data.
        selected_engine = self.engines[patch_info.selected_engine]
        new_patch = patch.Patch(selected_engine)
        new_patch.version = max(selected_engine.versions)
        new_patch.extended = selected_engine.extended

        # Store new patch info.
        self.patch = new_patch
        self.patch_info = patch_info
        self.workspace = new_workspace
        self.set_modified(False)

        # Initialize the UI.
        self.load_wads()
        self.editor_windows_show(False)
        self.update_ui()
        self.file_set_state()

    def save_if_needed(self) -> bool:
        """
        Requests the user to save the current patch file if it has been modified.
        """

        if self.patch_modified:
            result = wx.MessageBox(
                message='The file has been modified. Save changes?',
                caption='Save file',
                style=wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION,
                parent=self
            )

            if result == wx.YES:
                if self.patch.filename is None:
                    return self.save_file_dialog()
                self.save_file(self.patch.filename)

            elif result == wx.CANCEL:
                return False

        return True

    def close(self, event: CloseEvent):
        """
        Called when this window is being closed.
        """

        if not self.save_if_needed():
            return

        if self.workspace_modified:
            self.workspace_save()

        config.settings.save()

        self.DestroyChildren()
        self.Destroy()

        wx.GetApp().ExitMainLoop()

        sys.exit(-1)

    def editor_window_toolid_for_instance(self, window: MDIChildFrame) -> int:
        """
        Returns a toolbar tool id for an editor window instance.

        @return: a toolbar id if the window instance was found, wx.NOT_FOUND
        if none was found.
        """

        for tool_id, editor_window in self.editor_windows.items():
            if window == editor_window:
                return tool_id

        return wx.NOT_FOUND

    def editor_window_activate(self):
        """
        Called by a window that is being activated.
        """

        self.editor_window_set_edit()

    def editor_window_set_edit(self):
        """
        Sets the state of some edit menu tools.
        """

        # Disable edit menu tools if no window is active.
        active_child = self.GetActiveChild()
        if active_child is None or not active_child.IsShown():
            edit_state = False
            undo_state = False
        else:
            edit_state = hasattr(active_child, 'edit_copy')
            undo_state = True

        self.MenuEditCopy.Enable(edit_state)
        self.MenuEditPaste.Enable(edit_state)
        self.MenuEditUndo.Enable(undo_state)

    def editor_window_show(self, tool_id: int):
        """
        Shows an editor window.

        @param tool_id: the toolbar id of the window to show.
        """

        window = self.editor_windows[tool_id]
        window.Maximize(False)
        window.Show(True)

        self.MainToolbar.ToggleTool(tool_id, True)
        self.workspace_modified = True

    def editor_window_menutoggle(self, event: CommandEvent):
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

        self.editor_window_set_edit()

    def editor_window_tooltoggle(self, event: CommandEvent):
        """
        Toggles the visibility of an editor window from a toolbar item.
        """

        toolid = event.GetId()
        window = self.editor_windows[toolid]

        if window is not None:
            state = self.MainToolbar.GetToolState(toolid)
            active = self.GetActiveChild()

            # Bring a window to front if it is activated but not the active one.
            if not state and active != window:
                self.MainToolbar.ToggleTool(toolid, True)
                window.Activate()
            else:
                window.Maximize(False)
                window.Show(state)

            self.workspace_modified = True

        self.editor_window_set_edit()

    def editor_windows_show(self, show: bool):
        """
        Sets the visibility of all editor windows at once.
        """

        for window in self.editor_windows.values():
            window.Show(show)

    def editor_window_closed(self, window: MDIChildFrame):
        """
        Act on editor window being closed.
        """

        tool_id = self.editor_window_toolid_for_instance(window)
        if tool_id == wx.NOT_FOUND:
            return

        self.MainToolbar.ToggleTool(tool_id, False)
        window.Show(False)
        self.workspace_modified = True

        self.editor_window_set_edit()

    def toolbar_set_enabled(self, enabled: bool):
        """
        Sets the toolbar button and menu item enabled states.
        """

        # Set toolbar states.
        for tool_id in self.editor_windows:
            self.MainToolbar.EnableTool(tool_id, enabled)

        # Set menu states.
        self.MenuViewThings.Enable(enabled)
        self.MenuViewStates.Enable(enabled)
        self.MenuViewAmmo.Enable(enabled)
        self.MenuViewCheats.Enable(enabled)
        self.MenuViewStrings.Enable(enabled)
        self.MenuViewWeapons.Enable(enabled)
        self.MenuViewSounds.Enable(enabled)
        self.MenuViewMiscellaneous.Enable(enabled)
        self.MenuViewPatchSettings.Enable(enabled)

        # Disable unsupported editor tabs.
        if self.patch is not None:
            enable = 'nosupport.pars' not in self.patch.engine.features
            self.MainToolbar.EnableTool(windows.MAIN_TOOL_PAR, enable)
            self.MenuViewPar.Enable(enable)

        self.editor_window_set_edit()

    def toolbar_update_state(self):
        """
        Updates the toolbar button's state to reflect whether they are shown or not.
        """

        for tool_id, window in self.editor_windows.items():
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

    def file_set_state(self):
        """
        Set the state of file related menu options.
        """

        state = self.workspace is not None

        self.MenuFileReloadWADs.Enable(state)
        self.MenuFileSave.Enable(state)
        self.MenuFileSaveAs.Enable(state)

    def workspace_update_data(self, event: Event):
        """
        Update the current workspace with this window's size, position and state.
        """

        if not self:
            return

        # Only update size and position if the window is not maximized.
        if self.IsMaximized() or not self.IsShown():
            main_window_state = config.settings['main_window_state']

            pos = (main_window_state['x'], main_window_state['y'])
            size = (main_window_state['width'], main_window_state['height'])
        else:
            pos = self.GetPosition()
            size = self.GetSize()

        config.settings.main_window_state_store(
            pos[0], pos[1],
            size[0], size[1],
            self.IsMaximized()
        )

        event.Skip()

    def file_new(self, event: MenuEvent):
        if not self.save_if_needed():
            return

        self.new_file()

    def file_save(self, event: MenuEvent):
        if self.patch.filename is None:
            self.save_file_dialog()
        else:
            self.save_file(self.patch.filename)

    def file_save_as(self, event: MenuEvent):
        self.save_file_dialog()

    def file_open(self, event: MenuEvent):
        self.open_file_dialog()

    def file_open_as(self, event: MenuEvent):
        self.open_file_dialog(force_show_settings=True)

    def file_merge_with(self, event: MenuEvent):
        self.open_file_merge_dialog()

    def wads_reload(self, event: MenuEvent):
        self.workspace.store_windows(self, self.workspace_windows)
        self.load_wads()

        for window in self.editor_windows.values():
            window.update()

    def file_open_recent(self, event: MenuEvent):
        """
        Open a recent file.
        """

        item = self.MainMenu.FindItemById(event.GetId())
        filename = item.GetItemLabel()
        self.open_file(filename)

    def edit_undo(self, event: MenuEvent):
        window = self.GetActiveChild()
        if window is None:
            return
        window.undo_do_undo()

    def edit_redo(self, _: MenuEvent):
        """
        Redo last action.
        """

        window = self.GetActiveChild()
        if window is None:
            return
        window.undo_do_redo()

    def edit_copy(self, event: MenuEvent):
        window = self.GetActiveChild()
        if window is None:
            return
        window.edit_copy()

    def edit_paste(self, event: MenuEvent):
        window = self.GetActiveChild()
        if window is None:
            return
        window.edit_paste()

    def help_about(self, event: MenuEvent):
        self.about_dialog.ShowModal()

    def help_help(self, event: MenuEvent):
        file = 'file://' + os.path.join(os.getcwd(), 'docs/index.html')
        webbrowser.open(file)

    def _adjust_mac_ui(self):
        if sys.platform != 'darwin':
            return

        # Adjust the toolbar
        style = self.MainToolbar.GetWindowStyle()
        style &= ~wx.TB_VERTICAL
        style |= wx.TB_HORIZONTAL
        self.MainToolbar.SetWindowStyle(style)
        tool_info = []
        for index in range(self.MainToolbar.GetToolsCount()):
            tool = self.MainToolbar.GetToolByPos(index)
            tool_info.append((
                tool.GetId(),
                tool.GetLabel(),
                tool.GetBitmap().ConvertToImage().Scale(80, 80, wx.IMAGE_QUALITY_HIGH).ConvertToBitmap()
            ))
        self.MainToolbar.ClearTools()
        for entry in tool_info:
            self.MainToolbar.AddTool(entry[0], entry[1], entry[2], wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None)
        self.MainToolbar.Realize()
