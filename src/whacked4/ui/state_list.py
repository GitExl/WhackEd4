"""
Custom state list control.
"""

from enum import IntEnum
from math import floor
from typing import Optional, List, Tuple, Generator

import sys, wx
from wx import Colour, ListEvent, PostEvent, SizeEvent
from wx.lib.newevent import NewEvent

from whacked4 import config, utils
from whacked4.dehacked.entry import Entry
from whacked4.dehacked.patch import Patch
from whacked4.dehacked.statequery.result import StateQueryResult


FRAMEFLAG_LIT = 0x8000

ITEM_COLORS: List[Colour] = [
    wx.Colour(red=255, green=0, blue=0),
    wx.Colour(red=255, green=255, blue=255)
]


StateListEvent, EVT_STATE_LIST_EVENT = NewEvent()


class StateColumn(IntEnum):
    """
    State column index.
    """

    INDEX = 0
    NAME = 1
    SPRITE = 2
    FRAME = 3
    LIT = 4
    NEXT = 5
    DURATION = 6
    ACTION = 7
    PARAMETERS = 8


class StateList(wx.ListCtrl):
    """
    Custom statelist ListCtrl wrapper.
    """

    def __init__(
        self,
        parent=None,
        id=wx.ID_ANY,
        pos=wx.DefaultPosition,
        size=wx.DefaultSize,
        style=0
    ):
        super().__init__(parent, id, pos, size, style | wx.LC_NO_SORT_HEADER | wx.LC_REPORT)

        self.patch: Optional[Patch] = None

        self.Bind(wx.EVT_SIZE, self.resize)

        self.selected: List[int] = []
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.update_selection)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.update_selection)
        self.Bind(wx.EVT_LIST_ITEM_FOCUSED, self.update_selection)

        self.item_colors: List[Colour] = []
        self.mix_state_colours()

        self.query_result: Optional[StateQueryResult] = None

    def mix_state_colours(self):
        """
        Mix the state colors with system colors.
        """

        background_color = self.GetBackgroundColour()
        for color in ITEM_COLORS:
            self.item_colors.append(utils.mix_colors(color, background_color, 0.95))

    def resize(self, event: SizeEvent):
        """
        Dialog resize event handler.

        :param _:
        """

        columns_width = 0
        for column_index in range(0, self.GetColumnCount()):
            if column_index == StateColumn.PARAMETERS:
                continue
            columns_width += self.GetColumnWidth(column_index)

        width = self.GetClientSize()[0] - columns_width - 4
        if self.GetColumnCount() <= StateColumn.PARAMETERS:
            return
        current_width = self.GetColumnWidth(StateColumn.PARAMETERS)
        if width != current_width:
            self.SetColumnWidth(StateColumn.PARAMETERS, width)

        event.Skip()

    def update_item_attributes(self):
        """
        Updates the attributes of all list items.
        """
        self.Freeze()

        colour_index = 0
        previous_sprite = 0
        list_index = 0
        for _, _, state in self.query_result:
            if state['sprite'] != previous_sprite:
                colour_index += 1
                if colour_index == len(self.item_colors):
                    colour_index = 0

            self.SetItemBackgroundColour(list_index, self.item_colors[colour_index])

            list_index += 1
            previous_sprite = state['sprite']

        self.Thaw()

    def build(self):
        """
        Rebuild dialog contents.
        """

        self.Freeze()
        self.ClearAll()

        if self.GetColumnCount() == 0:
            scale = utils.get_platform_dpi_scale(self)
            self.InsertColumn(StateColumn.INDEX, '', width=floor(47 * scale))
            self.InsertColumn(StateColumn.NAME, 'Name', width=floor(59 * scale))
            self.InsertColumn(StateColumn.SPRITE, 'Spr', width=floor(42 * scale))
            self.InsertColumn(StateColumn.FRAME, 'Frm', width=floor(42 * scale))
            self.InsertColumn(StateColumn.LIT, 'Lit', width=floor(27 * scale))
            self.InsertColumn(StateColumn.NEXT, 'Next', width=floor(50 * scale))
            self.InsertColumn(StateColumn.DURATION, 'Dur', width=floor(50 * scale))
            self.InsertColumn(StateColumn.ACTION, 'Action', width=floor(160 * scale))
            self.InsertColumn(StateColumn.PARAMETERS, 'Parameters', width=floor(107 * scale))

        for item_index, state_index, state in self.query_result:
            self.InsertItem(item_index, '')
            self.update_row(item_index, state_index, state)
            self.SetItemFont(item_index, config.FONT_MONOSPACED)

        self.update_item_attributes()

        self.select_first_valid_state()
        self.Thaw()

    def update_row(self, item_index, state_index, state):
        """
        Update a single state row.

        :param item_index:
        :param state_index:
        :param state:


        """
        action = self.patch.engine.actions.get_by_key(state['action'])

        if action is not None:
            action_name = action.name
            parameters = action.get_state_parameter_properties(state)
        else:
            action_name = ''
            parameters = (str(state['unused1']), str(state['unused2']))

        # Use asterisk on macOS because of system theme causing the black square to be hard to see AND off-center
        # Same off-center problem with emoji, attempted it.
        lit = ('*' if sys.platform == 'darwin' else '◾') if state['spriteFrame'] & FRAMEFLAG_LIT else ''
        frame_name = str(state['spriteFrame'] & ~FRAMEFLAG_LIT)
        parameters_text = ', '.join(parameters)

        self.SetItemText(item_index, str(state_index))
        self.SetItem(item_index, StateColumn.NAME, self.patch.get_state_name(state_index))
        self.SetItem(item_index, StateColumn.SPRITE, str(state['sprite']))
        self.SetItem(item_index, StateColumn.FRAME, frame_name)
        self.SetItem(item_index, StateColumn.LIT, lit)
        self.SetItem(item_index, StateColumn.NEXT, str(state['nextState']))
        self.SetItem(item_index, StateColumn.DURATION, str(state['duration']))
        self.SetItem(item_index, StateColumn.ACTION, action_name)
        self.SetItem(item_index, StateColumn.PARAMETERS, parameters_text)

    def set_patch(self, patch: Patch):
        """
        Set the patch referenced by this dialog.

        :param patch:
        """
        self.patch = patch
        self.query_result = None

    def set_state_query_result(self, state_query_result: StateQueryResult):
        """
        Set a state query result.

        :param state_query_result:
        """
        self.query_result = state_query_result
        self.build()

    def select_first_valid_state(self):
        """
        Selects the first state in the list that is valid.
        """

        if self.query_result is None or len(self.query_result) == 0:
            return

        state = self.query_result.get_state_for_item_index(0)
        if state is not None and state['sprite'] != 0:
            self.set_selected([0])
        else:
            self.set_selected([1])

    def refresh_selected_rows(self):
        """
        Refreshes the contents of the selected rows.
        """

        for item_index in self.selected:
            state_index = self.query_result.get_state_index_for_item_index(item_index)
            state = self.query_result.get_state_for_item_index(item_index)
            if state is not None:
                self.update_row(item_index, state_index, state)

    def update_selection(self, _: ListEvent):
        """
        Update the selected state list.

        :param _:
        """

        # Check if the widget is still valid to avoid errors during shutdown
        if not self:
            return

        self.selected.clear()

        item = self.GetFirstSelected()
        while item != -1:
            self.selected.append(item)
            item = self.GetNextSelected(item)

        PostEvent(self, StateListEvent(selection=self.selected))

    def get_selected(self) -> List[int]:
        """
        Returns the selected states.
        """

        return self.selected

    def iterate_selected(self) -> Generator[tuple[int, int, Entry]]:
        """
        Iterator for selected states.
        """

        for item_index in self.selected:
            state_index = self.query_result.get_state_index_for_item_index(item_index)
            state = self.query_result.get_state_for_item_index(item_index)

            if state is not None:
                yield item_index, state_index, state

    def get_selected_count(self) -> int:
        """
        Return the number of selected states.
        """

        return len(self.selected)

    def get_first_selected(self) -> int:
        """
        Returns the index of the first selected state.
        """

        if len(self.selected) > 0:
            return self.selected[0]
        return -1

    def get_last_selected(self) -> int:
        """
        Returns the index of the last selected state.
        """

        if len(self.selected) > 0:
            return self.selected[-1]
        return -1

    def set_selected(self, selected: List[int]):
        """
        Set the list of selected states.

        :param selected:
        """

        self.clear_selection()
        for index in selected:
            self.Select(index, 1)

    def clear_selection(self):
        """
        Clear the state selection.
        """

        item = self.GetFirstSelected()
        while item != -1:
            self.Select(item, 0)
            item = self.GetNextSelected(item)
