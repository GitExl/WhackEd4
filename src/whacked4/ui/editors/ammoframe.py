"""
Ammo editor UI.
"""

from math import floor
from typing import Dict, Optional

import wx
from wx import Window, SizeEvent, ListEvent, CommandEvent

from whacked4 import utils
from whacked4.dehacked.patch import Patch
from whacked4.ui import editormixin, windows
from whacked4.ui.editormixin import UndoItem


class AmmoFrame(editormixin.EditorMixin, windows.AmmoFrameBase):
    """
    Ammo editor window.
    """

    # Text control to internal key mappings.
    PROPS_VALUES: Dict[int, str] = {
        windows.AMMO_VAL_MAXIMUM: 'maximum',
        windows.AMMO_VAL_PICKUP: 'clip'
    }

    def __init__(self, parent: Window):
        windows.AmmoFrameBase.__init__(self, parent)
        editormixin.EditorMixin.__init__(self)

        self.SetIcon(wx.Icon('res/editor-ammo.png'))

        self.patch: Optional[Patch] = None
        self.selected_index: int = -1

    def build(self, patch: Patch):
        """
        @see: EditorMixin.build
        """

        self.patch = patch
        self.selected_index = -1

        self.ammolist_build()

    def update(self):
        """
        @see: EditorMixin.update
        """

    def ammolist_build(self):
        """
        Builds the ammo list from scratch.
        """

        self.AmmoList.ClearAll()

        # Add column headers if necessary.
        if self.AmmoList.GetColumnCount() == 0:
            self.AmmoList.InsertColumn(0, 'Name', width=floor(76 * self.GetDPIScaleFactor()))
            self.AmmoList.InsertColumn(1, 'Maximum', width=floor(67 * self.GetDPIScaleFactor()))
            self.AmmoList.InsertColumn(2, 'Pickup', width=floor(49 * self.GetDPIScaleFactor()))

        for ammo_index in range(len(self.patch.ammo)):
            self.AmmoList.InsertItem(ammo_index, '')

            self.ammolist_update_row(ammo_index)

        self.list_autosize(self.AmmoList)
        self.AmmoList.Select(0, True)

    def ammolist_update_row(self, row_index: int):
        """
        Updates a row in the ammo list.
        """

        ammo = self.patch.ammo[row_index]

        self.AmmoList.SetItem(row_index, 0, ammo.name)
        self.AmmoList.SetItem(row_index, 1, str(ammo['maximum']))
        self.AmmoList.SetItem(row_index, 2, str(ammo['clip']))

    def ammolist_resize(self, event: SizeEvent):
        """
        Resize the ammo name column as wide as possible.
        """

        if not self.AmmoList.GetColumnCount():
            return

        column_width = self.AmmoList.GetClientSize()[0] - 4
        self.AmmoList.SetColumnWidth(0, column_width // 3)
        self.AmmoList.SetColumnWidth(1, column_width // 3)
        self.AmmoList.SetColumnWidth(2, column_width // 3)

    def ammo_select(self, event: ListEvent):
        """
        Selects a new ammo entry.
        """

        self.selected_index = event.GetIndex()
        self.update_properties()

    def ammo_rename(self, event: CommandEvent):
        """
        Called when the current ammo entry needs to be renamed.
        """

        self.ammo_rename_action()

    def ammo_rename_action(self):
        """
        Renames the currently selected ammo entry.
        """

        ammo_name = self.patch.ammo[self.selected_index].name
        new_name = wx.GetTextFromUser('Enter a new name for ' + ammo_name, caption='Change name',
                                      default_value=ammo_name, parent=self)

        if new_name != '':
            self.undo_add()

            self.patch.ammo[self.selected_index].name = new_name
            self.update_properties()
            self.is_modified(True)

    def ammo_restore(self, event: CommandEvent):
        """
        Restores the currently selected ammo entry to it's engine state.
        """

        self.undo_add()

        self.patch.ammo[self.selected_index] = self.patch.engine.ammo[self.selected_index].clone()

        self.update_properties()
        self.ammolist_update_row(self.selected_index)

    def update_properties(self):
        """
        Updates the displayed properties of the currently selected entry.
        """

        if not self.patch:
            return

        ammo = self.patch.ammo[self.selected_index]

        self.Maximum.ChangeValue(str(ammo['maximum']))
        self.Pickup.ChangeValue(str(ammo['clip']))
        self.AmmoList.SetItem(self.selected_index, 0, self.patch.get_ammo_name(self.selected_index))

        # Disable rename\restore for hardcoded entries.
        if self.selected_index >= len(self.patch.ammo):
            self.Restore.Disable()
            self.Rename.Disable()
        else:
            self.Restore.Enable()
            self.Rename.Enable()

    def set_value(self, event: CommandEvent):
        """
        Sets the currently selected ammo entry's property value.
        """

        self.undo_add()

        window_id = event.GetId()
        window = self.FindWindowById(window_id)
        value = utils.validate_numeric(window)

        key = self.PROPS_VALUES[window_id]
        self.patch.ammo[self.selected_index][key] = value

        self.ammolist_update_row(self.selected_index)
        self.is_modified(True)

    def undo_restore_item(self, item: UndoItem):
        """
        @see: EditorMixin.undo_restore_item
        """

        index = item['index']
        self.patch.ammo[index] = item['item']

        self.ammolist_update_row(index)
        self.update_properties()

        self.is_modified(True)

    def undo_store_item(self) -> UndoItem:
        """
        @see: EditorMixin.undo_store_item
        """

        return {
            'item': self.patch.ammo[self.selected_index].clone(),
            'index': self.selected_index
        }
