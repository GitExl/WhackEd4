#!/usr/bin/env python
#coding=utf8

from whacked4 import utils
from whacked4.dehacked import statefilter
from whacked4.ui import editormixin, windows
import copy
import wx


class WeaponsFrame(editormixin.EditorMixin, windows.WeaponsFrameBase):
    """
    Sounds editor window.
    """

    # Text control to internal key mappings.
    PROPS_VALUES = {
        windows.WEAPON_VAL_AMMO_USE: 'ammoUse',
        windows.WEAPON_VAL_MIN_AMMO: 'minAmmo',
        windows.WEAPON_VAL_DECAL: 'decal',
    }

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

    # State set button to partial internal key mappings.
    PROPS_STATESET = {
        windows.WEAPON_STATESET_SELECT: windows.WEAPON_STATE_SELECT,
        windows.WEAPON_STATESET_DESELECT: windows.WEAPON_STATE_DESELECT,
        windows.WEAPON_STATESET_BOB: windows.WEAPON_STATE_BOB,
        windows.WEAPON_STATESET_FIRE: windows.WEAPON_STATE_FIRE,
        windows.WEAPON_STATESET_MUZZLE: windows.WEAPON_STATE_MUZZLE
    }

    def __init__(self, params):
        windows.WeaponsFrameBase.__init__(self, params)
        editormixin.EditorMixin.__init__(self)

        self.SetIcon(wx.Icon('res/editor-weapons.ico'))

        self.patch = None
        self.selected_index = 0

    def build(self, patch):
        """
        @see: EditorMixin.build
        """

        self.patch = patch

        self.selected_index = 0

        self.set_feature_visibility()
        self.ammolist_build()
        self.weaponlist_build()

    def set_feature_visibility(self):
        """
        Sets the visibility of controls based on enabled engine features.
        """

        features = self.patch.engine.features

        self.PanelAmmoNeeded.Show(('weapon.minAmmo' in features))
        self.PanelDecal.Show(('weapon.decal' in features))
        self.PanelAmmoPerUse.Show(('weapon.ammoUse' in features))

        self.Layout()


    def activate(self, event):
        """
        Called when this editor window is activated by the user.
        """

        # Call the editor mixin function that we are overriding.
        editormixin.EditorMixin.activate(self, event)

        if self.IsBeingDeleted():
            return

        self.ammolist_build()
        self.update_properties()

    def weaponlist_build(self):
        """
        Builds the list of weapon names.
        """

        self.WeaponList.ClearAll()

        if self.WeaponList.GetColumnCount() == 0:
            self.WeaponList.InsertColumn(0, 'Name', width=120)
            self.WeaponList.InsertColumn(1, 'Ammo', width=120)

        for index in range(len(self.patch.weapons)):
            self.WeaponList.InsertStringItem(index, '')
            self.weaponlist_update_row(index)

        self.WeaponList.Select(0, True)

    def weaponlist_update_row(self, row_index):
        """
        Updates a row in the weapons list.
        """

        weapon = self.patch.weapons[row_index]
        weapon_name = self.patch.weapons.names[row_index]

        self.WeaponList.SetItemText(row_index, weapon_name)
        self.WeaponList.SetStringItem(row_index, 1, self.patch.get_ammo_name(weapon['ammoType']))

    def weaponlist_resize(self, event):
        """
        Resizes the weapon list to fill as much space as is available.
        """

        column_width = self.WeaponList.GetClientSizeTuple()[0] - 4
        self.WeaponList.SetColumnWidth(0, column_width / 2)
        self.WeaponList.SetColumnWidth(1, column_width / 2)

    def ammolist_build(self):
        """
        Builds the choice box with ammo types.
        """

        self.AmmoType.Clear()
        self.AmmoType.AppendItems(self.patch.ammo.names)
        self.AmmoType.Append('Unknown')
        self.AmmoType.Append('Infinite')

    def update_properties(self):
        """
        Updates the displayed properties of the currently selected thing.
        """

        weapon = self.patch.weapons[self.selected_index]

        self.AmmoType.Select(weapon['ammoType'])
        self.AmmoUse.SetValue(str(weapon['ammoUse']))
        self.MinAmmo.SetValue(str(weapon['minAmmo']))
        self.Decal.SetValue(weapon['decal'])

        self.WeaponStateSelect.ChangeValue(str(weapon['stateSelect']))
        self.WeaponStateDeselect.ChangeValue(str(weapon['stateDeselect']))
        self.WeaponStateBob.ChangeValue(str(weapon['stateBob']))
        self.WeaponStateFire.ChangeValue(str(weapon['stateFire']))
        self.WeaponStateMuzzle.ChangeValue(str(weapon['stateMuzzle']))

        # Set state values.
        for name in self.PROPS_STATES.values():
            self.set_display_state(name)

        self.WeaponList.SetItemText(self.selected_index, self.patch.weapons.names[self.selected_index])

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

    def set_value(self, event):
        """
        Sets the currently selected weapon entry's property value.
        """

        self.undo_add()

        window_id = event.GetId()
        window = self.FindWindowById(window_id)
        if window_id == windows.WEAPON_VAL_DECAL:
            value = window.GetValue()
        else:
            value = utils.validate_numeric(window)

        key = self.PROPS_VALUES[window_id]
        self.patch.weapons[self.selected_index][key] = value

        self.weaponlist_update_row(self.selected_index)
        self.is_modified(True)

    def set_ammo(self, event):
        """
        Update the ammo type for the currently selected weapon.
        """

        self.undo_add()

        ammo_index = self.AmmoType.GetSelection()
        self.patch.weapons[self.selected_index]['ammoType'] = ammo_index

        self.weaponlist_update_row(self.selected_index)
        self.is_modified(True)

    def set_state_external(self, event):
        """
        Sets a state property based on the state that is currently selected in the states editor.
        """

        self.undo_add()

        # Get a reference to the states editor window.
        parent = self.GetParent()
        states_frame = parent.editor_windows[windows.MAIN_TOOL_STATES]

        text_ctrl = self.FindWindowById(self.PROPS_STATESET[event.GetId()])
        text_ctrl.SetValue(str(states_frame.selection_get_state_index()))
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
        new_name = wx.GetTextFromUser('Enter a new name for ' + weapon_name, caption='Change name',
                                      default_value=weapon_name, parent=self)

        if new_name != '':
            self.undo_add()

            self.patch.weapons.names[self.selected_index] = new_name
            self.update_properties()
            self.is_modified(True)

    def weapon_restore(self, event):
        """
        Restores the selected weapon to it's engine state.
        """

        self.undo_add()

        self.patch.weapons[self.selected_index] = self.patch.engine.weapons[self.selected_index].clone()
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

        self.weaponlist_update_row(self.selected_index)
        self.update_properties()

        self.is_modified(True)

    def undo_store_item(self):
        """
        @see: EditorMixin.undo_store_item
        """

        return {
            'item': self.patch.weapons[self.selected_index].clone(),
            'name': copy.copy(self.patch.weapons.names[self.selected_index]),
            'index': self.selected_index
        }

    def goto_state_event(self, event):
        """
        Changes the selected state in the states editor window to the one of a weapon's state property.
        """

        key = self.PROPS_STATENAMES[event.GetId()]
        state_index = self.patch.weapons[self.selected_index]['state' + key]

        self.goto_state(state_index, statefilter.FILTER_TYPE_WEAPON, self.selected_index)

    def weapon_select(self, event):
        """
        Selects a new weapon from the list.
        """

        self.selected_index = event.GetIndex()
        self.update_properties()
