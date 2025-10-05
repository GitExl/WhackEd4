"""
State editing UI.
"""

import sys

from collections import OrderedDict
from typing import Dict, Optional, List, Tuple

import wx
from wx import Control, CommandEvent, KeyEvent, ListEvent, MenuEvent, SpinEvent

from whacked4 import config, utils
from whacked4.dehacked.action import Action
from whacked4.dehacked.entry import Entry
from whacked4.dehacked.patch import Patch
from whacked4.dehacked.statequery.query import StateFilterQuery
from whacked4.dehacked.statequery.stateindexsort import StateIndexSort
from whacked4.dehacked.statequery.thingfilter import ThingStateFilter
from whacked4.dehacked.statequery.unusedfilter import UnusedStateFilter
from whacked4.dehacked.statequery.weaponfilter import WeaponStateFilter
from whacked4.doom.wadlist import WADList
from whacked4.ui import editormixin, windows
from whacked4.ui.dialogs import spritesdialog, statepreviewdialog
from whacked4.ui.dialogs.spritesdialog import SpritesDialog
from whacked4.ui.dialogs.statepreviewdialog import StatePreviewDialog
from whacked4.ui.editormixin import UndoItem
from whacked4.ui.state_list import EVT_STATE_LIST_EVENT


FILTER_TYPE_NONE = 0
FILTER_TYPE_UNUSED = 1
FILTER_TYPE_THING = 2
FILTER_TYPE_WEAPON = 3


class StatesFrame(editormixin.EditorMixin, windows.StatesFrameBase):
    """
    States editor window.
    """

    # Maps window ids to state property keys.
    PROPS_STATE: Dict[int, str] = {
        windows.STATES_DURATION: 'duration',
        windows.STATES_NEXT: 'nextState',
        windows.STATES_SPRITE: 'sprite',
        windows.STATES_UNUSED1: 'unused1',
        windows.STATES_UNUSED2: 'unused2',
        windows.STATES_ARG1: 'arg1',
        windows.STATES_ARG2: 'arg2',
        windows.STATES_ARG3: 'arg3',
        windows.STATES_ARG4: 'arg4',
        windows.STATES_ARG5: 'arg5',
        windows.STATES_ARG6: 'arg6',
        windows.STATES_ARG7: 'arg7',
        windows.STATES_ARG8: 'arg8',
        windows.STATES_ARG9: 'arg9'
    }

    # Window ids grouped by state parameter value.
    UNUSED_IDS: List[Tuple[int, int]] = [
        (windows.STATES_LABEL_UNUSED1, windows.STATES_UNUSED1),
        (windows.STATES_LABEL_UNUSED2, windows.STATES_UNUSED2),
    ]
    ARG_IDS: List[Tuple[int, int]] = [
        (windows.STATES_LABEL_ARG1, windows.STATES_ARG1),
        (windows.STATES_LABEL_ARG2, windows.STATES_ARG2),
        (windows.STATES_LABEL_ARG3, windows.STATES_ARG3),
        (windows.STATES_LABEL_ARG4, windows.STATES_ARG4),
        (windows.STATES_LABEL_ARG5, windows.STATES_ARG5),
        (windows.STATES_LABEL_ARG6, windows.STATES_ARG6),
        (windows.STATES_LABEL_ARG7, windows.STATES_ARG7),
        (windows.STATES_LABEL_ARG8, windows.STATES_ARG8),
        (windows.STATES_LABEL_ARG9, windows.STATES_ARG9),
    ]

    # Doom lit flag. Frame indices with this flag set are always lit by Doom's rendering engine.
    FRAMEFLAG_LIT = 0x8000

    def __init__(self, parent):
        windows.StatesFrameBase.__init__(self, parent)
        editormixin.EditorMixin.__init__(self)
        self._adjust_mac_ui()

        self.SetIcon(wx.Icon('res/editor-states.png'))

        # A list of all tool windows for simple mass operations.
        self.windows_tools: List[Control] = [
            self.SpriteIndex,
            self.SpriteSelect,
            self.FrameIndex,
            self.FrameIndexSpinner,
            self.AlwaysLit,
            self.NextStateIndex,
            self.Duration,
            self.Action,
            self.Unused1,
            self.Unused2,
            self.Arg1,
            self.Arg2,
            self.Arg3,
            self.Arg4,
            self.Arg5,
            self.Arg6,
            self.Arg7,
            self.Arg8,
            self.Arg9,
            self.Restore,
            self.NextStateName,
            self.SpriteName
        ]

        self.patch: Optional[Patch] = None
        self.pwads: Optional[WADList] = None
        self.clipboard: Optional[Entry] = None
        self.sprites_dialog: Optional[SpritesDialog] = None
        self.preview_dialog: Optional[StatePreviewDialog] = None

        self.filters: List[Dict] = []

        self.SpriteName.SetFont(config.FONT_MONOSPACED_BOLD)
        self.NextStateName.SetFont(config.FONT_MONOSPACED_BOLD)

        self.Bind(wx.EVT_CHAR_HOOK, self.state_key)

        self.StateList.Bind(EVT_STATE_LIST_EVENT, self.statelist_event)
        self.StateList.Bind(wx.EVT_KEY_DOWN, self.statelist_key_down)

    def build(self, patch):
        """
        @see: EditorMixin.build
        """

        self.patch = patch
        self.StateList.set_patch(patch)
        self.pwads = self.GetMDIParent().pwads
        self.clipboard = None

        self.sprites_dialog = spritesdialog.SpritesDialog(self)
        self.preview_dialog = statepreviewdialog.StatePreviewDialog(self)

        # Setup sprite preview control.
        self.SpritePreview.set_source(self.pwads)
        self.SpritePreview.set_baseline_factor(0.85)
        self.SpritePreview.set_scale(2)

        # Initialize filter.
        self.build_filterlist()
        self.build_action_list()

        self.Filter.Select(0)
        self.filter_update(0)

    def update(self):
        """
        @see: EditorMixin.update
        """

        self.pwads = self.GetMDIParent().pwads

        self.sprites_dialog.update(self.pwads)
        self.preview_dialog.update(self.pwads)

        self.SpritePreview.set_source(self.pwads)
        self.update_sprite_preview()

    def undo_restore_item(self, item: UndoItem):
        """
        @see: EditorMixin.undo_restore_item
        """

        for state_index, state in item.items():
            self.patch.states[state_index] = state

            # Restore all state indices in the undo item.
            if self.StateList.query_result.contains_state_index(state_index):
                list_index = self.StateList.query_result.get_item_index_for_state_index(state_index)
                self.StateList.update_row(list_index, state_index, state)

        self.StateList.update_item_attributes()

        self.update_properties()
        self.update_sprite_preview()

        self.is_modified(True)

    def undo_store_item(self) -> UndoItem:
        """
        @see: EditorMixin.undo_store_item
        """

        # Store all currently selected states.
        items = OrderedDict()
        for _, state_index, state in self.StateList.iterate_selected():
            items[state_index] = state.clone()

        return items

    def edit_copy(self):
        """
        Copies all currently selected states to the clipboard.

        The states are stored in sequence, without non-selected states in between.
        """

        self.clipboard = []

        for _, _, state in self.StateList.iterate_selected():
            dup = state.clone()
            self.clipboard.append(dup)

    def edit_paste(self):
        """
        Pastes the current clipboard, starting at the first selected state.
        """

        if self.clipboard is None:
            return
        if self.StateList.get_selected_count() == 0:
            return

        # Do not paste over state 0.
        list_index = self.StateList.get_first_selected()
        state_index = self.StateList.query_result.get_state_index_for_item_index(list_index)
        if state_index == 0:
            return

        self.undo_add()

        for state in self.clipboard:
            # Ignore states that are not currently visible because of filters.
            if list_index in self.StateList.get_selected():
                dup = state.clone()
                state_index = self.StateList.query_result.get_state_index_for_item_index(list_index)
                self.patch.states[state_index] = dup
                self.StateList.update_row(list_index, state_index, state)

            list_index += 1
            if list_index >= len(self.patch.states):
                break

        self.update_properties()
        self.StateList.update_item_attributes()
        self.is_modified(True)

    def tools_set_state(self, enabled: bool):
        """
        Sets the state of all tool controls.
        """

        for window in self.windows_tools:
            window.Enable(enabled)

    def state_restore(self, event: CommandEvent):
        """
        Restores all currently selected states to the way they are in the
        engine configuration.
        """

        self.undo_add()

        for item_index, state_index, _ in self.StateList.iterate_selected():
            self.patch.states[state_index] = self.patch.engine.states[state_index].clone()
            self.StateList.update_row(item_index, state_index, self.patch.states[state_index])

        self.update_properties()
        self.StateList.update_item_attributes()
        self.is_modified(True)

    def state_link(self, event: KeyEvent):
        """
        Connects the currently selected state's next state property to the state being
        clicked, while the alt key is held down.
        """

        # Set the current state's next state if the alt key is held down.
        connect = wx.GetKeyState(wx.WXK_ALT)
        if connect:
            x = event.GetX()
            y = event.GetY()
            list_index = self.StateList.HitTest(wx.Point(x, y))[0]
            if list_index == wx.NOT_FOUND:
                return

            state_index = self.StateList.query_result.get_state_index_for_item_index(list_index)
            self.NextStateIndex.ChangeValue(str(state_index))
            self.set_selected_property('nextState', state_index)
            self.StateList.refresh_selected_rows()

        else:
            event.Skip()

    def build_filterlist(self):
        """
        Build the list of available filters.
        """

        self.filters = []

        # Add common filters first.
        self.filters.append({
            'name': '<none>',
            'type': FILTER_TYPE_NONE,
            'index': -1
        })
        self.filters.append({
            'name': 'Unused',
            'type': FILTER_TYPE_UNUSED,
            'index': -1
        })

        # Add thing state filters.
        for index, thing in enumerate(self.patch.things):
            self.filters.append({
                'name': thing.name,
                'type': FILTER_TYPE_THING,
                'index': index
            })

        # Add weapon state filters.
        for index, weapon in enumerate(self.patch.weapons):
            self.filters.append({
                'name': weapon.name,
                'type': FILTER_TYPE_WEAPON,
                'index': index
            })

        list_items = []
        for filter_data in self.filters:
            list_items.append(filter_data['name'])
        self.Filter.SetItems(list_items)

    def update_filter_list(self):
        """
        Refreshes the filter list with the current filter selection.
        """

        selected = self.Filter.GetSelection()
        self.build_filterlist()
        if selected != -1:
            self.Filter.Select(selected)
        else:
            self.Filter.Select(0)

    def build_action_list(self):
        """
        Builds the list of available state actions.
        """

        action_items = []

        for action in self.patch.engine.actions.values():
            action_items.append(action.name)

        self.Action.SetItems(action_items)

    def filter_update(self, index: int):
        """
        Updates the current state filter and rebuilds the state list accordingly.
        """

        filter_data = self.filters[index]

        state_query = StateFilterQuery(self.patch)
        state_query.sort(StateIndexSort(self.patch))

        if filter_data['type'] == FILTER_TYPE_THING:
            thing = self.patch.things[filter_data['index']]
            state_query.filter(ThingStateFilter(self.patch, thing))
        elif filter_data['type'] == FILTER_TYPE_WEAPON:
            weapon = self.patch.weapons[filter_data['index']]
            state_query.filter(WeaponStateFilter(self.patch, weapon))
        elif filter_data['type'] == FILTER_TYPE_UNUSED:
            state_query.filter(UnusedStateFilter(self.patch))

        state_query_result = state_query.execute()
        self.StateList.clear_selection()
        self.StateList.set_state_query_result(state_query_result)

        # Select first non-0 sprite state.
        if len(state_query_result):
            self.StateList.select_first_valid_state()
        else:
            self.update_properties()

    def set_selected_property(self, key: str, value: any):
        """
        Sets a property of all currently selected states.

        @param key: the state property key to set.
        @param value: the new value of the state property.
        """

        self.undo_add()

        for item_index, state_index, state in self.StateList.iterate_selected():
            if state_index == 0:
                continue

            state = self.StateList.query_result.get_state_for_item_index(item_index)
            if state is not None:
                state[key] = value

        self.is_modified(True)

    def update_properties(self):
        """
        Updates the tool controls with the properties of the currently selected state(s).
        """

        if not self.patch:
            return

        # If only one state is selected, fill the property controls with that state's data.
        if self.StateList.get_selected_count() == 1:
            first_selected = self.StateList.get_first_selected()
            state = self.StateList.query_result.get_state_for_item_index(first_selected)
            if state is None:
                return

            state_index = self.StateList.query_result.get_state_index_for_item_index(first_selected)

            if state_index == 0:
                sprite_name = '-'
            else:
                sprite_name = self.patch.get_sprite_name(state['sprite'])
            sprite_frame = state['spriteFrame'] & ~self.FRAMEFLAG_LIT

            self.SpriteIndex.ChangeValue(str(state['sprite']))
            self.SpriteName.SetLabel(sprite_name)
            self.FrameIndex.ChangeValue(str(sprite_frame))
            self.FrameIndexSpinner.SetValue(sprite_frame)
            self.NextStateIndex.ChangeValue(str(state['nextState']))
            self.NextStateName.SetLabel(self.patch.get_state_name(state['nextState']))
            self.Duration.ChangeValue(str(state['duration']))
            self.Unused1.ChangeValue(str(state['unused1']))
            self.Unused2.ChangeValue(str(state['unused2']))

            if 'arg1' in state:
                self.Arg1.ChangeValue(str(state['arg1']))
            if 'arg2' in state:
                self.Arg2.ChangeValue(str(state['arg2']))
            if 'arg3' in state:
                self.Arg3.ChangeValue(str(state['arg3']))
            if 'arg4' in state:
                self.Arg4.ChangeValue(str(state['arg4']))
            if 'arg5' in state:
                self.Arg5.ChangeValue(str(state['arg5']))
            if 'arg6' in state:
                self.Arg6.ChangeValue(str(state['arg6']))
            if 'arg7' in state:
                self.Arg7.ChangeValue(str(state['arg7']))
            if 'arg8' in state:
                self.Arg8.ChangeValue(str(state['arg8']))
            if 'arg9' in state:
                self.Arg9.ChangeValue(str(state['arg9']))

            self.set_selected_action(state['action'])

            if state['spriteFrame'] & self.FRAMEFLAG_LIT != 0:
                self.AlwaysLit.SetValue(True)
            else:
                self.AlwaysLit.SetValue(False)

            # Do not allow state 0 to be edited.
            if state_index == 0:
                self.tools_set_state(False)
            else:
                self.tools_set_state(True)

            # For non-extended patches, do not allow editing an action on a state that has none.
            if not self.patch.engine.extended:
                engine_action_key = self.patch.engine.states[state_index]['action']
                if engine_action_key == '0':
                    self.Action.Disable()
                else:
                    self.Action.Enable()

        # If multiple states are selected, empty out all properties.
        else:
            self.SpriteIndex.ChangeValue('')
            self.SpriteName.SetLabel('')
            self.FrameIndex.ChangeValue('')
            self.NextStateIndex.ChangeValue('')
            self.NextStateName.SetLabel('')
            self.Duration.ChangeValue('')
            self.Action.Select(0)
            self.AlwaysLit.SetValue(False)
            self.Action.Enable()
            self.tools_set_state(True)
            self.Unused1.ChangeValue('')
            self.Unused2.ChangeValue('')
            self.Arg1.ChangeValue('')
            self.Arg2.ChangeValue('')
            self.Arg3.ChangeValue('')
            self.Arg4.ChangeValue('')
            self.Arg5.ChangeValue('')
            self.Arg6.ChangeValue('')
            self.Arg7.ChangeValue('')
            self.Arg8.ChangeValue('')
            self.Arg9.ChangeValue('')

            self.set_param_visibility('')

        if not self.StateList.get_selected_count():
            self.tools_set_state(False)

        self.update_sprite_preview()

    def set_param_visibility(self, action_key: str):
        """
        Sets the visibility of action parameters for the currently selected states.
        """

        if action_key in self.patch.engine.actions:
            action = self.patch.engine.actions[action_key]
        else:
            action = None

        if action is not None:
            self.Action.SetToolTip(action.description)

        arg_count = get_action_param_counts(action)

        # Unused parameters.
        for index, unused_id in enumerate(StatesFrame.UNUSED_IDS):
            label = self.FindWindowById(unused_id[0])
            text = self.FindWindowById(unused_id[1])

            if (action is not None) and (index < len(action.unused)):
                label.SetLabel(action.unused[index].name)
                text.SetToolTip(action.unused[index].description)
            else:
                label.SetLabel(f'Unused {index + 1}')
                text.SetToolTip('')

        # Arg0-9 parameters.
        for index, arg_id in enumerate(StatesFrame.ARG_IDS):
            label = self.FindWindowById(arg_id[0])
            text = self.FindWindowById(arg_id[1])

            if index < arg_count:
                label.SetLabel(action.arguments[index].name)
                label.Show()

                text.Show()
                text.SetToolTip(action.arguments[index].description)
            else:
                label.Hide()
                text.Hide()

    def update_sprite_preview(self):
        """
        Updates the sprite preview control with the currently selected state's sprite.
        """

        if self.StateList.get_selected_count() == 1:
            first_selected = self.StateList.get_first_selected()
            state = self.StateList.query_result.get_state_for_item_index(first_selected)
            if state is not None:
                state_query_result = self.StateList.query_result
                state_index = state_query_result.get_state_index_for_item_index(first_selected)

                # Find a valid sprite name and frame index.
                if state_index != 0:
                    sprite_index = state['sprite']
                    if sprite_index != '':
                        sprite_index = int(sprite_index)
                        sprite_name = self.patch.get_sprite_name(sprite_index)

                        sprite_frame = state['spriteFrame'] & ~self.FRAMEFLAG_LIT
                        if sprite_frame != '':
                            sprite_frame = int(sprite_frame)
                        else:
                            sprite_frame = 0

                        self.SpritePreview.show_sprite(sprite_name, sprite_frame)
                        return

        self.SpritePreview.clear()

    def statelist_key_down(self, event: KeyEvent):
        """
        Handle key presses for the states list.
        """

        if event.GetKeyCode() == 76 and event.ShiftDown():
            self.link_selected_states(True)
        elif event.GetKeyCode() == 76:
            self.link_selected_states(False)
        else:
            event.Skip()

    def select_sprite(self, event: CommandEvent):
        """
        Shows the sprite select dialog to replace the currently selected state's sprites.
        """

        # Only use the first selected state's sprite as the default selected value.
        sprite_index = 0
        frame_index = 0
        if self.StateList.get_selected_count() == 1:
            sprite_index = int(self.SpriteIndex.GetValue())
            frame_index = int(self.FrameIndex.GetValue())

        elif self.StateList.get_selected_count() > 1:
            first_selected = self.StateList.get_first_selected()
            state = self.StateList.query_result.get_state_for_item_index(first_selected)
            if state is not None:
                sprite_index = state['sprite']
                frame_index = None

        self.sprites_dialog.set_state(
            self.patch,
            self.pwads,
            sprite_index=sprite_index,
            frame_index=frame_index
        )
        self.sprites_dialog.ShowModal()

        if self.sprites_dialog.selected_sprite != -1:
            sprite_index = self.sprites_dialog.selected_sprite
            frame_index = self.sprites_dialog.selected_frame

            self.SpriteIndex.SetValue(str(sprite_index))

            # Change the frame index if it was altered.
            if frame_index != -1:
                self.FrameIndex.ChangeValue(str(frame_index))

                # Update sprite frames separately to mix in lit flag.
                for list_index in self.StateList.get_selected():
                    state = self.StateList.query_result.get_state_for_item_index(list_index)
                    if state is not None:
                        is_lit_flag = state['spriteFrame'] & self.FRAMEFLAG_LIT
                        state['spriteFrame'] = frame_index | is_lit_flag

            self.StateList.refresh_selected_rows()
            self.StateList.update_item_attributes()
            self.update_sprite_preview()

    def set_value(self, event: CommandEvent):
        """
        Validates and sets a property of all currently selected states.
        """

        window_id = event.GetId()
        window = self.FindWindowById(window_id)
        value = utils.validate_numeric(window)

        # Clamp sprite index and update sprite name.
        if window_id == windows.STATES_SPRITE:
            if value < 0:
                value = 0
                wx.Bell()
            elif value >= len(self.patch.sprite_names):
                value = len(self.patch.sprite_names) - 1
                wx.Bell()
            self.SpriteName.SetLabel(self.patch.get_sprite_name(value))
            window.ChangeValue(str(value))

        # Clamp next state index and update state name.
        elif window_id == windows.STATES_NEXT:
            if value < 0:
                value = 0
                wx.Bell()
            elif value >= len(self.patch.states):
                value = len(self.patch.states) - 1
                wx.Bell()
            self.NextStateName.SetLabel(self.patch.get_state_name(value))
            window.ChangeValue(str(value))

        # Clamp duration.
        elif window_id == windows.STATES_DURATION:
            if value < -1:
                value = 0
                window.ChangeValue(str(value))
                wx.Bell()

        key = self.PROPS_STATE[window_id]
        self.set_selected_property(key, value)

        self.StateList.refresh_selected_rows()
        self.update_sprite_preview()
        self.is_modified(True)

        # Update sprite index colour coding.
        if window_id == windows.STATES_SPRITE:
            self.StateList.update_item_attributes()

    def set_lit(self, event: CommandEvent):
        """
        Sets the lit property of all currently selected states.
        """

        self.undo_add()

        checked = self.AlwaysLit.GetValue()

        for _, _, state in self.StateList.iterate_selected():

            # Remove lit flag, then set it only if it needs to be.
            frame_index = state['spriteFrame'] & ~self.FRAMEFLAG_LIT
            if checked:
                frame_index |= self.FRAMEFLAG_LIT

            state['spriteFrame'] = frame_index

        self.StateList.refresh_selected_rows()
        self.is_modified(True)

    def set_action(self, event: CommandEvent):
        """
        Sets the action property of all currently selected states.
        """

        action_name = self.Action.GetStringSelection()
        action_key = self.patch.engine.get_action_key_from_name(action_name)

        if not self.patch.engine.extended and action_key == '0':
            self.update_properties()
            return

        self.undo_add()

        for _, state_index, state in self.StateList.iterate_selected():

            # Only allow modifying a state's action if the engine is extended, or if the state
            # already has an action.
            if self.patch.engine.extended or self.patch.engine.states[state_index]['action'] != '0':
                state['action'] = action_key

        self.set_param_visibility(action_key)
        self.StateList.refresh_selected_rows()
        self.is_modified(True)

    def set_frame(self, event: CommandEvent):
        """
        Sets the frame index property of all currently selected states.
        """

        self.undo_add()

        window = self.FindWindowById(event.GetId())
        value = utils.validate_numeric(window)

        # Clamp to a valid index.
        if value < 0:
            value = 0
        elif value >= config.MAX_SPRITE_FRAME:
            value = config.MAX_SPRITE_FRAME - 1
        if window.GetValue() != str(value):
            window.ChangeValue(str(value))
            wx.Bell()

        # Manually update all selected states so that the lit frame index flag can be retained.
        for _, _, state in self.StateList.iterate_selected():
            state['spriteFrame'] = value | (state['spriteFrame'] & self.FRAMEFLAG_LIT)

        self.StateList.refresh_selected_rows()
        self.update_sprite_preview()
        self.is_modified(True)

    def set_selected_action(self, action_key: str):
        """
        Sets the action choice box' index to reflect the specified action value.
        """

        action = self.patch.engine.actions[action_key]
        self.Action.Select(self.Action.FindString(action.name))

        self.set_param_visibility(action_key)

    def state_context(self, event: ListEvent):
        """
        Displays the context menu for states.
        """

        enable_loops = self.StateList.get_selected_count() > 1
        self.StateContextLink.Enable(enable_loops)
        self.StateContextLinkLoop.Enable(enable_loops)

        self.StateList.PopupMenu(self.StateContext, event.GetPoint())

    def state_context_copy(self, event: MenuEvent):
        """
        Context menu copy redirect.
        """
        self.edit_copy()

    def state_context_paste(self, event: MenuEvent):
        """
        Context menu paste redirect.
        """
        self.edit_paste()

    def link_selected_states(self, loop: bool):
        """
        Links the currently selected states together.
        """

        self.undo_add()

        prev_state = None

        for _, state_index, state in self.StateList.iterate_selected():

            # Link previous state to this one.
            if prev_state is not None:
                prev_state['nextState'] = state_index

            prev_state = state

        # Link last state to first state to loop.
        if loop:
            last_selected = self.StateList.get_last_selected()
            state_last = self.StateList.query_result.get_state_for_item_index(last_selected)
            if state_last:
                first_selected = self.StateList.get_first_selected()
                query_result = self.StateList.query_result
                state_first_index = query_result.get_state_index_for_item_index(first_selected)
                state_last['nextState'] = state_first_index

        self.StateList.refresh_selected_rows()
        self.update_properties()
        self.is_modified(True)

    def frame_set(self, modifier: int):
        """
        Modifies the state frame index value by a specified amount.
        """

        if self.FrameIndex.GetValue() == '':
            self.FrameIndex.SetValue('0')
        else:
            index = int(self.FrameIndex.GetValue())
            self.FrameIndex.SetValue(str(index + modifier))

    def goto_next_state(self, event: CommandEvent):
        """
        Select the currently selected state's next state.
        """

        if self.StateList.get_selected_count() == 0:
            return

        first_selected = self.StateList.get_first_selected()
        state = self.StateList.query_result.get_state_for_item_index(first_selected)
        if state is not None:
            self.goto_state_index(state['nextState'])

    def goto_state_index(
        self,
        state_index: int,
        filter_type: Optional[str] = None,
        filter_index: Optional[int] = None
    ):
        """
        Selects a state and applies a filter.

        @param state_index: the index of the state to select.
        @param filter_type: the type of filter to enable. @see dehacked.statequery.
        @param filter_index: the index of the item to filter for. @see dehacked.statequery.
        """

        # Enable the specified filter.
        if filter_type is not None:
            for index, data in enumerate(self.filters):
                if data['type'] == filter_type and data['index'] == filter_index:
                    self.filter_update(index)
                    self.Filter.Select(index)
                    break

        # Disable all filtering otherwise.
        else:
            if not self.StateList.query_result.contains_state_index(state_index):
                self.filter_update(0)
                self.Filter.Select(0)

        # Select only the specified state and make sure it is visible.
        list_index = self.StateList.query_result.get_item_index_for_state_index(state_index)
        self.StateList.clear_selection()
        self.StateList.Select(list_index, True)
        self.StateList.EnsureVisible(list_index)
        self.StateList.SetFocus()

    def get_selected_state_index(self) -> int:
        """
        Returns the index of the currently selected state.

        :return:
        """

        item_index = self.StateList.get_first_selected()
        if item_index == -1:
            return -1

        return self.StateList.query_result.get_state_index_for_item_index(item_index)

    def preview(self):
        """
        Start an animation preview at the selected state.
        """

        filter_data = self.filters[self.Filter.GetSelection()]

        # If we are currently filtering for a thing, use that as the preview's reference thing.
        if filter_data['type'] == FILTER_TYPE_THING:
            thing_index = filter_data['index']
        else:
            thing_index = None

        first_selected = self.StateList.get_first_selected()
        state_index = self.StateList.query_result.get_state_index_for_item_index(first_selected)
        self.preview_dialog.prepare(self.pwads, self.patch, state_index, thing_index)
        self.preview_dialog.ShowModal()

    def state_key(self, event: KeyEvent):
        """
        Intercept key presses to this entire frame.
        """

        if event.GetKeyCode() == 96:
            self.preview()
        else:
            event.Skip()

    def state_context_clear(self, event: MenuEvent):
        """
        Clears all selected states.
        """

        self.undo_add()

        for _, state_index, _ in self.StateList.iterate_selected():
            self.patch.states[state_index] = self.patch.engine.default_state.clone()

        self.StateList.refresh_selected_rows()

    def state_context_link(self, event: MenuEvent):
        self.link_selected_states(False)

    def state_context_link_loop(self, event: MenuEvent):
        self.link_selected_states(True)

    def state_context_preview(self, event: MenuEvent):
        self.preview()

    def filter_select(self, event: ListEvent):
        self.filter_update(self.Filter.GetSelection())

    def frame_spin_up(self, event: SpinEvent):
        self.frame_set(1)

    def frame_spin_down(self, event: SpinEvent):
        self.frame_set(-1)

    def statelist_event(self, _: ListEvent):
        """
        Event redirect for updating properties.
        """
        self.update_properties()

    def _adjust_mac_ui(self):
        """
        Adjust the UI for macOS.
        """

        if sys.platform != 'darwin':
            return

        id = self.FilterToolRefresh.GetId()
        label = self.FilterToolRefresh.GetLabel()
        bitmap_size = self.FilterTools.GetToolBitmapSize()
        bitmap = self.FilterToolRefresh.GetBitmap().ConvertToImage().Scale(
            bitmap_size.width,
            bitmap_size.height).ConvertToBitmap()
        short_help = self.FilterToolRefresh.GetShortHelp()
        disabled_bitmap = self.FilterToolRefresh.GetDisabledBitmap()
        kind = self.FilterToolRefresh.GetKind()
        long_help = self.FilterToolRefresh.GetLongHelp()
        client_data = self.FilterToolRefresh.GetClientData()

        self.FilterTools.ClearTools()
        self.FilterToolRefresh = self.FilterTools.AddTool(id, label, bitmap, disabled_bitmap, kind, short_help, long_help, client_data)


def get_action_param_counts(action: Optional[Action]) -> int:
    """
    Returns the number of parameters for an action.

    :param action:

    :return:
    """
    if action is None:
        return 0

    return len(action.arguments)


def get_action_param_properties(unused_count: int = 0, arg_count: int = 0) -> List[str]:
    """
    Returns action property state fields.

    :param unused_count:
    :param arg_count:

    :return:
    """
    params = []
    if unused_count:
        params.extend([f'unused{x}' for x in range(1, unused_count + 1)])
    if arg_count:
        params.extend([f'arg{x}' for x in range(1, arg_count + 1)])

    return params
