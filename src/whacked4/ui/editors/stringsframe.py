import copy
from math import floor

import wx

from whacked4 import config
from whacked4.dehacked import patch
from whacked4.ui import editormixin, windows
from whacked4.ui.dialogs import stringdialog


class StringsFrame(editormixin.EditorMixin, windows.StringsFrameBase):
    """
    Strings editor window.
    """

    def __init__(self, parent):
        windows.StringsFrameBase.__init__(self, parent)
        editormixin.EditorMixin.__init__(self)

        self.SetIcon(wx.Icon('res/editor-strings.ico'))

        self.patch = None
        self.string_dialog = None
        self.selected_index = -1

    def build(self, new_patch):
        """
        @see: EditorMixin.build
        """

        self.patch = new_patch
        self.string_dialog = stringdialog.StringDialog(self.GetParent())

        self.stringlist_build()

    def update(self):
        """
        @see: EditorMixin.update
        """

        self.stringlist_build()

    def stringlist_build(self):
        """
        Rebuilds the entire list of strings.
        """

        self.StringList.ClearAll()

        if self.StringList.GetColumnCount() == 0:
            if self.patch.extended:
                self.StringList.InsertColumn(0, 'Name', width=floor(134 * self.GetDPIScaleFactor()))
                self.StringList.InsertColumn(1, 'String', width=floor(800 * self.GetDPIScaleFactor()))
            else:
                self.StringList.InsertColumn(0, 'Index', width=floor(42 * self.GetDPIScaleFactor()))
                self.StringList.InsertColumn(1, 'String', width=floor(800 * self.GetDPIScaleFactor()))

        for row_index, string_key in enumerate(self.patch.strings.keys()):
            if string_key not in self.patch.engine.strings:
                continue

            self.StringList.InsertItem(row_index, string_key)
            self.StringList.SetItemFont(row_index, config.FONT_MONOSPACED)

            self.stringlist_update_row(row_index, string_key)

        self.list_autosize(self.StringList)
        self.StringList.Select(0, True)

    def stringlist_update_row(self, row_index, string_key):
        """
        Updates a single row in the strings list.
        """

        string = self.patch.strings[string_key]
        self.StringList.SetItem(row_index, 1, patch.string_escape(string))

    def stringlist_resize(self, event):
        """
        Called when the string list is resized. Adjusts the list column widths to match.
        """

        if not self.StringList.GetColumnCount():
            return

        width = self.StringList.GetClientSize()[0]
        column_width = width - self.StringList.GetColumnWidth(0) - 4
        self.StringList.SetColumnWidth(1, column_width)

        event.Skip()

    def string_edit(self, event):
        """
        Show the string editing dialog to edit the selected string.
        """

        string_key = self.get_string_key_from_index(self.selected_index)
        if string_key == -1:
            return

        engine_string = self.patch.engine.strings[string_key]
        old_string = self.patch.strings[string_key]
        name = string_key

        # Display dialog.
        self.string_dialog.set_state(engine_string, old_string, self.patch.extended, name)
        self.string_dialog.ShowModal()

        if self.string_dialog.new_string is not None:
            self.undo_add()

            # Store a duplicate of the new string in the patch.
            dup = copy.copy(self.string_dialog.new_string)
            self.patch.strings[string_key] = dup

            self.stringlist_update_row(self.selected_index, string_key)
            self.update_externals(dup)
            self.is_modified(True)

    def get_string_key_from_index(self, row_index):
        """
        Returns the string key belonging to a row index.
        """

        keys = list(self.patch.engine.strings)
        if row_index < 0 or row_index >= len(keys):
            return -1

        return keys[row_index]

    def string_restore(self, event):
        """
        Restores the currently selected string to it's engine state.
        """

        string_key = self.get_string_key_from_index(self.selected_index)
        if string_key not in self.patch.engine.strings:
            return

        self.undo_add()

        dup = copy.copy(self.patch.engine.strings[string_key])
        self.patch.strings[string_key] = dup

        self.stringlist_update_row(self.selected_index, string_key)
        self.update_externals(dup)

        self.is_modified(True)

    def update_externals(self, new_string):
        """
        Updates name lists in case a relevant string was changed.
        """

        if self.patch.extended:
            return

        if len(new_string) <= 6:
            self.patch.update_string_externals(self.patch.engine.sounds, self.patch.sounds)
        if len(new_string) == 4:
            self.patch.update_string_externals(self.patch.engine.sprite_names, self.patch.sprite_names)

    def undo_restore_item(self, item):
        """
        @see: EditorMixin.undo_restore_item
        """

        string_key = self.get_string_key_from_index(item['index'])
        if string_key == -1:
            return

        self.patch.strings[string_key] = item['item']
        self.stringlist_update_row(item['index'], string_key)

        self.is_modified(True)

    def undo_store_item(self):
        """
        @see: EditorMixin.undo_store_item
        """

        string_key = self.get_string_key_from_index(self.selected_index)
        if string_key == -1:
            return

        return {
            'item': copy.deepcopy(self.patch.strings[string_key]),
            'index': self.selected_index
        }

    def string_select(self, event):
        self.selected_index = event.GetIndex()
