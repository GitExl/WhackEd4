"""
Mixin for common editor UI functionality.
"""

#!/usr/bin/env python
#coding=utf8

from typing import List, Dict, Optional

import wx
from wx import ListCtrl, Event, MouseEvent, ActivateEvent, CloseEvent

from whacked4 import config, utils
from whacked4.dehacked.patch import Patch
from whacked4.ui import windows


UndoItem = Dict[str, any]
WorkspaceData = Dict[str, int]


class EditorMixin(wx.MDIChildFrame):
    """
    Adds common editor window functionality to any wx.Frame object.
    """

    def __init__(self):
        self.undo: List[UndoItem] = []
        self.undo_index: int = -1

        # Stores the position of this editor window.
        self.workspace_data: WorkspaceData = {
            'x': 0,
            'y': 0,
            'width': self.GetMinWidth(),
            'height': self.GetMinHeight()
        }

        self.Bind(wx.EVT_MOVE, self.workspace_update_data)
        self.Bind(wx.EVT_SIZE, self.workspace_update_data)
        self.Bind(wx.EVT_ACTIVATE, self.activate)
        self.Bind(wx.EVT_CLOSE, self.close)

    def build(self, patch: Patch):
        """
        Called when this editor window needs to build its UI contents.
        """

        raise NotImplementedError()

    def update(self):
        """
        Called when this editor window needs to update its UI contents.
        """

        raise NotImplementedError()

    def list_autosize(self, list_control: ListCtrl):
        """
        Sizes all the columns in a ListCtrl to match the widest value in its contents
        or itself.

        @param list_control: the list control whose columns should be sized.
        """

        for i in range(list_control.GetColumnCount()):
            list_control.SetColumnWidth(i, wx.LIST_AUTOSIZE_USEHEADER)
        list_control.Layout()

    def undo_add(self):
        """
        Adds an undo item to the undo stack.
        """

        # If the undo stack has reached it's maximum size, prune off the first item.
        if len(self.undo) == config.settings['undo_size']:
            self.undo = self.undo[1:]
            self.undo_index -= 1

        # Prune the stack up to and including the current item.
        self.undo = self.undo[0:self.undo_index + 1]

        self.undo.append(self.undo_store_item())
        self.undo_index += 1

    def undo_do_undo(self):
        """
        Restores an item from the undo stack.
        """

        if self.undo_index == -1:
            return

        undo_item = self.undo[self.undo_index]
        self.undo_index -= 1
        self.undo_restore_item(undo_item)

    def undo_restore_item(self, item: UndoItem):
        """
        Called when an undo item needs to be restored.

        @param item: the item object for the editor window to restore.
        """

        raise NotImplementedError()

    def undo_store_item(self):
        """
        Called when an undo item needs to be stored.

        @return: an item object to store in the undo buffer.
        """

        raise NotImplementedError()

    def workspace_update_data(self, event: Event):
        """
        Updates this editor window's position data.
        """

        self.GetMDIParent().workspace_modified = True

        if self.IsMaximized():
            event.Skip()
            return

        position = self.GetPosition()
        size = self.GetSize()

        self.workspace_data['x'] = position[0]
        self.workspace_data['y'] = position[1]
        self.workspace_data['width'] = size[0]
        self.workspace_data['height'] = size[1]

        event.Skip()

    def enter_state(self, event: MouseEvent):
        """
        Called when the mouse enters a state label.
        """

        window = self.GetMDIParent().FindWindowById(event.GetId())
        if window is None:
            return
        window.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        window.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        window.Refresh()

    def leave_state(self, event: MouseEvent):
        """
        Called when the mouse leaves a state label.
        """

        window = self.GetMDIParent().FindWindowById(event.GetId())
        if window is None:
            return
        window.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
        window.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        window.Refresh()

    def is_modified(self, modified: bool):
        """
        Marks the currently loaded patch as modified or not.

        @param modified: True if the patch was modified.
        """

        self.GetMDIParent().set_modified(modified)

    def focus_text(self, event: MouseEvent):
        """
        Focuses an entire text control.
        """

        utils.focus_text(event, self)
        event.Skip()

    def activate(self, _: ActivateEvent):
        """
        Called when this window is activated.
        """

        if not bool(self):
            return

        self.GetMDIParent().editor_window_activate()

    def close(self, _: CloseEvent):
        """
        Called when this editor window is closed.
        """

        self.Maximize(False)
        self.GetMDIParent().editor_window_closed(self)

    def goto_state(
        self,
        state_index: int,
        filter_type: Optional[str] = None,
        filter_index: Optional[int] = None
    ):
        """
        Displays a state in the states editor, and enables a filter.

        @param state_index: the index of the state to go to.
        @param filter_type: the type of state filter to enable.
        @param filter_index: the index of the item to select in the state filter.
        """

        parent = self.GetMDIParent()
        parent.editor_window_show(windows.MAIN_TOOL_STATES)

        # Set selected state and display the state editor window.
        states_frame = parent.editor_windows[windows.MAIN_TOOL_STATES]
        states_frame.goto_state_index(
            state_index,
            filter_type=filter_type,
            filter_index=filter_index
        )
        states_frame.Raise()

    def goto_sound(self, sound_index: int):
        """
        Displays a sound in the sounds editor.

        @param sound_index: the index of the sound to go to.
        """

        parent = self.GetMDIParent()
        parent.editor_window_show(windows.MAIN_TOOL_SOUNDS)

        # Set selected state and display the state editor window.
        sounds_frame = parent.editor_windows[windows.MAIN_TOOL_SOUNDS]
        sounds_frame.goto_sound_index(sound_index)
        sounds_frame.Raise()

    def dummy(self, event: Event):
        """
        Dummy event consumer.
        """

    def before_save(self):
        """
        Called by the main window before saving the current patch.
        """
