"""
String editor UI.
"""

import copy
from math import floor
from typing import Optional

import wx
from wx import Window, SizeEvent, CommandEvent

from whacked4 import config, utils
from whacked4.dehacked.patch import Patch, string_escape
from whacked4.ui import editormixin, windows
from whacked4.ui.dialogs import stringdialog
from whacked4.ui.dialogs.stringdialog import StringDialog
from whacked4.ui.editormixin import UndoItem


class StringsFrame(editormixin.EditorMixin, windows.StringsFrameBase):
    """
    Strings editor window.
    """

    def __init__(self, parent: Window):
        windows.StringsFrameBase.__init__(self, parent)
        editormixin.EditorMixin.__init__(self)

        self.SetIcon(wx.Icon('res/editor-strings.png'))

        self.patch: Optional[Patch] = None
        self.string_dialog: Optional[StringDialog] = None
        self.selected_index: int = -1

    def build(self, patch: Patch):
        """
        @see: EditorMixin.build
        """

        self.patch = patch
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
            scale = utils.get_platform_dpi_scale(self)
            if self.patch.extended:
                self.StringList.InsertColumn(0, 'Name', width=floor(134 * scale))
                self.StringList.InsertColumn(1, 'String', width=floor(800 * scale))
            else:
                self.StringList.InsertColumn(0, 'Index', width=floor(42 * scale))
                self.StringList.InsertColumn(1, 'String', width=floor(800 * scale))

        for row_index, string_key in enumerate(self.patch.strings.keys()):
            if string_key not in self.patch.engine.strings:
                continue

            self.StringList.InsertItem(row_index, string_key)
            self.StringList.SetItemFont(row_index, config.FONT_MONOSPACED)

            self.stringlist_update_row(row_index, string_key)

        self.list_autosize(self.StringList)
        self.StringList.Select(0, True)

    def stringlist_update_row(self, row_index: int, string_key: str):
        """
        Updates a single row in the strings list.
        """

        string = self.patch.strings[string_key]
        self.StringList.SetItem(row_index, 1, string_escape(string))

    def stringlist_resize(self, event: SizeEvent):
        """
        Called when the string list is resized. Adjusts the list column widths to match.
        """

        if not self.StringList.GetColumnCount():
            return

        width = self.StringList.GetClientSize()[0]
        column_width = width - self.StringList.GetColumnWidth(0) - 4
        self.StringList.SetColumnWidth(1, column_width)

        event.Skip()

    def string_edit(self, event: CommandEvent):
        """
        Show the string editing dialog to edit the selected string.
        """

        string_key = self.get_string_key_from_index(self.selected_index)
        if string_key is None:
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

    def get_string_key_from_index(self, row_index: int) -> Optional[str]:
        """
        Returns the string key belonging to a row index.
        """

        keys = list(self.patch.engine.strings.keys())
        if row_index < 0 or row_index >= len(keys):
            return None

        return keys[row_index]

    def string_restore(self, event: CommandEvent):
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

    def update_externals(self, new_string: str):
        """
        Updates name lists in case a relevant string was changed.
        """

        if self.patch.extended:
            return

        # Update potential sound names from strings.
        if len(new_string) <= 6:
            for index, engine_sound in enumerate(self.patch.engine.sounds):
                if engine_sound.name in self.patch.engine.strings:
                    self.patch.sounds[index].name = self.patch.engine.strings[engine_sound.name]

        # Update potential sprite names from strings.
        if len(new_string) == 4:
            for index, engine_sprite_name in enumerate(self.patch.engine.sprite_names):
                if engine_sprite_name in self.patch.engine.strings:
                    self.patch.sprite_names[index] = self.patch.engine.strings[engine_sprite_name]

    def undo_restore_item(self, item: UndoItem):
        """
        @see: EditorMixin.undo_restore_item
        """

        string_key = self.get_string_key_from_index(item['index'])
        if string_key is None:
            return

        self.patch.strings[string_key] = item['item']
        self.stringlist_update_row(item['index'], string_key)

        self.is_modified(True)

    def undo_store_item(self) -> Optional[UndoItem]:
        """
        @see: EditorMixin.undo_store_item
        """

        string_key = self.get_string_key_from_index(self.selected_index)
        if string_key is None:
            return None

        return {
            'item': copy.deepcopy(self.patch.strings[string_key]),
            'index': self.selected_index
        }

    def string_select(self, event):
        self.selected_index = event.GetIndex()
