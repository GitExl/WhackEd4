#!/usr/bin/env python
#coding=utf8

from whacked4 import utils
from whacked4.dehacked import entries
from whacked4.ui import editormixin, windows
import copy
import wx


class ParFrame(editormixin.EditorMixin, windows.ParFrameBase):
    """
    Par times editor window.
    """

    # Maps window ids to value keys.
    PROPS_VALUES = {
        windows.PAR_EPISODE: 'episode',
        windows.PAR_MAP: 'map',
        windows.PAR_SECONDS: 'seconds'
    }

    def __init__(self, params):
        windows.ParFrameBase.__init__(self, params)
        editormixin.EditorMixin.__init__(self)

        self.SetIcon(wx.Icon('res/editor-par.ico'))

        self.patch = None
        self.selected_index = 0

    def build(self, patch):
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

        pass

    def parlist_build(self):
        """
        Builds a new par times list.
        """

        self.ParList.ClearAll()

        # Add columns if needed.
        if self.ParList.GetColumnCount() == 0:
            self.ParList.InsertColumn(0, 'Map', width=59)
            self.ParList.InsertColumn(1, 'Seconds', width=58)
            self.ParList.InsertColumn(2, 'Minutes', width=69)

        for index in range(len(self.patch.pars)):
            self.ParList.InsertStringItem(index, '')

            self.parlist_update_row(index)

        self.list_autosize(self.ParList)

        # Select the first entry if it is available.
        if self.ParList.GetItemCount() > 0 and self.selected_index < len(self.patch.pars):
            self.ParList.Select(self.selected_index, True)
            self.properties_set_state(True)
        else:
            self.selected_index = -1
            self.properties_set_state(False)

    def parlist_update_row(self, row_index):
        """
        Updates a row in the par times list.
        """

        par = self.patch.pars[row_index]

        self.ParList.SetStringItem(row_index, 0, utils.get_map_name(par['episode'], par['map']))
        self.ParList.SetStringItem(row_index, 1, str(par['seconds']))
        self.ParList.SetStringItem(row_index, 2, utils.seconds_to_minutes(par['seconds']))

    def parlist_resize(self, event):
        """
        Resize the parlist columns to divide them over the width of the client area.
        """

        column_width = (self.ParList.GetClientSize()[0] - 4) / 3
        self.ParList.SetColumnWidth(0, column_width)
        self.ParList.SetColumnWidth(1, column_width)
        self.ParList.SetColumnWidth(2, column_width)

    def properties_set_state(self, state):
        """
        Sets the state of the properties controls.
        """

        self.Episode.Enable(state)
        self.Map.Enable(state)
        self.Seconds.Enable(state)
        self.Tools.EnableTool(windows.PAR_TOOL_REMOVE, state)

    def par_select(self, event):
        """
        Selects a par time from the list.
        """

        self.selected_index = event.GetIndex()
        self.update_properties()
        self.properties_set_state(True)

    def par_add(self, event):
        """
        Adds a new par time to the list.
        """

        self.undo_add()

        # Add a new par time.
        par = entries.ParEntry(self.patch.pars)
        par['episode'] = 0
        par['map'] = 1
        par['seconds'] = 666
        self.patch.pars.append(par)

        self.parlist_build()
        self.ParList.Select(len(self.patch.pars) - 1, True)

    def par_remove(self, event):
        """
        Removes the currently selected par time from the list.
        """

        self.undo_add()

        del self.patch.pars[self.selected_index]
        self.parlist_build()

    def update_properties(self):
        """
        Updates the property controls of the currently displayed par time.
        """

        par = self.patch.pars[self.selected_index]

        self.Episode.ChangeValue(str(par['episode']))
        self.Map.ChangeValue(str(par['map']))
        self.Seconds.ChangeValue(str(par['seconds']))

    def set_value(self, event):
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
            if value < 0:
                value = 0
            elif value > 9:
                value = 9
        elif key == 'map':
            if value < 0:
                value = 0
            elif value > 99:
                value = 99
        elif key == 'seconds':
            if value < 0:
                value = 0
        window.ChangeValue(str(value))

        self.patch.pars[self.selected_index][key] = value

        self.parlist_update_row(self.selected_index)
        self.is_modified(True)

    def undo_restore_item(self, item):
        """
        @see: EditorMixin.undo_restore_item
        """

        self.patch.pars = item
        self.parlist_build()

        self.is_modified(True)

    def undo_store_item(self):
        """
        @see: EditorMixin.undo_store_item

        Undo for this editor works by storing *all* par entries in a single undo item.
        """

        dup = []
        for par in self.patch.pars:
            dup.append(par.clone())

        return dup
