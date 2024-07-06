#!/usr/bin/env python
#coding=utf8
from math import floor

from whacked4 import utils
from whacked4.ui import editormixin, windows
import copy
import wx


class MiscFrame(editormixin.EditorMixin, windows.MiscFrameBase):
    """
    Misc editor window.
    """

    def __init__(self, parent):
        windows.MiscFrameBase.__init__(self, parent)
        editormixin.EditorMixin.__init__(self)

        self.SetIcon(wx.Icon('res/editor-misc.ico'))

        self.patch = None
        self.selected_index = -1
        self.data_type = None

    def build(self, patch):
        """
        @see: EditorMixin.build
        """

        self.patch = patch
        self.misclist_build()

    def update(self):
        """
        @see: EditorMixin.update
        """

        pass

    def misc_select(self, event):
        """
        Selects a new ammo entry.
        """

        self.selected_index = event.GetIndex()
        self.update_properties()

    def update_properties(self):
        """
        Updates the displayed properties of the currently selected entry.
        """

        if not self.patch:
            return

        misc_data_keys = list(self.patch.engine.misc_data.keys())
        key = misc_data_keys[self.selected_index]
        data = self.patch.engine.misc_data[key]
        value = self.patch.misc[key]

        self.Value.Disable()
        self.Value.ChangeValue('')

        self.ValueEnabled.Disable()
        self.ValueEnabled.SetValue(False)

        self.data_type = data['type']
        if data['type'] == 'boolean':
            self.ValueEnabled.Enable()
            if value == data['on']:
                self.ValueEnabled.SetValue(True)
            else:
                self.ValueEnabled.SetValue(False)

        else:
            self.Value.Enable()
            self.Value.ChangeValue(str(value))

    def misclist_build(self):
        """
        Builds the misc. data list.
        """

        self.MiscList.ClearAll()

        # Add column headers if necessary.
        if self.MiscList.GetColumnCount() == 0:
            self.MiscList.InsertColumn(0, 'Name', width=floor(76 * self.GetDPIScaleFactor()))
            self.MiscList.InsertColumn(1, 'Value', width=floor(67 * self.GetDPIScaleFactor()))

        misc_values = list(self.patch.engine.misc_data.values())
        for misc_index in range(len(misc_values)):
            misc_value = misc_values[misc_index]

            self.MiscList.InsertItem(misc_index, misc_value['name'])

            self.misclist_update_row(misc_index)

        self.list_autosize(self.MiscList)
        self.MiscList.Select(0, True)

    def misclist_update_row(self, row_index):
        """
        Updates a row in the misc list.
        """

        data_keys = list(self.patch.engine.misc_data.keys())
        data_key = data_keys[row_index]
        data = self.patch.engine.misc_data[data_key]
        value = self.patch.misc[data_key]

        self.MiscList.SetItem(row_index, 0, data['name'])

        if data['type'] == 'boolean':
            if value == data['on']:
                str_value = 'On'
            else:
                str_value = 'Off'
        else:
            str_value = str(value)

        self.MiscList.SetItem(row_index, 1, str_value)

    def misclist_resize(self, event):
        """
        Resize the misc name column as wide as possible.
        """

        if not self.MiscList.GetColumnCount():
            return

        column_width = self.MiscList.GetClientSize()[0] - 4
        self.MiscList.SetColumnWidth(0, 200)
        self.MiscList.SetColumnWidth(1, column_width - 200)

    def set_value(self, event):
        """
        Validates and sets a misc. property.
        """

        self.undo_add()

        window_id = event.GetId()
        window = self.FindWindowById(window_id)

        if self.data_type == 'int' or self.data_type == 'byte':
            value = utils.validate_numeric(window)
        elif self.data_type == 'float':
            value = utils.validate_numeric_float(window)
        else:
            value = window.GetValue()

        key_list = list(self.patch.engine.misc_data.keys())
        key = key_list[self.selected_index]

        # Clamp values to their data type range.
        if self.data_type == 'int':
            if value < -0x80000000:
                value = -0x80000000
            elif value > 0x80000000:
                value = 0x80000000
            window.ChangeValue(str(value))

        elif self.data_type == 'byte':
            if value < 0:
                value = 0
            elif value > 255:
                value = 255
            window.ChangeValue(str(value))

        self.patch.misc[key] = value

        self.is_modified(True)
        self.misclist_update_row(self.selected_index)

    def set_bool_value(self, event):
        """
        Validates and sets a misc. boolean property.
        """

        self.undo_add()

        key_list = list(self.patch.engine.misc_data.keys())
        key = key_list[self.selected_index]
        data = self.patch.engine.misc_data[key]

        if self.ValueEnabled.GetValue():
            self.patch.misc[key] = data['on']
        else:
            self.patch.misc[key] = data['off']

        self.is_modified(True)
        self.misclist_update_row(self.selected_index)

    def misc_action(self, event):
        """
        Performs the default action for a misc. item.
        """

        key_list = list(self.patch.engine.misc_data.keys())
        key = key_list[self.selected_index]
        data = self.patch.engine.misc_data[key]

        # Booleans are toggled.
        if data['type'] == 'boolean':
            self.undo_add()

            value = self.patch.misc[key]
            if value == data['on']:
                self.patch.misc[key] = data['off']
            elif value == data['off']:
                self.patch.misc[key] = data['on']

            self.is_modified(True)
            self.update_properties()
            self.misclist_update_row(self.selected_index)

        # Other values shift focus to the value to edit.
        else:
            self.Value.SetFocus()
            self.Value.SetSelection(-1, -1)


    def restore(self, event):
        """
        Restore the selected misc item to it's engine state.
        """

        self.undo_add()

        key_list = list(self.patch.engine.misc_data.keys())
        key = key_list[self.selected_index]
        self.patch.misc[key] = copy.copy(self.patch.engine.misc[key])

        self.misclist_update_row(self.selected_index)
        self.update_properties()

    def undo_restore_item(self, item):
        """
        @see: EditorMixin.undo_restore_item
        """

        self.patch.misc[item['key']] = item['item']

        self.misclist_update_row(item['index'])
        self.update_properties()

        self.is_modified(True)

    def undo_store_item(self):
        """
        @see: EditorMixin.undo_store_item
        """

        key_list = list(self.patch.engine.misc_data.keys())
        key = key_list[self.selected_index]

        return {
            'item': self.patch.misc[key],
            'index': self.selected_index,
            'key': key
        }
