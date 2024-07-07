"""
Weapon editor UI.
"""

from math import floor
from typing import Dict, Optional

import wx
from wx import Window, ActivateEvent, SizeEvent, CommandEvent, ListEvent, MouseEvent

from whacked4 import utils, config
from whacked4.dehacked.patch import Patch
from whacked4.doom.wadlist import WADList
from whacked4.ui import editormixin, windows
from whacked4.ui.dialogs import statepreviewdialog
from whacked4.ui.dialogs.statepreviewdialog import StatePreviewDialog
from whacked4.ui.editormixin import UndoItem
from whacked4.ui.editors import statesframe


class WeaponsFrame(editormixin.EditorMixin, windows.WeaponsFrameBase):
    """
    Sounds editor window.
    """

    # Text control to internal key mappings.
    PROPS_VALUES: Dict[int, str] = {
        windows.WEAPON_VAL_AMMO_USE: 'ammoUse',
        windows.WEAPON_VAL_MIN_AMMO: 'minAmmo',
        windows.WEAPON_VAL_DECAL: 'decal',
    }

    # State text control to partial internal key mappings.
    PROPS_STATES: Dict[int, str] = {
        windows.WEAPON_STATE_SELECT: 'Select',
        windows.WEAPON_STATE_DESELECT: 'Deselect',
        windows.WEAPON_STATE_BOB: 'Bob',
        windows.WEAPON_STATE_FIRE: 'Fire',
        windows.WEAPON_STATE_MUZZLE: 'Muzzle'
    }

    # State name label to partial internal key mappings.
    PROPS_STATENAMES: Dict[int, str] = {
        windows.WEAPON_STATENAME_SELECT: 'Select',
        windows.WEAPON_STATENAME_DESELECT: 'Deselect',
        windows.WEAPON_STATENAME_BOB: 'Bob',
        windows.WEAPON_STATENAME_FIRE: 'Fire',
        windows.WEAPON_STATENAME_MUZZLE: 'Muzzle'
    }

    # State set button to partial internal key mappings.
    PROPS_STATESET: Dict[int, int] = {
        windows.WEAPON_STATESET_SELECT: windows.WEAPON_STATE_SELECT,
        windows.WEAPON_STATESET_DESELECT: windows.WEAPON_STATE_DESELECT,
        windows.WEAPON_STATESET_BOB: windows.WEAPON_STATE_BOB,
        windows.WEAPON_STATESET_FIRE: windows.WEAPON_STATE_FIRE,
        windows.WEAPON_STATESET_MUZZLE: windows.WEAPON_STATE_MUZZLE
    }

    def __init__(self, parent: Window):
        windows.WeaponsFrameBase.__init__(self, parent)
        editormixin.EditorMixin.__init__(self)

        self.SetIcon(wx.Icon('res/editor-weapons.png'))

        self.patch: Optional[Patch] = None
        self.pwads: Optional[WADList] = None
        self.selected_index: int = 0
        self.preview_dialog: Optional[StatePreviewDialog] = None

        for prop_key in self.PROPS_STATENAMES:
            item = self.FindWindowById(prop_key)
            item.SetFont(config.FONT_MONOSPACED_BOLD)

    def build(self, patch: Patch):
        """
        @see: EditorMixin.build
        """

        self.patch = patch
        self.pwads = self.GetMDIParent().pwads
        self.selected_index = 0
        self.preview_dialog = statepreviewdialog.StatePreviewDialog(self.GetParent())

        self.set_feature_visibility()
        self.ammolist_build()
        self.weaponlist_build()

    def update(self):
        """
        @see: EditorMixin.update
        """

        self.pwads = self.GetMDIParent().pwads

    def set_feature_visibility(self):
        """
        Sets the visibility of controls based on enabled engine features.
        """

        features = self.patch.engine.features

        self.PanelAmmoNeeded.Show(('weapon.minAmmo' in features))
        self.PanelDecal.Show(('weapon.decal' in features))
        self.PanelAmmoPerUse.Show(('weapon.ammoUse' in features))

        self.Layout()

    def activate(self, event: ActivateEvent):
        """
        Called when this editor window is activated by the user.
        """

        # Call the editor mixin function that we are overriding.
        editormixin.EditorMixin.activate(self, event)

        if not self:
            return

        self.ammolist_build()
        self.update_properties()

    def weaponlist_build(self):
        """
        Builds the list of weapon names.
        """

        self.WeaponList.ClearAll()

        if self.WeaponList.GetColumnCount() == 0:
            self.WeaponList.InsertColumn(0, 'Name', width=floor(120 * self.GetDPIScaleFactor()))
            self.WeaponList.InsertColumn(1, 'Ammo', width=floor(120 * self.GetDPIScaleFactor()))

        for index in range(len(self.patch.weapons)):
            self.WeaponList.InsertItem(index, '')
            self.weaponlist_update_row(index)

        self.WeaponList.Select(0, True)

    def weaponlist_update_row(self, row_index: int):
        """
        Updates a row in the weapons list.
        """

        weapon = self.patch.weapons[row_index]

        self.WeaponList.SetItemText(row_index, weapon.name)
        self.WeaponList.SetItem(row_index, 1, self.patch.get_ammo_name(weapon['ammoType']))

    def weaponlist_resize(self, event: SizeEvent):
        """
        Resizes the weapon list to fill as much space as is available.
        """
        if not self.WeaponList.GetColumnCount():
            return

        column_width = self.WeaponList.GetClientSize()[0] - 4
        self.WeaponList.SetColumnWidth(0, column_width // 2)
        self.WeaponList.SetColumnWidth(1, column_width // 2)

    def ammolist_build(self):
        """
        Builds the choice box with ammo types.
        """

        self.AmmoType.Clear()
        for ammo in self.patch.ammo:
            self.AmmoType.Append(ammo.name)
        self.AmmoType.Append('Unknown')
        self.AmmoType.Append('Infinite')

    def update_properties(self):
        """
        Updates the displayed properties of the currently selected thing.
        """

        if not self.patch:
            return

        weapon = self.patch.weapons[self.selected_index]

        self.AmmoType.Select(weapon['ammoType'])

        self.WeaponStateSelect.ChangeValue(str(weapon['stateSelect']))
        self.WeaponStateDeselect.ChangeValue(str(weapon['stateDeselect']))
        self.WeaponStateBob.ChangeValue(str(weapon['stateBob']))
        self.WeaponStateFire.ChangeValue(str(weapon['stateFire']))
        self.WeaponStateMuzzle.ChangeValue(str(weapon['stateMuzzle']))

        if 'weapon.ammoUse' in self.patch.engine.features:
            self.AmmoUse.ChangeValue(str(weapon['ammoUse']))
        if 'weapon.minAmmo' in self.patch.engine.features:
            self.MinAmmo.ChangeValue(str(weapon['minAmmo']))
        if 'weapon.decal' in self.patch.engine.features:
            self.Decal.ChangeValue(weapon['decal'])

        # Set state values.
        for name in self.PROPS_STATES.values():
            self.set_display_state(name)

        self.WeaponList.SetItemText(
            self.selected_index,
            self.patch.weapons[self.selected_index].name
        )

    def set_state_index(self, event: CommandEvent):
        """
        Sets the currently selected weapon's state.
        """

        self.undo_add()

        window_id = event.GetId()
        window = self.FindWindowById(window_id)
        value = utils.validate_numeric(window)

        weapon = self.patch.weapons[self.selected_index]

        # Clamp to valid state indices.
        value = max(0, min(value, len(self.patch.states) - 1))

        if str(value) != window.GetValue():
            window.ChangeValue(str(value))

        key = self.PROPS_STATES[window_id]
        weapon['state' + key] = value
        self.__dict__['WeaponState' + key + 'Name'].SetLabel(self.patch.get_state_name(value))
        self.is_modified(True)

    def set_value(self, event: CommandEvent):
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

        if str(value) != window.GetValue():
            window.ChangeValue(str(value))

        key = self.PROPS_VALUES[window_id]
        self.patch.weapons[self.selected_index][key] = value

        self.weaponlist_update_row(self.selected_index)
        self.is_modified(True)

    def set_ammo(self, event: ListEvent):
        """
        Update the ammo type for the currently selected weapon.
        """

        self.undo_add()

        ammo_index = self.AmmoType.GetSelection()
        self.patch.weapons[self.selected_index]['ammoType'] = ammo_index

        self.weaponlist_update_row(self.selected_index)
        self.is_modified(True)

    def set_state_external(self, event: CommandEvent):
        """
        Sets a state property based on the state that is currently selected in
        the state editor.
        """

        self.undo_add()

        # Get a reference to the states editor window.
        parent = self.GetMDIParent()
        states_frame = parent.editor_windows[windows.MAIN_TOOL_STATES]

        text_ctrl = self.FindWindowById(self.PROPS_STATESET[event.GetId()])
        text_ctrl.SetValue(str(states_frame.get_selected_state_index()))
        self.is_modified(True)

    def set_display_state(self, state_name: str):
        """
        Sets state control values based on the partial name of a weapon state property.
        """

        state_key = 'state' + state_name
        state_index = self.patch.weapons[self.selected_index][state_key]
        label = self.patch.get_state_name(state_index)
        self.__dict__['WeaponState' + state_name].ChangeValue(str(state_index))
        self.__dict__['WeaponState' + state_name + 'Name'].SetLabel(label)

    def weapon_rename(self, event: CommandEvent):
        """
        Called when the current weapon needs to be renamed.
        """

        self.weapon_rename_action()

    def weapon_rename_action(self):
        """
        Renames the currently selected thing.
        """

        weapon_name = self.patch.weapons[self.selected_index].name
        new_name = wx.GetTextFromUser(
            'Enter a new name for ' + weapon_name,
            caption='Change name',
            default_value=weapon_name,
            parent=self
        )

        if new_name != '':
            self.undo_add()

            self.patch.weapons[self.selected_index].name = new_name
            self.update_properties()
            self.is_modified(True)

    def weapon_restore(self, event: CommandEvent):
        """
        Restores the selected weapon to its engine state.
        """

        self.undo_add()

        weapon_clone = self.patch.engine.weapons[self.selected_index].clone()
        self.patch.weapons[self.selected_index] = weapon_clone

        self.update_properties()
        self.is_modified(True)

    def undo_restore_item(self, item: UndoItem):
        """
        @see: EditorMixin.undo_restore_item
        """

        index = item['index']
        self.patch.weapons[index] = item['item']

        self.weaponlist_update_row(self.selected_index)
        self.update_properties()

        self.is_modified(True)

    def undo_store_item(self) -> UndoItem:
        """
        @see: EditorMixin.undo_store_item
        """

        return {
            'item': self.patch.weapons[self.selected_index].clone(),
            'index': self.selected_index
        }

    def goto_state_event(self, event: MouseEvent):
        """
        Changes the selected state in the states editor window to the one of a weapon's
        state property.
        """

        key = self.PROPS_STATENAMES[event.GetId()]
        state_index = self.patch.weapons[self.selected_index]['state' + key]

        self.goto_state(state_index, statesframe.FILTER_TYPE_WEAPON, self.selected_index)

    def weapon_select(self, event: ListEvent):
        """
        Selects a new weapon from the list.
        """

        self.selected_index = event.GetIndex()
        self.update_properties()

    def preview_state(self, event: MouseEvent):
        """
        Preview animation from a state.
        """

        key = self.PROPS_STATENAMES[event.GetId()]
        weapon = self.patch.weapons[self.selected_index]
        state_index = weapon['state' + key]

        self.preview_dialog.prepare(
            self.pwads,
            self.patch,
            state_index,
            weapon_index=self.selected_index
        )
        self.preview_dialog.ShowModal()
