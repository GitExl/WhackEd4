#!/usr/bin/env python
#coding=utf8

from whacked4 import utils
from whacked4.doom import wad
from whacked4.ui import windows
import os.path
import wx


class PatchInfoDialog(windows.PatchInfoDialogBase):
    """
    This dialog allows the user to modify Dehacked patch related settings.
    """

    def __init__(self, parent):
        windows.PatchInfoDialogBase.__init__(self, parent)

        self.SetEscapeId(windows.PATCHINFO_CANCEL)

        self.selected_engine = None
        self.selected_iwad = None
        self.selected_pwads = None

        self.patch = None
        self.engines = None
        self.workspace = None

        self.pwads = None

    def reset(self):
        """
        Resets this dialog's state.
        """

        self.selected_engine = None
        self.selected_iwad = None
        self.selected_pwads = None

        self.patch = None
        self.engines = None
        self.workspace = None

        self.pwads = []

        self.EngineList.Clear()

        self.PWADList.ClearAll()
        client_width = self.PWADList.GetClientSize()[0]
        self.PWADList.InsertColumn(0, 'Filename', width=client_width)

    def set_state(self, patch, engines, workspace, modify_engine=True):
        """
        Sets this dialog's state.

        @param patch: the patch object to display this dialog for.
        @param engines: a dict of engine configurations.
        @param workspace: a loaded workspace object.
        @param modify_engine: set to True if the user is allowed to change the engine.
        """

        self.reset()

        self.patch = patch
        self.engines = engines
        self.workspace = workspace

        # Display the patch filename if it exists.
        if patch.filename is not None:
            self.SetLabel('Patch settings - ' + os.path.basename(patch.filename))
        else:
            self.SetLabel('Patch settings')

        if workspace.iwad is not None:
            self.IWAD.SetValue(workspace.iwad)
        else:
            self.IWAD.SetValue('')

        # Build PWAD list.
        if workspace.pwads is not None:
            for index, pwad in enumerate(workspace.pwads):
                self.pwads.append(pwad)
                self.PWADList.InsertItem(index, pwad)

        # Display a list of engines that are supported by the patch.
        for name, engine in self.engines.items():
            if engine.is_compatible(self.patch) or self.patch.version == 0:
                self.EngineList.Append(engine.name, clientData=name)

                if workspace.engine == name:
                    self.EngineList.Select(self.EngineList.GetCount() - 1)

        # Select the first engine in the list if the patch matched none.
        if self.EngineList.GetSelection() == wx.NOT_FOUND and self.EngineList.GetCount() > 0:
            self.EngineList.Select(0)

        if not modify_engine:
            self.EngineList.Disable()
        else:
            self.EngineList.Enable()

    def ok(self, event):
        """
        Called when the user presses the Ok button.

        The selected patch details are stored more permanently before hiding.
        """

        # An engine must always be selected.
        if self.EngineList.GetSelection() == -1:
            wx.MessageBox(message='No engine selected.', caption='Patch settings', style=wx.OK | wx.ICON_EXCLAMATION,
                          parent=self)
            return

        # Without an IWAD, sprite previews are not possible.
        if self.IWAD.GetValue() == '':
            result = wx.MessageBox(message='No IWAD selected. Sprite previews will not be available.',
                                   caption='Missing IWAD', style=wx.OK | wx.CANCEL | wx.ICON_EXCLAMATION, parent=self)
            if result == wx.CANCEL:
                return

        # Store selected details.
        self.selected_engine = self.EngineList.GetClientData(self.EngineList.GetSelection())
        self.selected_iwad = self.IWAD.GetValue()
        if self.selected_iwad == '':
            self.selected_iwad = None
        self.selected_pwads = self.pwads

        self.EndModal(0)

    def delete_iwad(self, event):
        """
        Deletes the currently selected IWAD.
        """

        self.IWAD.ChangeValue('')

    def browse_iwad(self, event):
        """
        Displays the IWAD file browser.
        """

        filename = utils.file_dialog(self, message='Choose an IWAD', wildcard='WAD files (*.wad)|*.wad|All files|*.*',
                                     style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST, default_file=self.IWAD.GetValue())

        if filename is not None:
            # Validate the WAD file.
            try:
                iwad = wad.WADReader(filename)
            except wad.WADTypeError:
                wx.MessageBox(message='The selected WAD is not a valid WAD file.', caption='Invalid WAD file',
                              style=wx.OK | wx.ICON_EXCLAMATION, parent=self)
            else:
                if iwad.type != 'IWAD':
                    wx.MessageBox(message='The selected WAD is not an IWAD.', caption='Invalid WAD file',
                                  style=wx.OK | wx.ICON_EXCLAMATION, parent=self)
                else:
                    self.IWAD.SetValue(filename)

    def pwad_add(self, event):
        """
        Displays the PWAD file browser.
        """

        filename = utils.file_dialog(self, message='Choose a PWAD', wildcard='WAD files (*.wad)|*.wad|All files|*.*',
                                     style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST, default_file=self.IWAD.GetValue())

        if filename is not None:
            # Validate the WAD file.
            try:
                pwad = wad.WADReader(filename)
            except wad.WADTypeError:
                wx.MessageBox(message='The selected WAD is not a valid WAD file.', caption='Invalid WAD file',
                              style=wx.OK | wx.ICON_EXCLAMATION, parent=self)
            else:
                if pwad.type != 'PWAD':
                    wx.MessageBox(message='The selected WAD is not a PWAD.', caption='Invalid WAD file',
                                  style=wx.OK | wx.ICON_EXCLAMATION, parent=self)
                else:

                    # Append it to the relevant lists.
                    self.pwads.append(filename)
                    self.PWADList.InsertItem(len(self.pwads), filename)

    def pwad_remove(self, event):
        """
        Removes the selected PWAD from the list.
        """

        index = self.PWADList.GetFirstSelected()
        if index > -1:
            del self.pwads[index]
            self.PWADList.DeleteItem(index)

    def cancel(self, event):
        self.EndModal(0)
