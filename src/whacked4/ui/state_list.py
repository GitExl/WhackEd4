from enum import IntEnum
from typing import Optional, List, Tuple

import wx
from wx import ItemAttr, Colour, ListEvent, PostEvent, SizeEvent
from wx.lib.newevent import NewEvent

from whacked4 import config, utils
from whacked4.dehacked.action import Action
from whacked4.dehacked.entry import Entry
from whacked4.dehacked.patch import Patch
from whacked4.dehacked.statequery.result import StateQueryResult


FRAMEFLAG_LIT = 0x8000

ITEM_COLORS = [
    wx.Colour(red=255, green=0, blue=0),
    wx.Colour(red=255, green=255, blue=255)
]


StateListEvent, EVT_STATE_LIST_EVENT = NewEvent()


class StateColumn(IntEnum):
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

    def __init__(self, parent=None, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        super().__init__(parent, id, pos, size, style | wx.LC_NO_SORT_HEADER | wx.LC_REPORT)

        self.patch: Optional[Patch] = None

        self.Bind(wx.EVT_SIZE, self.resize)

        self.selected: List[int] = []
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.update_selection)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.update_selection)
        self.Bind(wx.EVT_LIST_ITEM_FOCUSED, self.update_selection)

        self.item_colors: List[Colour] = []
        self.mix_state_colours()

        self.state_query_result: Optional[StateQueryResult] = None

    def mix_state_colours(self):
        background_color = self.GetBackgroundColour()
        for color in ITEM_COLORS:
            self.item_colors.append(utils.mix_colors(color, background_color, 0.95))

    def resize(self, event: SizeEvent):
        columns_width = 0
        for column_index in range(0, self.GetColumnCount()):
            if column_index == StateColumn.PARAMETERS:
                continue
            columns_width += self.GetColumnWidth(column_index)

        width = self.GetClientSize()[0] - columns_width - 4
        current_width = self.GetColumnWidth(StateColumn.PARAMETERS)
        if width != current_width:
            self.SetColumnWidth(StateColumn.PARAMETERS, width)

    def update_item_attributes(self):
        self.Freeze()

        colour_index = 0
        previous_sprite = 0
        list_index = 0
        for item_index, state_index, state in self.state_query_result:
            if state['sprite'] != previous_sprite:
                colour_index += 1
                if colour_index == len(self.item_colors):
                    colour_index = 0

            self.SetItemBackgroundColour(list_index, self.item_colors[colour_index])

            list_index += 1
            previous_sprite = state['sprite']

        self.Thaw()

    def build(self):
        self.Freeze()
        self.ClearAll()

        if self.GetColumnCount() == 0:
            self.InsertColumn(StateColumn.INDEX, '', width=47)
            self.InsertColumn(StateColumn.NAME, 'Name', width=59)
            self.InsertColumn(StateColumn.SPRITE, 'Spr', width=42)
            self.InsertColumn(StateColumn.FRAME, 'Frm', width=42)
            self.InsertColumn(StateColumn.LIT, 'Lit', width=27)
            self.InsertColumn(StateColumn.NEXT, 'Next', width=50)
            self.InsertColumn(StateColumn.DURATION, 'Dur', width=47)
            self.InsertColumn(StateColumn.ACTION, 'Action', width=160)
            self.InsertColumn(StateColumn.PARAMETERS, 'Parameters', width=107)

        for item_index, state_index, state in self.state_query_result:
            self.InsertItem(item_index, '')
            self.update_row(item_index, state_index, state)
            self.SetItemFont(item_index, config.FONT_MONOSPACED)

        self.update_item_attributes()

        self.select_first_valid_state()
        self.Thaw()

    def update_row(self, item_index, state_index, state):
        action = self.patch.engine.actions.get(state['action'], None)

        if action is not None:
            action_name = action.name
            parameters = action.get_state_parameter_properties(state)
        else:
            action_name = ''
            parameters = (str(state['unused1']), str(state['unused2']))

        parameters_text = ', '.join(parameters)

        self.SetItemText(item_index, str(state_index))
        self.SetItem(item_index, StateColumn.NAME, self.patch.get_state_name(state_index))
        self.SetItem(item_index, StateColumn.SPRITE, str(state['sprite']))
        self.SetItem(item_index, StateColumn.FRAME, str(state['spriteFrame'] & ~FRAMEFLAG_LIT))
        self.SetItem(item_index, StateColumn.LIT, '◾' if state['spriteFrame'] & FRAMEFLAG_LIT else '')
        self.SetItem(item_index, StateColumn.NEXT, str(state['nextState']))
        self.SetItem(item_index, StateColumn.DURATION, str(state['duration']))
        self.SetItem(item_index, StateColumn.ACTION, action_name)
        self.SetItem(item_index, StateColumn.PARAMETERS, parameters_text)

    def set_patch(self, patch: Patch):
        self.patch = patch
        if self.state_query_result is not None:
            self.build()

    def set_state_query_result(self, state_query_result: StateQueryResult):
        self.state_query_result = state_query_result
        self.build()

    def select_first_valid_state(self):
        if self.state_query_result is None or not len(self.state_query_result):
            return

        state = self.state_query_result.get_state_for_item_index(0)
        if state['sprite'] != 0:
            self.set_selected([0])
        else:
            self.set_selected([1])

    def refresh_selected_rows(self):
        for item_index in self.selected:
            state_index = self.state_query_result.get_state_index_for_item_index(item_index)
            state = self.state_query_result.get_state_for_item_index(item_index)
            self.update_row(item_index, state_index, state)

    def update_selection(self, event: ListEvent):
        self.selected.clear()

        item = self.GetFirstSelected()
        while item != -1:
            self.selected.append(item)
            item = self.GetNextSelected(item)

        PostEvent(self, StateListEvent(selection=self.selected))

    def get_selected(self) -> List[int]:
        return self.selected

    def iterate_selected(self) -> Tuple[int, int, Entry]:
        for item_index in self.selected:
            state_index = self.state_query_result.get_state_index_for_item_index(item_index)
            state = self.state_query_result.get_state_for_item_index(item_index)

            yield item_index, state_index, state

    def get_selected_count(self) -> int:
        return len(self.selected)

    def get_first_selected(self) -> int:
        if len(self.selected):
            return self.selected[0]
        return -1

    def get_last_selected(self) -> int:
        if len(self.selected):
            return self.selected[-1]
        return -1

    def set_selected(self, selected: List[int]):
        self.clear_selection()
        for index in selected:
            self.Select(index, 1)

    def clear_selection(self):
        item = self.GetFirstSelected()
        while item != -1:
            self.Select(item, 0)
            item = self.GetNextSelected(item)
