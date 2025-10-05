"""
Par time editor UI.
"""

import sys

from math import floor
from typing import Dict, Optional

import wx
from wx import Window, SizeEvent, ListEvent, CommandEvent

from whacked4 import utils
from whacked4.dehacked import entries
from whacked4.dehacked.patch import Patch
from whacked4.ui import editormixin, windows
from whacked4.ui.editormixin import UndoItem


class ParFrame(editormixin.EditorMixin, windows.ParFrameBase):
    """
    Par times editor window.
    """

    # Maps window ids to value keys.
    PROPS_VALUES: Dict[int, str] = {
        windows.PAR_EPISODE: 'episode',
        windows.PAR_MAP: 'map',
        windows.PAR_SECONDS: 'seconds'
    }

    def __init__(self, parent: Window):
        windows.ParFrameBase.__init__(self, parent)
        editormixin.EditorMixin.__init__(self)
        self._adjust_mac_ui()

        self.SetIcon(wx.Icon('res/editor-par.png'))

        self.patch: Optional[Patch] = None
        self.selected_index: int = 0

    def build(self, patch: Patch):
        """
        @see: EditorMixin.build
        """

        self.patch = patch
        if not patch.extended:
            return

        self.selected_index = 0
        self.parlist_build()

    def update(self):
        """
        @see: EditorMixin.update
        """

    def parlist_build(self):
        """
        Builds a new par times list.
        """

        self.ParList.ClearAll()
        self.ParList.InsertColumn(0, 'Map', width=floor(59 * utils.get_platform_dpi_scale(self)))
        self.ParList.InsertColumn(1, 'Seconds', width=floor(58 * utils.get_platform_dpi_scale(self)))
        self.ParList.InsertColumn(2, 'Minutes', width=floor(69 * utils.get_platform_dpi_scale(self)))

        for index, _ in enumerate(self.patch.pars.entries):
            self.ParList.InsertItem(index, '')
            self.parlist_update_row(index)

        self.list_autosize(self.ParList)

        # Select the first entry if it is available.
        if self.ParList.GetItemCount() > 0 and self.selected_index < len(self.patch.pars.entries):
            self.ParList.Select(self.selected_index, True)
            self.properties_set_state(True)
        else:
            self.selected_index = -1
            self.properties_set_state(False)

    def parlist_update_row(self, row_index: int):
        """
        Updates a row in the par times list.
        """

        par = self.patch.pars.entries[row_index]

        self.ParList.SetItem(row_index, 0, utils.get_map_name(par['episode'], par['map']))
        self.ParList.SetItem(row_index, 1, str(par['seconds']))
        self.ParList.SetItem(row_index, 2, utils.seconds_to_minutes(par['seconds']))

    def parlist_resize(self, event: SizeEvent):
        """
        Resize the parlist columns to divide them over the width of the client area.
        """

        self.list_autosize(self.ParList)
        event.Skip()

    def properties_set_state(self, state: bool):
        """
        Sets the state of the properties controls.
        """

        self.Episode.Enable(state)
        self.Map.Enable(state)
        self.Seconds.Enable(state)
        self.Tools.EnableTool(windows.PAR_TOOL_REMOVE, state)

    def par_select(self, event: ListEvent):
        """
        Selects a par time from the list.
        """

        self.selected_index = event.GetIndex()
        self.update_properties()
        self.properties_set_state(True)

    def par_add(self, event: CommandEvent):
        """
        Adds a new par time to the list.
        """

        self.undo_add()

        # Add a new par time.
        par = entries.ParEntry(self.patch.pars).from_json({
            'episode': 0,
            'map': 1,
            'seconds': 666,
        })
        self.patch.pars.entries.append(par)

        self.parlist_build()
        self.ParList.Select(len(self.patch.pars.entries) - 1, True)

    def par_remove(self, event: CommandEvent):
        """
        Removes the currently selected par time from the list.
        """

        self.undo_add()

        del self.patch.pars.entries[self.selected_index]
        self.parlist_build()

    def update_properties(self):
        """
        Updates the property controls of the currently displayed par time.
        """

        if not self.patch:
            return

        par = self.patch.pars.entries[self.selected_index]

        self.Episode.ChangeValue(str(par['episode']))
        self.Map.ChangeValue(str(par['map']))
        self.Seconds.ChangeValue(str(par['seconds']))

    def set_value(self, event: CommandEvent):
        """
        Validates and sets a property.
        """

        self.undo_add()

        window_id = event.GetId()
        window = self.FindWindowById(window_id)

        key = self.PROPS_VALUES[window_id]
        value = utils.validate_numeric(window)

        # Clamp values so that they make sense.
        if key == 'episode':
            value = max(0, min(value, 9))
        elif key == 'map':
            value = max(0, min(value, 99))
        elif key == 'seconds':
            value = max(0, value)
        window.ChangeValue(str(value))

        self.patch.pars.entries[self.selected_index][key] = value

        self.parlist_update_row(self.selected_index)
        self.is_modified(True)

    def undo_restore_item(self, item: UndoItem):
        """
        @see: EditorMixin.undo_restore_item
        """

        self.patch.pars.entries = item['pars']
        self.parlist_build()

        self.is_modified(True)

    def undo_store_item(self) -> UndoItem:
        """
        @see: EditorMixin.undo_store_item

        Undo for this editor works by storing *all* par entries in a single undo item.
        """

        dup = []
        for par in self.patch.pars.entries:
            dup.append(par.clone())

        return {
            'pars': dup
        }

    def _adjust_mac_ui(self):
        if sys.platform != 'darwin':
            return

        bitmap_size = self.Tools.GetToolBitmapSize()
        add_id, add_label, add_bitmap, add_dis_bitmap, add_kind, add_short_help, add_long_help, add_client_data = (
            self.Add.GetId(),
            self.Add.GetLabel(),
            self.Add.GetBitmap().ConvertToImage().Scale(bitmap_size.x, bitmap_size.y).ConvertToBitmap(),
            self.Add.GetDisabledBitmap(),
            self.Add.GetKind(),
            self.Add.GetShortHelp(),
            self.Add.GetLongHelp(),
            self.Add.GetClientData()
        )
        rem_id, rem_label, rem_bitmap, rem_dis_bitmap, rem_kind, rem_short_help, rem_long_help, rem_client_data = (
            self.Remove.GetId(),
            self.Remove.GetLabel(),
            self.Remove.GetBitmap().ConvertToImage().Scale(bitmap_size.x, bitmap_size.y).ConvertToBitmap(),
            self.Remove.GetDisabledBitmap(),
            self.Remove.GetKind(),
            self.Remove.GetShortHelp(),
            self.Remove.GetLongHelp(),
            self.Remove.GetClientData()
        )
        self.Tools.ClearTools()
        self.Add = self.Tools.AddTool(
            add_id,
            add_label,
            add_bitmap,
            add_dis_bitmap,
            add_kind,
            add_short_help,
            add_long_help,
            add_client_data
        )
        self.Remove = self.Tools.AddTool(
            rem_id,
            rem_label,
            rem_bitmap,
            rem_dis_bitmap,
            rem_kind,
            rem_short_help,
            rem_long_help,
            rem_client_data
        )
        self.Tools.Realize()
