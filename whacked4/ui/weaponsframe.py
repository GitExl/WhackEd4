#!/usr/bin/env python
#coding=utf8

from dehacked import statefilter
from ui import editormixin, windows, utils
import copy
import wx


class WeaponsFrame(editormixin.EditorMixin, windows.WeaponsFrameBase):
    """
    Sounds editor window.
    """
    
    # State text control to partial internal key mappings.
    PROPS_STATES = {
        windows.WEAPON_STATE_SELECT: 'Select',
        windows.WEAPON_STATE_DESELECT: 'Deselect',
        windows.WEAPON_STATE_BOB: 'Bob',
        windows.WEAPON_STATE_FIRE: 'Fire',
        windows.WEAPON_STATE_MUZZLE: 'Muzzle'
    }
    
    # State name label to partial internal key mappings.
    PROPS_STATENAMES = {
        windows.WEAPON_STATENAME_SELECT: 'Select',
        windows.WEAPON_STATENAME_DESELECT: 'Deselect',
        windows.WEAPON_STATENAME_BOB: 'Bob',
        windows.WEAPON_STATENAME_FIRE: 'Fire',
        windows.WEAPON_STATENAME_MUZZLE: 'Muzzle'
    }
    
    def __init__(self, params):
        windows.WeaponsFrameBase.__init__(self, params)
        editormixin.EditorMixin.__init__(self)
        
        self.SetIcon(wx.Icon('res/icon-weapons-small.png'))


    def build(self, patch):
        """
        @see: EditorMixin.build
        """
        
        self.patch = patch
    
        self.selected_index = 0
    
        self.ammolist_build()
        self.weaponlist_build()
    
    
    def weaponlist_build(self):
        """
        Builds the list of weapon names.
        """
        
        self.WeaponList.Clear()
        self.WeaponList.AppendItems(self.patch.weapons.names)
        self.WeaponList.Select(0)
        
        self.update_properties()
    
    
    def ammolist_build(self):
        """
        Builds the choice box with ammo types.
        """
        
        self.AmmoType.Clear()
        self.AmmoType.AppendItems(self.patch.ammo.names)
        
        
    def update_properties(self):
        """
        Updates the displayed properties of the currently selected thing.
        """
        
        weapon = self.patch.weapons[self.selected_index]
        
        self.AmmoType.Select(weapon['ammoType'])
        self.WeaponStateSelect.ChangeValue(str(weapon['stateSelect']))
        self.WeaponStateDeselect.ChangeValue(str(weapon['stateDeselect']))
        self.WeaponStateBob.ChangeValue(str(weapon['stateBob']))
        self.WeaponStateFire.ChangeValue(str(weapon['stateFire']))
        self.WeaponStateMuzzle.ChangeValue(str(weapon['stateMuzzle']))
        
        # Set state values.
        for name in self.PROPS_STATES.values():
            self.set_display_state(name)
            
        self.WeaponList.SetString(self.selected_index, self.patch.weapons.names[self.selected_index])
        
        
    def set_state_index(self, event):
        """
        Sets the currently selected weapon's state.
        """

        self.undo_add()

        window_id = event.GetId()
        window = self.FindWindowById(window_id)
        value = utils.validate_numeric(window)
        
        # Clamp to valid state indices.
        if value < 0:
            value = 0
        if value >= len(self.patch.states):
            value = len(self.patch.states) - 1
            
        if str(value) != window.GetValue():
            window.ChangeValue(str(value))
        
        key = self.PROPS_STATES[window_id]
        self.patch.weapons[self.selected_index]['state' + key] = value
        self.__dict__['WeaponState' + key + 'Name'].SetLabel(self.patch.get_state_name(value))
        self.is_modified(True)
        
    
    def set_ammo(self, event):
        """
        Update the ammo type for the currently selected weapon.
        """
        
        self.undo_add()
        
        ammo_index = self.AmmoType.GetSelection()
        self.patch.weapons[self.selected_index]['ammoType'] = ammo_index
        self.is_modified(True)
        
        
    def set_display_state(self, state_name):
        """
        Sets state control values based on the partial name of a weapon state property.
        """
        
        state_index = self.patch.weapons[self.selected_index]['state' + state_name]
        self.__dict__['WeaponState' + state_name].ChangeValue(str(state_index))
        self.__dict__['WeaponState' + state_name + 'Name'].SetLabel(self.patch.get_state_name(state_index))


    def weapon_rename(self, event):
        """
        Called when the current weapon needs to be renamed.
        """
        
        self.weapon_rename_action()


    def weapon_rename_action(self):
        """
        Renames the currently selected thing.
        """
        
        weapon_name = self.patch.weapons.names[self.selected_index]
        new_name = wx.GetTextFromUser('Enter a new name for ' + weapon_name, caption='Change name', default_value=weapon_name, parent=self)
        
        if new_name != '':
            self.undo_add()
            
            self.patch.weapons.names[self.selected_index] = new_name
            self.WeaponList.SetString(self.selected_index, new_name)
            
            self.update_properties()
            self.is_modified(True)
            
            
    def weapon_restore(self, event):
        """
        Restores the selected weapon to it's engine state.
        """
        
        self.undo_add()
        
        self.patch.weapons[self.selected_index] = copy.deepcopy(self.patch.engine.weapons[self.selected_index])
        self.patch.weapons.names[self.selected_index] = copy.copy(self.patch.engine.weapons.names[self.selected_index])
        
        self.update_properties()
        self.is_modified(True)

        
    def undo_restore_item(self, item):
        """
        @see: EditorMixin.undo_restore_item
        """
        
        index = item['index']
        self.patch.weapons[index] = item['item']
        self.patch.weapons.names[index] = item['name']
        
        self.update_properties()
        
        
    def undo_store_item(self):
        """
        @see: EditorMixin.undo_store_item
        """
        
        return {
            'item': copy.deepcopy(self.patch.weapons[self.selected_index]),
            'name': copy.deepcopy(self.patch.weapons.names[self.selected_index]),
            'index': self.selected_index
        }
    
    
    def goto_state(self, event):
        """
        Changes the selected state in the states editor window to the one of a weapon's state property.
        """
        
        key = self.PROPS_STATENAMES[event.GetId()]
        state_index = self.patch.weapons[self.selected_index]['state' + key]
        
        self.goto_state_index(state_index, statefilter.FILTER_TYPE_WEAPON, self.selected_index)
    
    
    def weapon_select(self, event):
        self.selected_index = self.WeaponList.GetSelection()
        self.update_properties()
