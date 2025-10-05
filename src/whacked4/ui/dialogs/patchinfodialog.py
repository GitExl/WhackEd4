"""
Dehacked patch info UI.
"""

import os.path
import sys
from typing import Dict, Optional, List

import wx
from wx import Window, CommandEvent

from whacked4 import utils
from whacked4.dehacked.engine import Engine
from whacked4.doom import wad
from whacked4.doom.wad import WAD
from whacked4.ui import windows
from whacked4.ui.workspace import Workspace


class PatchInfoDialog(windows.PatchInfoDialogBase):
    """
    This dialog allows the user to modify Dehacked patch related settings.
    """

    def __init__(self, parent: Window):
        windows.PatchInfoDialogBase.__init__(self, parent)
        self._adjust_mac_ui()

        self.SetEscapeId(windows.PATCHINFO_CANCEL)

        self.selected_engine: Optional[str] = None
        self.selected_iwad: Optional[str] = None
        self.selected_pwads: Optional[List[str]] = None

        self.engines: Optional[Dict[str, Engine]] = None
        self.workspace: Optional[Workspace] = None

        self.pwads: Optional[List[str]] = None

    def reset(self):
        """
        Resets this dialog's state.
        """

        self.selected_engine = None
        self.selected_iwad = None
        self.selected_pwads = None

        self.engines = None
        self.workspace = None

        self.pwads = []

        self.EngineList.Clear()

        self.PWADList.ClearAll()
        client_width = self.PWADList.GetClientSize()[0]
        self.PWADList.InsertColumn(0, 'Filename', width=client_width)

    def set_state(
        self,
        filename: Optional[str],
        version: Optional[int],
        is_extended: Optional[bool],
        engines: Dict[str, Engine],
        workspace: Workspace,
        modify_engine: bool = True
    ):
        """
        Sets this dialog's state.

        @param filename: the filename of the patch.
        @param version: optional detected patch version.
        @param is_extended: optional extended engine state.
        @param engines: a dict of engine configurations.
        @param workspace: a loaded workspace object.
        @param modify_engine: set to True if the user is allowed to change the engine.
        """

        self.reset()

        self.engines = engines
        self.workspace = workspace

        # Display the patch filename if it exists.
        if filename is not None:
            self.SetLabel('Patch settings - ' + os.path.basename(filename))
        else:
            self.SetLabel('Patch settings')

        if workspace.iwad is not None:
            self.IWAD.SetValue(workspace.iwad)
            self.IWADNotificationPanel.Hide()
        else:
            self.IWAD.SetValue('')
            self.IWADNotificationPanel.Show()

        # Build PWAD list.
        if workspace.pwads is not None:
            for index, pwad in enumerate(workspace.pwads):
                self.pwads.append(pwad)
                self.PWADList.InsertItem(index, pwad)

        # Display a list of engines that are supported by the patch.
        for name, engine in self.engines.items():
            if engine.is_compatible(version, is_extended) or version is None or version == 0:
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

    def ok(self, event: CommandEvent):
        """
        Called when the user presses the Ok button.

        The selected patch details are stored more permanently before hiding.
        """

        # An engine must always be selected.
        if self.EngineList.GetSelection() == -1:
            wx.MessageBox(
                message='No engine selected.',
                caption='Patch settings',
                style=wx.OK | wx.ICON_EXCLAMATION,
                parent=self
            )
            return

        # Store selected details.
        self.selected_engine = self.EngineList.GetClientData(self.EngineList.GetSelection())
        self.selected_iwad = self.IWAD.GetValue()
        if self.selected_iwad == '':
            self.selected_iwad = None
        self.selected_pwads = self.pwads

        self.EndModal(0)

    def delete_iwad(self, event: CommandEvent):
        """
        Deletes the currently selected IWAD.
        """

        self.IWAD.ChangeValue('')
        self.IWADNotificationPanel.Show()
        self.Layout()

    def browse_iwad(self, event: CommandEvent):
        """
        Displays the IWAD file browser.
        """

        filename = utils.file_dialog(
            self,
            message='Choose an IWAD',
            wildcard='WAD files (*.wad)|*.wad|All files|*.*',
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
            default_file=self.IWAD.GetValue()
        )

        if filename is not None:
            # Validate the WAD file.
            try:
                iwad = WAD.from_file(filename)
            except wad.WADTypeError:
                wx.MessageBox(
                    message='The selected WAD is not a valid WAD file.',
                    caption='Invalid WAD file',
                    style=wx.OK | wx.ICON_EXCLAMATION,
                    parent=self
                )
            else:
                if iwad.type != 'IWAD':
                    wx.MessageBox(
                        message='The selected WAD is not an IWAD.',
                        caption='Invalid WAD file',
                        style=wx.OK | wx.ICON_EXCLAMATION,
                        parent=self
                    )
                else:
                    self.IWAD.SetValue(filename)
                    self.IWADNotificationPanel.Hide()
                    self.Layout()

    def pwad_add(self, event: CommandEvent):
        """
        Displays the PWAD file browser.
        """

        filename = utils.file_dialog(
            self,
            message='Choose a PWAD',
            wildcard='WAD files (*.wad)|*.wad|All files|*.*',
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
            default_file=self.IWAD.GetValue()
        )

        if filename is not None:
            # Validate the WAD file.
            try:
                pwad = WAD.from_file(filename)
            except wad.WADTypeError:
                wx.MessageBox(
                    message='The selected WAD is not a valid WAD file.',
                    caption='Invalid WAD file',
                    style=wx.OK | wx.ICON_EXCLAMATION,
                    parent=self
                )
            else:
                if pwad.type != 'PWAD':
                    wx.MessageBox(
                        message='The selected WAD is not a PWAD.',
                        caption='Invalid WAD file',
                        style=wx.OK | wx.ICON_EXCLAMATION,
                        parent=self
                    )
                else:

                    # Append it to the relevant lists.
                    self.pwads.append(filename)
                    self.PWADList.InsertItem(len(self.pwads), filename)

    def pwad_remove(self, event: CommandEvent):
        """
        Removes the selected PWAD from the list.
        """

        index = self.PWADList.GetFirstSelected()
        if index > -1:
            del self.pwads[index]
            self.PWADList.DeleteItem(index)

    def cancel(self, event: CommandEvent):
        self.EndModal(0)

    def _adjust_mac_ui(self):
        if sys.platform != 'darwin':
            return
        bitmap_size = self.m_toolBar3.GetToolBitmapSize()
        info = [(
            tool.GetId(),
            tool.GetLabel(),
            tool.GetBitmap().ConvertToImage().Scale(
                bitmap_size.x,
                bitmap_size.y,
                wx.IMAGE_QUALITY_HIGH
            ).ConvertToBitmap(),
            tool.GetDisabledBitmap(),
            tool.GetKind(),
            tool.GetShortHelp(),
            tool.GetLongHelp(),
            tool.GetClientData()
        ) for tool in (self.AddPWAD, self.RemovePWAD)]
        self.m_toolBar3.ClearTools()
        self.AddPWAD = self.m_toolBar3.AddTool(*info[0])
        self.RemovePWAD = self.m_toolBar3.AddTool(*info[1])
        self.m_toolBar3.Realize()
