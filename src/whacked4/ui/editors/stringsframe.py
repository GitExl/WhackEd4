#!/usr/bin/env python
#coding=utf8

from whacked4 import config
from whacked4.dehacked import patch
from whacked4.ui import editormixin, windows
from whacked4.ui.dialogs import stringdialog
import copy
import wx


class StringsFrame(editormixin.EditorMixin, windows.StringsFrameBase):
    """
    Strings editor window.
    """

    def __init__(self, params):
        windows.StringsFrameBase.__init__(self, params)
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

        if self.patch.extended:
            if self.StringList.GetColumnCount() == 0:
                self.StringList.InsertColumn(0, 'Name', width=134)
                self.StringList.InsertColumn(1, 'String', width=800)

            string_index = 0
            for name in self.patch.strings.iterkeys():
                self.StringList.InsertStringItem(string_index, name)
                self.StringList.SetItemFont(string_index, config.FONT_MONOSPACED)

                self.stringlist_update_row(string_index)

                string_index += 1

        else:
            if self.StringList.GetColumnCount() == 0:
                self.StringList.InsertColumn(0, 'Index', width=42)
                self.StringList.InsertColumn(1, 'String', width=800)

            for string_index in range(len(self.patch.strings)):
                self.StringList.InsertStringItem(string_index, str(string_index))
                self.StringList.SetItemFont(string_index, config.FONT_MONOSPACED)

                self.stringlist_update_row(string_index)

        self.list_autosize(self.StringList)
        self.StringList.Select(0, True)

    def stringlist_update_row(self, row_index):
        """
        Updates a single row in the strings list.
        """

        string_key = self.get_string_key(row_index)
        string = self.patch.strings[string_key]

        self.StringList.SetStringItem(row_index, 1, patch.string_escape(string))

    def stringlist_resize(self, event):
        """
        Called when the string list is resized. Adjusts the list column widths to match.
        """

        width = self.StringList.GetClientSizeTuple()[0]
        column_width = width - self.StringList.GetColumnWidth(0) - 4
        self.StringList.SetColumnWidth(1, column_width)

        event.Skip()

    def string_edit(self, event):
        """
        Show the string editing dialog to edit the selected string.
        """

        string_key = self.get_string_key(self.selected_index)

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

            self.stringlist_update_row(self.selected_index)
            self.update_externals(dup)
            self.is_modified(True)

    def string_restore(self, event):
        """
        Restores the currently selected string to it's engine state.
        """

        self.undo_add()

        string_key = self.get_string_key(self.selected_index)

        dup = copy.copy(self.patch.engine.strings[string_key])
        self.patch.strings[string_key] = dup

        self.stringlist_update_row(self.selected_index)
        self.update_externals(dup)

        self.is_modified(True)

    def update_externals(self, new_string):
        """
        Updates name lists in case a relevant string was changed.
        """

        if self.patch.extended:
            return

        if len(new_string) <= 6:
            self.patch.update_string_externals(self.patch.engine.sound_names, self.patch.sound_names)
        if len(new_string) == 4:
            self.patch.update_string_externals(self.patch.engine.sprite_names, self.patch.sprite_names)

    def get_string_key(self, string_index):
        """
        Returns a valid string key for usage with a patch strings dict or list.
        """

        if self.patch.extended:
            return self.patch.strings.keys()[string_index]
        else:
            return string_index

    def undo_restore_item(self, item):
        """
        @see: EditorMixin.undo_restore_item
        """

        string_key = self.get_string_key(item['index'])
        self.patch.strings[string_key] = item['item']
        self.stringlist_update_row(item['index'])

        self.is_modified(True)

    def undo_store_item(self):
        """
        @see: EditorMixin.undo_store_item
        """

        string_key = self.get_string_key(self.selected_index)

        return {
            'item': copy.deepcopy(self.patch.strings[string_key]),
            'index': self.selected_index
        }

    def string_select(self, event):
        self.selected_index = event.GetIndex()
