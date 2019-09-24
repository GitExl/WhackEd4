from collections import OrderedDict
from typing import Optional, List

from whacked4 import config, utils
from whacked4.dehacked.patch import Patch
from whacked4.dehacked.statequery.query import StateFilterQuery
from whacked4.dehacked.statequery.result import StateQueryResult
from whacked4.dehacked.statequery.stateindexsort import StateIndexSort
from whacked4.dehacked.statequery.thingfilter import ThingStateFilter
from whacked4.dehacked.statequery.unusedfilter import UnusedStateFilter
from whacked4.dehacked.statequery.weaponfilter import WeaponStateFilter
from whacked4.doom.wadlist import WADList
from whacked4.ui import editormixin, windows
from whacked4.ui.dialogs import spritesdialog, statepreviewdialog

import wx

from whacked4.ui.dialogs.spritesdialog import SpritesDialog
from whacked4.ui.dialogs.statepreviewdialog import StatePreviewDialog
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
    PROPS_STATE = {
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

    # The colours used for color-coding sprite indices.
    SPRITE_COLOURS = [
        wx.Colour(red=255, green=48, blue=0),
        wx.Colour(red=255, green=255, blue=255)
    ]

    # Window ids grouped by state parameter value.
    UNUSED_IDS = [
        [windows.STATES_LABEL_UNUSED1, windows.STATES_UNUSED1],
        [windows.STATES_LABEL_UNUSED2, windows.STATES_UNUSED2]
    ]
    ARG_IDS = [
        [windows.STATES_LABEL_ARG1, windows.STATES_ARG1],
        [windows.STATES_LABEL_ARG2, windows.STATES_ARG2],
        [windows.STATES_LABEL_ARG3, windows.STATES_ARG3],
        [windows.STATES_LABEL_ARG4, windows.STATES_ARG4],
        [windows.STATES_LABEL_ARG5, windows.STATES_ARG5],
        [windows.STATES_LABEL_ARG6, windows.STATES_ARG6],
        [windows.STATES_LABEL_ARG7, windows.STATES_ARG7],
        [windows.STATES_LABEL_ARG8, windows.STATES_ARG8],
        [windows.STATES_LABEL_ARG9, windows.STATES_ARG9],
    ]

    # Doom lit flag. Frame indices with this flag set are always lit by Doom's rendering engine.
    FRAMEFLAG_LIT = 0x8000

    def __init__(self, params):
        windows.StatesFrameBase.__init__(self, params)
        editormixin.EditorMixin.__init__(self)

        self.SetIcon(wx.Icon('res/editor-states.ico'))

        # A list of all tool windows for simple mass operations.
        self.WINDOWS_TOOLS = [
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
        self.clipboard = None
        self.sprites_dialog: Optional[SpritesDialog] = None
        self.preview_dialog: Optional[StatePreviewDialog] = None
        self.selected = None

        self.state_query_results: Optional[StateQueryResult] = None
        self.filters: List[int] = []

        # Mix sprite color coding colours with the default system colours.
        self.mix_colours()

        self.SpriteName.SetFont(config.FONT_MONOSPACED_BOLD)
        self.NextStateName.SetFont(config.FONT_MONOSPACED_BOLD)

        self.Bind(wx.EVT_CHAR_HOOK, self.state_key)

        self.StateList.Bind(EVT_STATE_LIST_EVENT, self.state_selection_update)

    def build(self, patch):
        """
        @see: EditorMixin.build
        """

        self.patch = patch
        self.StateList.set_patch(patch)
        self.pwads = self.GetParent().pwads
        self.clipboard = None

        self.sprites_dialog = spritesdialog.SpritesDialog(self.GetParent())
        self.preview_dialog = statepreviewdialog.StatePreviewDialog(self.GetParent())

        # Setup sprite preview control.
        self.SpritePreview.set_source(self.pwads)
        self.SpritePreview.set_baseline_factor(0.85)
        self.SpritePreview.set_scale(2)

        # List of selected list indices.
        self.selected = []

        # Initialize filter.
        self.build_filterlist()
        self.build_actionlist()

        self.filter_update(0)

    def update(self):
        """
        @see: EditorMixin.update
        """

        self.pwads = self.GetParent().pwads

        self.sprites_dialog.update(self.pwads)
        self.preview_dialog.update(self.pwads)

        self.SpritePreview.set_source(self.pwads)
        self.update_sprite_preview()

    def mix_colours(self):
        """
        Mixes sprite index colour coding with the system's window background color.
        """

        sys_colour = self.StateList.GetBackgroundColour()
        for index, colour in enumerate(self.SPRITE_COLOURS):
            self.SPRITE_COLOURS[index] = utils.mix_colors(colour, sys_colour, 0.92)

    def undo_restore_item(self, item):
        """
        @see: EditorMixin.undo_restore_item
        """

        for state_index, state in item.items():
            self.patch.states[state_index] = state

            # Restore all state indices in the undo item.
            if self.state_query_results.contains_state(state_index):
                list_index = self.state_query_results.get_item_index_for_state(state_index)
                self.StateList.RefreshItem(list_index)
                #self.filter_states[list_index] = state

        self.update_properties()
        self.update_sprite_preview()

        self.is_modified(True)

    def undo_store_item(self):
        """
        @see: EditorMixin.undo_store_item
        """

        # Store all currently selected states.
        items = OrderedDict()
        for list_index in self.selected:
            state = self.state_query_results.get_state_for_item_index(list_index)
            state_index = self.state_query_results.get_state_index_for_item_index(list_index)

            items[state_index] = state.clone()

        return items

    def edit_copy(self):
        """
        Copies all currently selected states to the clipboard.

        The states are stored in sequence, without non-selected states in between.
        """

        self.clipboard = []

        for list_index in self.selected:
            state = self.state_query_results.get_state_for_item_index(list_index)
            dup = state.clone()
            self.clipboard.append(dup)

    def edit_paste(self):
        """
        Pastes the current clipboard, starting at the first selected state.
        """

        if self.clipboard is None:
            return
        if len(self.selected) == 0:
            return

        # Do not paste over state 0.
        list_index = self.selected[0]
        state_index = self.state_query_results.get_state_index_for_item_index(list_index)
        if state_index == 0:
            return

        self.undo_add()

        for state in self.clipboard:
            # Ignore states that are not currently visible because of filters.
            if list_index in self.selected:
                dup = state.clone()
                state_index = self.state_query_results.get_state_index_for_item_index(list_index)
                self.patch.states[state_index] = dup
                #self.filter_states[list_index] = dup
                self.StateList.RefreshItem(list_index)

            list_index += 1
            if list_index >= len(self.patch.states):
                break

        self.update_properties()
        self.update_colours()
        self.is_modified(True)

    def tools_set_state(self, enabled):
        """
        Sets the state of all tool controls.
        """

        for window in self.WINDOWS_TOOLS:
            window.Enable(enabled)

    def state_restore(self, event):
        """
        Restores all currently selected states to the way they are in the engine configuration.
        """

        self.undo_add()

        for list_index in self.selected:
            state_index = self.state_query_results.get_state_index_for_item_index(list_index)
            self.patch.states[state_index] = self.patch.engine.states[state_index].clone()
            #self.filter_states[list_index] = self.patch.states[state_index]
            self.StateList.RefreshItem(list_index)

        self.update_properties()
        self.update_colours()
        self.is_modified(True)

    def state_link(self, event):
        """
        Connects the currently selected state's next state property to the state being clicked, while the alt key
        is held down.
        """

        # Set the current state's next state if the alt key is held down.
        connect = wx.GetKeyState(wx.WXK_ALT)
        if connect:
            x = event.GetX()
            y = event.GetY()
            list_index = self.StateList.HitTest(wx.Point(x, y))[0]
            if list_index == wx.NOT_FOUND:
                return

            state_index = self.state_query_results.get_state_index_for_item_index(list_index)
            self.NextStateIndex.ChangeValue(str(state_index))
            self.set_selected_property('nextState', state_index)
            self.statelist_update_selected_rows()

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
        for index in range(len(self.patch.things.names)):
            self.filters.append({
                'name': self.patch.things.names[index],
                'type': FILTER_TYPE_THING,
                'index': index
            })

        # Add weapon state filters.
        for index in range(len(self.patch.weapons.names)):
            self.filters.append({
                'name': self.patch.weapons.names[index],
                'type': FILTER_TYPE_WEAPON,
                'index': index
            })

        selected = self.Filter.GetSelection()
        list_items = []
        for filter_data in self.filters:
            list_items.append(filter_data['name'])
        self.Filter.SetItems(list_items)

        if selected != -1:
            self.Filter.Select(selected)
        else:
            self.Filter.Select(0)

    def update_filterlist(self):
        """
        Refreshes the filter list with the current filter selection.
        """

        self.build_filterlist()

    def build_actionlist(self):
        """
        Builds the list of available state actions.
        """

        action_items = []

        for action in self.patch.engine.actions.values():
            action_items.append(action.name)

        self.Action.SetItems(action_items)

    def statelist_build(self):
        """
        Builds the list of currently filtered states.
        """

        return

        wx.BeginBusyCursor()

        self.StateList.Freeze()
        self.StateList.ClearAll()
        self.selected = []

        # Add list column headers if needed.
        if self.StateList.GetColumnCount() == 0:
            self.StateList.InsertColumn(0, '', width=37)
            self.StateList.InsertColumn(1, 'Name', width=57)
            self.StateList.InsertColumn(2, 'Spr', width=39)
            self.StateList.InsertColumn(3, 'Frm', width=39)
            self.StateList.InsertColumn(4, 'Lit', width=27)
            self.StateList.InsertColumn(5, 'Next', width=41)
            self.StateList.InsertColumn(6, 'Dur', width=40)
            self.StateList.InsertColumn(7, 'Action', width=160)
            self.StateList.InsertColumn(8, 'Parameters', width=107)

        # Add all items in the filtered list.
        list_index = 0

        for state_index in self.filter_state_indices:
            self.StateList.InsertItem(list_index, str(state_index))
            self.StateList.SetItemFont(list_index, config.FONT_MONOSPACED)
            self.StateList.RefreshItem(list_index)

            list_index += 1

        self.update_colours()

        # Select the first row if it is not state 0.
        if len(self.filter_state_indices) > 1 and self.filter_state_indices[0] == 0:
            self.StateList.Select(1, True)
        elif len(self.filter_state_indices) > 0:
            self.StateList.Select(0, True)

        self.StateList.Thaw()

        wx.EndBusyCursor()

    def filter_update(self, index):
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

        self.state_query_results = state_query.execute()

        self.StateList.set_state_query_result(self.state_query_results)
        self.StateList.Refresh()
        self.update_properties()

    def set_selected_property(self, key, value):
        """
        Sets a property of all currently selected states.

        @param key: the state property key to set.
        @param value: the new value of the state property.
        """

        self.undo_add()

        for list_index in self.selected:
            state_index = self.state_query_results.get_state_index_for_item_index(list_index)
            if state_index == 0:
                continue

            state = self.state_query_results.get_state_for_item_index(list_index)
            state[key] = value

        self.is_modified(True)

    def statelist_update_selected_rows(self):
        """
        Updates the contents of every selected state list row.
        """

        self.StateList.Freeze()

        for list_index in self.selected:
            self.StateList.RefreshItem(list_index)

        self.StateList.Thaw()

    def update_properties(self):
        """
        Updates the tool controls with the properties of the currently selected state(s).
        """

        # If only one state is selected, fill the property controls with that state's data.
        if len(self.selected) == 1:
            state = self.state_query_results.get_state_for_item_index(self.selected[0])
            state_index = self.state_query_results.get_state_index_for_item_index(self.selected[0])

            if state_index == 0:
                sprite_name = '-'
            else:
                sprite_name = self.patch.sprite_names[state['sprite']]
            sprite_frame = state['spriteFrame'] & ~self.FRAMEFLAG_LIT

            self.SpriteIndex.ChangeValue(str(state['sprite']))
            self.SpriteName.SetLabel(sprite_name)
            self.FrameIndex.ChangeValue(str(sprite_frame))
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

        self.update_sprite_preview()

    def set_param_visibility(self, action_key):
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
        for index in range(0, len(StatesFrame.UNUSED_IDS)):
            label = self.FindWindowById(StatesFrame.UNUSED_IDS[index][0])
            text = self.FindWindowById(StatesFrame.UNUSED_IDS[index][1])

            if (action is not None) and (index < len(action.unused)):
                label.SetLabel(action.unused[index].name)
                text.SetToolTip(action.unused[index].description)
            else:
                label.SetLabel('Unused {}'.format(index + 1))
                text.SetToolTip('')

        # Arg0-9 parameters.
        for index in range(0, len(StatesFrame.ARG_IDS)):
            label = self.FindWindowById(StatesFrame.ARG_IDS[index][0])
            text = self.FindWindowById(StatesFrame.ARG_IDS[index][1])

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

        if len(self.selected) == 1:
            state = self.state_query_results.get_state_for_item_index(self.selected[0])
            state_index = self.state_query_results.get_state_index_for_item_index(self.selected[0])

            # Find a valid sprite name and frame index.
            if state_index != 0:
                sprite_index = state['sprite']
                if sprite_index != '':
                    sprite_index = int(sprite_index)
                    sprite_name = self.patch.sprite_names[sprite_index]

                    sprite_frame = state['spriteFrame'] & ~self.FRAMEFLAG_LIT
                    if sprite_frame != '':
                        sprite_frame = int(sprite_frame)
                    else:
                        sprite_frame = 0

                    self.SpritePreview.show_sprite(sprite_name, sprite_frame)
                    return

        self.SpritePreview.clear()

    def statelist_key_down(self, event):
        """
        Handle key presses for the states list.
        """

        if event.GetKeyCode() == 76 and event.ShiftDown():
            self.link_selected_states(True)
        elif event.GetKeyCode() == 76:
            self.link_selected_states(False)
        else:
            event.Skip()

    def select_sprite(self, event):
        """
        Shows the sprite select dialog to replace the currently selected state's sprites.
        """

        # Only use the first selected state's sprite as the default selected value.
        if len(self.selected) == 1:
            sprite_index = int(self.SpriteIndex.GetValue())
            frame_index = int(self.FrameIndex.GetValue())

        elif len(self.selected) > 1:
            state = self.state_query_results.get_state_for_item_index(self.selected[0])
            sprite_index = state['sprite']
            frame_index = None

        else:
            sprite_index = 0
            frame_index = 0

        self.sprites_dialog.set_state(self.patch, self.pwads, sprite_index=sprite_index, frame_index=frame_index)
        self.sprites_dialog.ShowModal()

        if self.sprites_dialog.selected_sprite != -1:
            sprite_index = self.sprites_dialog.selected_sprite
            frame_index = self.sprites_dialog.selected_frame

            self.SpriteIndex.SetValue(str(sprite_index))

            # Change the frame index if it was altered.
            if frame_index != -1:
                self.FrameIndex.ChangeValue(str(frame_index))

                # Update sprite frames separately to mix in lit flag.
                for list_index in self.selected:
                    state = self.state_query_results.get_state_for_item_index(list_index)
                    state['spriteFrame'] = frame_index | (state['spriteFrame'] & self.FRAMEFLAG_LIT)

            self.statelist_update_selected_rows()
            self.update_colours()
            self.update_sprite_preview()

    def set_value(self, event):
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
            elif value >= len(self.patch.sprite_names):
                value = len(self.patch.sprite_names) - 1
            self.SpriteName.SetLabel(self.patch.sprite_names[value])
            window.ChangeValue(str(value))

        # Clamp next state index and update state name.
        elif window_id == windows.STATES_NEXT:
            if value < 0:
                value = 0
            elif value >= len(self.patch.states):
                value = len(self.patch.states) - 1
            self.NextStateName.SetLabel(self.patch.get_state_name(value))
            window.ChangeValue(str(value))

        # Clamp duration.
        elif window_id == windows.STATES_DURATION:
            if value < -1:
                value = 0
                window.ChangeValue(str(value))

        key = self.PROPS_STATE[window_id]
        self.set_selected_property(key, value)

        self.statelist_update_selected_rows()
        self.update_sprite_preview()
        self.is_modified(True)

        # Update sprite index colour coding.
        if window_id == windows.STATES_SPRITE:
            self.update_colours()

    def set_lit(self, event):
        """
        Sets the lit property of all currently selected states.
        """

        self.undo_add()

        checked = self.AlwaysLit.GetValue()

        for list_index in self.selected:
            state = self.state_query_results.get_state_for_item_index(list_index)

            # Remove lit flag, then set it only if it needs to be.
            frame_index = state['spriteFrame'] & ~self.FRAMEFLAG_LIT
            if checked:
                frame_index |= self.FRAMEFLAG_LIT

            state['spriteFrame'] = frame_index

        self.statelist_update_selected_rows()
        self.is_modified(True)

    def set_action(self, event):
        """
        Sets the action property of all currently selected states.
        """

        action_name = self.Action.GetStringSelection()
        action_key = self.patch.engine.get_action_key_from_name(action_name)

        if not self.patch.engine.extended and action_key == '0':
            self.update_properties()
            return

        self.undo_add()

        for list_index in self.selected:
            state = self.state_query_results.get_state_for_item_index(list_index)
            state_index = self.state_query_results.get_state_index_for_item_index(list_index)

            # Only allow modifying a state's action if the engine is extended, or if the state already has an action.
            if self.patch.engine.extended or self.patch.engine.states[state_index]['action'] != '0':
                state['action'] = action_key

        self.set_param_visibility(action_key)
        self.statelist_update_selected_rows()
        self.is_modified(True)

    def set_frame(self, event):
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

        # Manually update all selected states so that the lit frame index flag can be retained.
        for list_index in self.selected:
            state = self.state_query_results.get_state_for_item_index(list_index)
            state['spriteFrame'] = value | (state['spriteFrame'] & self.FRAMEFLAG_LIT)

        self.statelist_update_selected_rows()
        self.update_sprite_preview()
        self.is_modified(True)

    def set_selected_action(self, action_key):
        """
        Sets the action choice box' index to reflect the specified action value.
        """

        action = self.patch.engine.actions[action_key]
        self.Action.Select(self.Action.FindString(action.name))

        self.set_param_visibility(action_key)

    def state_context(self, event):
        """
        Displays the context menu for states.
        """

        enable_loops = (self.StateList.GetSelectedItemCount() > 1)
        self.StateContextLink.Enable(enable_loops)
        self.StateContextLinkLoop.Enable(enable_loops)

        self.StateList.PopupMenu(self.StateContext, event.GetPoint())

    def state_context_copy(self, event):
        """
        Context menu copy redirect.
        """
        self.edit_copy()

    def state_context_paste(self, event):
        """
        Context menu paste redirect.
        """
        self.edit_paste()

    def link_selected_states(self, loop):
        """
        Links the currently selected states together.
        """

        self.undo_add()

        prev_state = None

        for list_index in self.selected:
            state = self.state_query_results.get_state_for_item_index(list_index)
            state_index = self.state_query_results.get_state_index_for_item_index(list_index)

            # Link previous state to this one.
            if prev_state is not None:
                prev_state['nextState'] = state_index

            prev_state = state

        # Link last state to first state to loop.
        if loop:
            state_last = self.state_query_results.get_state_for_item_index(self.selected[-1])
            state_first_index = self.state_query_results.get_state_index_for_item_index(self.selected[0])

            state_last['nextState'] = state_first_index

        self.statelist_update_selected_rows()
        self.update_properties()
        self.is_modified(True)

    def selection_clear(self):
        """
        Clears the list of selected states.
        """

        self.StateList.Freeze()

        for list_index in self.selected:
            self.StateList.Select(list_index, False)

        self.StateList.Thaw()

    def frame_set(self, modifier):
        """
        Modifies the state frame index value by a specified amount.
        """

        if self.FrameIndex.GetValue() == '':
            self.FrameIndex.SetValue('0')
        else:
            index = int(self.FrameIndex.GetValue())
            self.FrameIndex.SetValue(str(index + modifier))

    def goto_next_state(self, event):
        """
        Select the currently selected state's next state.
        """

        if len(self.selected) == 0:
            return

        state = self.state_query_results.get_state_for_item_index(self.selected[0])
        self.goto_state_index(state['nextState'])

    def goto_state_index(self, state_index, filter_type=None, filter_index=None):
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
            if not self.state_query_results.contains_state(state_index):
                self.filter_update(0)
                self.Filter.Select(0)

        # Select only the specified state and make sure it is visible.
        list_index = self.state_query_results.get_item_index_for_state_index(state_index)
        self.selection_clear()
        self.StateList.Select(list_index, True)
        self.StateList.EnsureVisible(list_index)
        self.StateList.SetFocus()

    def statelist_resize(self, event):
        """
        Resizes the state parameters column to match the control's width.
        """

        columns_width = self.StateList.GetColumnWidth(0) + self.StateList.GetColumnWidth(1)
        columns_width += self.StateList.GetColumnWidth(2) + self.StateList.GetColumnWidth(3)
        columns_width += self.StateList.GetColumnWidth(4) + self.StateList.GetColumnWidth(5)
        columns_width += self.StateList.GetColumnWidth(6) + self.StateList.GetColumnWidth(7)

        width = self.StateList.GetClientSize()[0] - columns_width - 4
        self.StateList.SetColumnWidth(8, width)

    def preview(self):
        filter_data = self.filters[self.Filter.GetSelection()]

        # If we are currently filtering for a thing, use that as the preview's reference thing.
        if filter_data['type'] == FILTER_TYPE_THING:
            thing_index = filter_data['index']
        else:
            thing_index = None

        state_index = self.state_query_results.get_state_index_for_item_index(self.selected[0])
        self.preview_dialog.prepare(self.pwads, self.patch, state_index, thing_index)
        self.preview_dialog.ShowModal()

    def state_key(self, event):
        """
        Intercept keypresses to this entire frame.
        """

        if event.GetKeyCode() == 96:
            self.preview()
        else:
            event.Skip()

    def state_context_clear(self, event):
        """
        Clears all selected states.
        """

        self.undo_add()

        for list_index in self.selected:
            state_index = self.state_query_results.get_state_index_for_item_index(list_index)
            self.patch.states[state_index] = self.patch.engine.empty_state.clone()
            #self.filter_states[list_index] = self.patch.states[state_index]

        self.statelist_update_selected_rows()

    def state_context_link(self, event):
        self.link_selected_states(False)

    def state_context_link_loop(self, event):
        self.link_selected_states(True)

    def state_context_preview(self, event):
        self.preview()

    def state_selection_update(self, event):
        self.selected = event.selection.copy()
        self.update_properties()

    def filter_select(self, event):
        self.filter_update(self.Filter.GetSelection())

    def frame_spin_up(self, event):
        self.frame_set(1)

    def frame_spin_down(self, event):
        self.frame_set(-1)


def get_action_param_counts(action):
    if action is None:
        return 0

    return len(action.arguments)


def get_action_param_properties(unused_count=0, arg_count=0):
    params = []
    if unused_count:
        params.extend(['unused{}'.format(x) for x in range(1, unused_count + 1)])
    if arg_count:
        params.extend(['arg{}'.format(x) for x in range(1, arg_count + 1)])

    return params
