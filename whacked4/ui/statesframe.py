from app import config
from collections import OrderedDict
from dehacked import statefilter
from ui import windows, utils, spritesdialog, editormixin
import copy
import wx

class StatesFrame(editormixin.EditorMixin, windows.StatesFrameBase):
    FRAMEFLAG_LIT = 0x8000
    
    PROPS_STATE = {
        windows.STATES_DURATION: 'duration',
        windows.STATES_NEXT: 'nextState',
        windows.STATES_PARM1: 'parameter1',
        windows.STATES_PARM2: 'parameter2',
        windows.STATES_SPRITE: 'sprite'
    }
        
    SPRITE_COLOURS = [
        wx.Colour(red=255, green=48, blue=0),
        wx.Colour(red=255, green=255, blue=255),
    ]
    
    def __init__(self, params):
        windows.StatesFrameBase.__init__(self, params)
        editormixin.EditorMixin.__init__(self)
        
        self.SetIcon(wx.Icon('res/icon-weapons-small.bmp'))
                
        self.WINDOWS_TOOLS = [
            self.SpriteIndex,
            self.SpriteSelect,
            self.FrameIndex,
            self.FrameIndexSpinner,
            self.AlwaysLit,
            self.NextStateIndex,
            self.Duration,
            self.Action,
            self.Parameter1,
            self.Parameter2,
            self.Restore,
            self.NextStateName,
            self.SpriteName
        ]
        
        font_size = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT).GetPointSize()
        self.list_font = wx.Font(
            font_size,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL,
            faceName=config.FONT_MONOSPACED
        )
        
        self.mix_colors()


    def build(self, patch):
        self.patch = patch
        self.clipboard = None
        self.pwads = self.GetParent().pwads
        
        self.SpritePreview.set_source(self.pwads)
        self.SpritePreview.set_baseline_factor(0.9)
        
        # Undo properties.
        self.undo = []
        self.undo_index = -1
        
        self.sprites_dialog = spritesdialog.SpritesDialog(self.GetParent())
                
        # List of selected list indices.
        self.selected = []
        
        # Initialize filter.
        self.filter = statefilter.StateFilter(patch)
        self.build_filterlist()
        self.filter_update(0)
        
        self.build_statelist()
        self.build_actionlist()
                
        
    def mix_colors(self):
        sys_col = self.StateList.GetBackgroundColour()
        factor = 0.08
        sys_factor = 1 - factor
        
        for col in self.SPRITE_COLOURS:
            col.Set(
                int(col.Red() * factor + sys_col.Red() * sys_factor),
                int(col.Green() * factor + sys_col.Green() * sys_factor),
                int(col.Blue() * factor + sys_col.Blue() * sys_factor)
            )
        
        
    def undo_restore_item(self, item):
        for state_index, state in item.iteritems():
            self.patch.states[state_index] = state
            
            if state_index in self.filter.state_indices:
                list_index = self.filter.state_indices.index(state_index)
                self.filter.states[list_index] = state
                self.update_row(list_index)
        
        self.tools_update()
        self.update_sprite_preview()
        
        
    def undo_store_item(self):
        items = OrderedDict()
        
        for list_index in self.selected:
            state_index = self.filter.state_indices[list_index]
            state = copy.deepcopy(self.filter.states[list_index])
            
            items[state_index] = state
            
        return items
            
    
    def edit_copy(self):
        self.clipboard = []
        
        for list_index in self.selected:
            dup = copy.deepcopy(self.filter.states[list_index])
            self.clipboard.append(dup)
        
        
    def edit_paste(self):
        if self.clipboard is None:
            return
        if len(self.selected) == 0:
            return
        
        list_index = self.selected[0]
        if self.filter.state_indices[list_index] == 0:
            return
        
        self.undo_add()
         
        for state in self.clipboard:
            dup = copy.deepcopy(state)
            state_index = self.filter.state_indices[list_index]
            
            if list_index in self.selected:
                self.patch.states[state_index] = dup
                self.update_row(list_index)
            
            list_index += 1
            if list_index >= len(self.patch.states):
                break
        
        self.tools_update()
        self.GetParent().set_modified(True)
    
    
    def tools_set_state(self, enabled):
        if enabled == True:
            for window in self.WINDOWS_TOOLS:
                window.Enable()
        elif enabled == False:
            for window in self.WINDOWS_TOOLS:
                window.Disable()
                
                
    def state_restore(self, event):
        self.undo_add()
        
        for list_index in self.selected:
            state_index = self.filter.state_indices[list_index]
            self.patch.states[state_index] = copy.deepcopy(self.patch.engine.states[state_index])
            self.filter.states[list_index] = self.patch.states[state_index]
        
        self.tools_update()
        self.update_selected_rows()
        self.update_colors()
        self.GetParent().set_modified(True)
        
    
    def state_link(self, event):
        # Set the current state's next state if the alt key is held down.
        connect = wx.GetKeyState(wx.WXK_ALT)
        if connect == True:
            x = event.GetX()
            y = event.GetY()
            list_index = self.StateList.HitTest(wx.Point(x, y))[0]
            if list_index == wx.NOT_FOUND:
                return
            
            state_index = self.filter.state_indices[list_index]
            self.NextStateIndex.ChangeValue(str(state_index))
            self.set_selected_property('nextState', state_index)
            self.update_selected_rows()
        
        else:
            event.Skip()
            

    def state_select(self, event):
        self.selected.append(event.GetIndex())
        self.tools_update()
        
            
    def state_deselect(self, event):
        self.selected.remove(event.GetIndex())
        self.tools_update()
    
    
    def build_filterlist(self):
        list_items = []
        for filter_data in self.filter.filters:
            list_items.append(filter_data['name'])
        self.Filter.SetItems(list_items)
                
        self.Filter.Select(0)
    
            
    def build_actionlist(self):
        action_items = []
        
        if self.patch.engine.extended == True:
            for name in self.patch.engine.actions.iterkeys():
                if name == 'NULL':
                    name = ''
                action_items.append(name)
        
        else:
            for action in self.patch.engine.actions.itervalues():
                if action['name'] == 'NULL':
                    action_items.append('')
                else:
                    action_items.append(action['name'])
                    
        self.Action.SetItems(action_items)
        
        
    def build_statelist(self):
        wx.BeginBusyCursor()
        
        self.StateList.Freeze()
        self.StateList.ClearAll()
        self.selected = []
        
        # Add columns when needed.
        if self.StateList.GetColumnCount() == 0:
            self.StateList.InsertColumn(0, '', width=29)
            self.StateList.InsertColumn(1, 'Name', width=47)
            self.StateList.InsertColumn(2, 'Spr', width=33)
            self.StateList.InsertColumn(3, 'Frm', width=34)
            self.StateList.InsertColumn(4, 'Lit', width=25)
            self.StateList.InsertColumn(5, 'Next', width=36)
            self.StateList.InsertColumn(6, 'Dur', width=40)
            self.StateList.InsertColumn(7, 'Action', width=103)
            self.StateList.InsertColumn(8, 'Parameters', width=77)
        
        # Add all list items.
        list_index = 0
        for state_index in self.filter.state_indices:
            self.StateList.InsertStringItem(list_index, str(state_index))
            self.StateList.SetItemFont(list_index, self.list_font)
            
            self.update_row(list_index)
            
            list_index += 1
        
        self.update_colors()
        
        if self.filter.state_indices[0] == 0 and len(self.filter.state_indices) > 1:
            self.StateList.Select(1, True)
        elif len(self.filter.state_indices) > 0:
            self.StateList.Select(0, True)
            
        self.StateList.Thaw()
        
        wx.EndBusyCursor()
        
        
    def filter_select(self, event):
        self.filter_update(self.Filter.GetSelection())
    
    
    def filter_update(self, index):
        self.filter.update(index)
        self.build_statelist()
        self.tools_update()
        
    
    def set_selected_property(self, key, value):
        self.undo_add()
        
        parent = self.GetParent()
        for list_index in self.selected:
            state_index = self.filter.state_indices[list_index]
            if state_index > 0:
                state = self.filter.states[list_index]
                state[key] = value
                parent.set_modified(True)
        
        
    def update_selected_rows(self):
        for list_index in self.selected:
            self.update_row(list_index)


    def tools_update(self):
        # Only one state is selected, fill tools with state info.
        if len(self.selected) == 1:
            state = self.filter.states[self.selected[0]]
            state_index = self.filter.state_indices[self.selected[0]] 
            
            if state_index == 0:
                sprite_name = '-'
            else:
                sprite_name = self.patch.sprite_names[state['sprite']]
            sprite_frame = state['spriteFrame'] & ~self.FRAMEFLAG_LIT
            
            action_index = self.get_action_index_from_value(state['action'])
            
            self.SpriteIndex.ChangeValue(str(state['sprite']))
            self.SpriteName.SetLabel(sprite_name)
            self.FrameIndex.ChangeValue(str(sprite_frame))
            self.NextStateIndex.ChangeValue(str(state['nextState']))
            self.NextStateName.SetLabel(self.patch.get_state_name(state['nextState']))
            self.Duration.ChangeValue(str(state['duration']))
            self.Action.SetSelection(action_index)
            self.Parameter1.ChangeValue(str(state['parameter1']))
            self.Parameter2.ChangeValue(str(state['parameter2']))
            
            if state['spriteFrame'] & self.FRAMEFLAG_LIT != 0:
                self.AlwaysLit.SetValue(True)
            else:
                self.AlwaysLit.SetValue(False)
            
            # Do not allow state 0 to be edited.
            if state_index == 0:
                self.tools_set_state(False)
            else:
                self.tools_set_state(True)
            
            # Do not allow editing an action on a state that has none for non-extended patches.
            if self.patch.engine.extended == False:
                if state['action'] == 0:
                    self.Action.Disable()
                else:
                    self.Action.Enable()

        
        # Multiple states are selected, zero out all tools.
        else:
            self.SpriteIndex.ChangeValue('')
            self.SpriteName.SetLabel('')
            self.FrameIndex.ChangeValue('')
            self.NextStateIndex.ChangeValue('')
            self.NextStateName.SetLabel('')
            self.Duration.ChangeValue('')
            self.Action.Select(0)
            self.Parameter1.ChangeValue('')
            self.Parameter2.ChangeValue('')
            self.AlwaysLit.SetValue(False)
            self.Action.Enable()
            self.tools_set_state(True)
        
        self.update_sprite_preview()
        
        
    def update_sprite_preview(self):
        self.sprite = None
        
        if len(self.selected) == 1:
            state_index = self.filter.state_indices[self.selected[0]]
        else:
            state_index = -1
        
        if state_index != 0:
            sprite_index = self.SpriteIndex.GetValue()
            if sprite_index != '':
                sprite_name = self.patch.sprite_names[int(sprite_index)]
                    
                sprite_frame = self.FrameIndex.GetValue()
                if sprite_frame != '':
                    sprite_frame = int(sprite_frame)
                else:
                    sprite_frame = 0
                    
                self.SpritePreview.show_sprite(sprite_name, sprite_frame)
                
    
    def select_sprite(self, event):
        if len(self.selected) == 1:
            sprite_index = int(self.SpriteIndex.GetValue())
            frame_index = int(self.FrameIndex.GetValue())
            
            self.sprites_dialog.set_state(self.patch, self.pwads, sprite_index, frame_index=frame_index)
        elif len(self.selected) > 1:
            state = self.filter.states[self.selected[0]]
            self.sprites_dialog.set_state(self.patch, self.pwads, state['sprite'])
            
        self.sprites_dialog.ShowModal()
        
        if self.sprites_dialog.selected_sprite != -1:
            sprite_index = self.sprites_dialog.selected_sprite
            frame_index = self.sprites_dialog.selected_frame
            
            self.SpriteIndex.ChangeValue(str(sprite_index))
            self.set_selected_property('sprite', sprite_index)
            
            if frame_index != -1:
                self.FrameIndex.ChangeValue(str(frame_index))
                
                # Update sprite frames separately to mix in lit flag.
                for list_index in self.selected:
                    state = self.filter.states[list_index]
                    state['spriteFrame'] = frame_index | (state['spriteFrame'] & self.FRAMEFLAG_LIT)
            
            self.update_selected_rows()
            self.update_colors()
            self.update_sprite_preview()
    
    
    def set_value(self, event):        
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
        
        self.update_selected_rows()
        self.update_sprite_preview()
        self.GetParent().set_modified(True)
        
        if window_id == windows.STATES_SPRITE:
            self.update_colors()
        

    def set_lit(self, event):
        self.undo_add()
        
        checked = self.AlwaysLit.GetValue()
         
        for list_index in self.selected:
            state = self.filter.states[list_index]
            frame_index = state['spriteFrame'] & ~self.FRAMEFLAG_LIT
            if checked == True:
                frame_index |= self.FRAMEFLAG_LIT
            
            state['spriteFrame'] = frame_index
    
        self.update_selected_rows()
        self.GetParent().set_modified(True)
        
    
    def set_action(self, event):
        self.undo_add()
        
        value = self.Action.GetStringSelection()
        action_value = self.get_action_value_from_name(value)
        
        for list_index in self.selected:
            state = self.filter.states[list_index]
            if self.patch.engine.extended == True:
                state['action'] = action_value
            else:
                if state['action'] != 0:
                    state['action'] = action_value
        
        self.update_selected_rows()
        self.GetParent().set_modified(True)
            
    
    def set_frame(self, event):
        self.undo_add()
        
        window = self.FindWindowById(event.GetId())
        value = utils.validate_numeric(window)
        
        if value < 0:
            value = 0
        elif value > 29:
            value = 29
        
        if window.GetValue() != str(value):
            window.ChangeValue(str(value))
        
        for list_index in self.selected:
            state = self.filter.states[list_index]
            state['spriteFrame'] = value | (state['spriteFrame'] & self.FRAMEFLAG_LIT)
            
        self.update_selected_rows()
        self.update_sprite_preview()
        self.GetParent().set_modified(True)
        
        
    def get_action_value_from_name(self, action_name):
        if action_name == '':
            if self.patch.engine.extended == True:
                return 'NULL'
            else:
                return 0
        
        return self.patch.engine.get_action_from_name(action_name)
    
    
    def get_action_name_from_value(self, action_value):
        # Determine action string based on extended mode.
        # NULL\0 is displayed as an empty string.
        if self.patch.engine.extended == True:
            if action_value == 'NULL':
                return ''
            else:
                return str(action_value)
            
        else:
            if action_value == 0:
                return ''
            else:
                return self.patch.engine.actions[str(action_value)]['name']
        
        return None
    
    
    def get_action_index_from_value(self, action_value):
        if self.patch.engine.extended == True:
            return self.patch.engine.actions.keys().index(action_value)
        else:
            return self.patch.engine.actions.keys().index(str(action_value)) 
        
    
    def update_row(self, list_index):
        state_index = self.filter.state_indices[list_index]
        state = self.filter.states[list_index]

        if (state['spriteFrame'] & self.FRAMEFLAG_LIT) != 0:
            lit = 'X'
        else:
            lit = ''
            
        parameters = str(state['parameter1']) + ', ' + str(state['parameter2'])
        action = self.get_action_name_from_value(state['action'])
        
        # Fill out column strings.
        self.StateList.SetStringItem(list_index, 1, self.patch.get_state_name(state_index))
        self.StateList.SetStringItem(list_index, 2, str(state['sprite']))
        self.StateList.SetStringItem(list_index, 3, str(state['spriteFrame'] & ~self.FRAMEFLAG_LIT))
        self.StateList.SetStringItem(list_index, 4, lit)
        self.StateList.SetStringItem(list_index, 5, str(state['nextState']))
        self.StateList.SetStringItem(list_index, 6, str(state['duration']))
        self.StateList.SetStringItem(list_index, 7, action)
        self.StateList.SetStringItem(list_index, 8, parameters)
    
    
    def update_colors(self):
        color_index = 0
        previous_sprite = 0
        list_index = 0
        
        self.StateList.Freeze()
        
        for state in self.filter.states:
            if state['sprite'] != previous_sprite:
                color_index += 1
                if color_index == len(self.SPRITE_COLOURS):
                    color_index = 0
            
            self.StateList.SetItemBackgroundColour(list_index, self.SPRITE_COLOURS[color_index])
            
            list_index += 1
            previous_sprite = state['sprite']
            
        self.StateList.Thaw()
    
    
    def selection_get_state_index(self):
        if len(self.selected) == 0:
            return -1
        
        return self.filter.state_indices[self.selected[0]]
    
    
    def selection_clear(self):
        self.StateList.Freeze()
        
        for list_index in self.selected:
            self.StateList.Select(list_index, False)    
        
        self.StateList.Thaw()
    
        
    def frame_spin_up(self, event):
        if self.FrameIndex.GetValue() == '':
            self.FrameIndex.SetValue('0')
        else:
            index = int(self.FrameIndex.GetValue())
            self.FrameIndex.SetValue(str(index + 1))
    
    
    def frame_spin_down(self, event):
        if self.FrameIndex.GetValue() == '':
            self.FrameIndex.SetValue('0')
        else:
            index = int(self.FrameIndex.GetValue())
            self.FrameIndex.SetValue(str(index - 1))
    
    
    def goto_next_state(self, event):
        if len(self.selected) == 0:
            return
        
        state = self.filter.states[self.selected[0]]
        self.goto_state_index(state['nextState'])
        
    
    def goto_state_index(self, state_index, filter_type=None, filter_index=None):
        if filter_type is not None:
            index = self.filter.find_index(filter_type, filter_index)
            self.filter_update(index)
            self.Filter.Select(index)
        else:
            if not state_index in self.filter.state_indices:
                self.filter_update(0)
                self.Filter.Select(0)
            
        filter_index = self.filter.state_indices.index(state_index)
            
        self.selection_clear()
        self.StateList.Select(filter_index, True)
        self.StateList.EnsureVisible(filter_index)
        self.StateList.SetFocus()