#!/usr/bin/env python
#coding=utf8

from whacked4 import utils
from whacked4.dehacked import statefilter
from whacked4.ui import editormixin, windows
from whacked4.ui.dialogs import statepreviewdialog

import whacked4.config as config

import copy
import wx


class ThingsFrame(editormixin.EditorMixin, windows.ThingsFrameBase):
    """
    Things editor window.
    """

    # Text control to internal key mappings.
    PROPS_VALUES = {
        windows.THING_VAL_ID: 'id',
        windows.THING_VAL_HEALTH: 'health',
        windows.THING_VAL_GIBHEALTH: 'gibHealth',
        windows.THING_VAL_SPEED: 'speed',
        windows.THING_VAL_RADIUS: 'radius',
        windows.THING_VAL_HEIGHT: 'height',
        windows.THING_VAL_DAMAGE: 'damage',
        windows.THING_VAL_REACTIONTIME: 'reactionTime',
        windows.THING_VAL_PAINCHANCE: 'painChance',
        windows.THING_VAL_MASS: 'mass',
        windows.THING_VAL_GAME: 'game',
        windows.THING_VAL_SPAWNID: 'spawnId',
        windows.THING_VAL_RESPAWNTIME: 'respawnTime',
        windows.THING_VAL_RENDERSTYLE: 'renderStyle',
        windows.THING_VAL_ALPHA: 'alpha',
        windows.THING_VAL_SCALE: 'scale',
        windows.THING_VAL_DECAL: 'decal',
        windows.THING_VAL_DAMAGEFACTOR: 'damageFactor',
        windows.THING_VAL_GRAVITY: 'gravity',
    }

    # Value types for text control validation.
    PROPS_VALUE_TYPES = {
        windows.THING_VAL_ID: 'int',
        windows.THING_VAL_HEALTH: 'int',
        windows.THING_VAL_GIBHEALTH: 'int',
        windows.THING_VAL_SPEED: 'int',
        windows.THING_VAL_RADIUS: 'fixed',
        windows.THING_VAL_HEIGHT: 'fixed',
        windows.THING_VAL_DAMAGE: 'int',
        windows.THING_VAL_REACTIONTIME: 'int',
        windows.THING_VAL_PAINCHANCE: 'int',
        windows.THING_VAL_MASS: 'int',
        windows.THING_VAL_GAME: 'int',
        windows.THING_VAL_SPAWNID: 'int',
        windows.THING_VAL_RESPAWNTIME: 'int',
        windows.THING_VAL_RENDERSTYLE: 'int',
        windows.THING_VAL_ALPHA: 'float',
        windows.THING_VAL_SCALE: 'float',
        windows.THING_VAL_DECAL: 'str',
        windows.THING_VAL_DAMAGEFACTOR: 'float',
        windows.THING_VAL_GRAVITY: 'float',
    }

    # State text control to partial internal key mappings.
    PROPS_STATES = {
        windows.THING_STATE_SPAWN: 'Spawn',
        windows.THING_STATE_WALK: 'Walk',
        windows.THING_STATE_PAIN: 'Pain',
        windows.THING_STATE_MELEE: 'Melee',
        windows.THING_STATE_ATTACK: 'Attack',
        windows.THING_STATE_DEATH: 'Death',
        windows.THING_STATE_EXPLODE: 'Explode',
        windows.THING_STATE_RAISE: 'Raise',
        windows.THING_STATE_CRASH: 'Crash',
        windows.THING_STATE_FREEZE: 'Freeze',
        windows.THING_STATE_BURN: 'Burn'
    }

    # State name label to partial internal key mappings.
    PROPS_STATENAMES = {
        windows.THING_STATENAME_SPAWN: 'Spawn',
        windows.THING_STATENAME_WALK: 'Walk',
        windows.THING_STATENAME_PAIN: 'Pain',
        windows.THING_STATENAME_MELEE: 'Melee',
        windows.THING_STATENAME_ATTACK: 'Attack',
        windows.THING_STATENAME_DEATH: 'Death',
        windows.THING_STATENAME_EXPLODE: 'Explode',
        windows.THING_STATENAME_RAISE: 'Raise',
        windows.THING_STATENAME_CRASH: 'Crash',
        windows.THING_STATENAME_FREEZE: 'Freeze',
        windows.THING_STATENAME_BURN: 'Burn'
    }

    # State set button to partial internal key mappings.
    PROPS_STATESET = {
        windows.THING_STATESET_SPAWN: windows.THING_STATE_SPAWN,
        windows.THING_STATESET_WALK: windows.THING_STATE_WALK,
        windows.THING_STATESET_PAIN: windows.THING_STATE_PAIN,
        windows.THING_STATESET_MELEE: windows.THING_STATE_MELEE,
        windows.THING_STATESET_ATTACK: windows.THING_STATE_ATTACK,
        windows.THING_STATESET_DEATH: windows.THING_STATE_DEATH,
        windows.THING_STATESET_EXPLODE: windows.THING_STATE_EXPLODE,
        windows.THING_STATESET_RAISE: windows.THING_STATE_RAISE,
        windows.THING_STATESET_CRASH: windows.THING_STATE_CRASH,
        windows.THING_STATESET_FREEZE: windows.THING_STATE_FREEZE,
        windows.THING_STATESET_BURN: windows.THING_STATE_BURN
    }

    # Sound text control to partial internal key mappings.
    PROPS_SOUNDS = {
        windows.THING_SOUND_ALERT: 'Alert',
        windows.THING_SOUND_ATTACK: 'Attack',
        windows.THING_SOUND_PAIN: 'Pain',
        windows.THING_SOUND_DEATH: 'Death',
        windows.THING_SOUND_ACTIVE: 'Active'
    }

    # Sound set button to partial internal key mappings.
    PROPS_SOUNDSET = {
        windows.THING_SOUNDSET_ALERT: windows.THING_SOUND_ALERT,
        windows.THING_SOUNDSET_ATTACK: windows.THING_SOUND_ATTACK,
        windows.THING_SOUNDSET_PAIN: windows.THING_SOUND_PAIN,
        windows.THING_SOUNDSET_DEATH: windows.THING_SOUND_DEATH,
        windows.THING_SOUNDSET_ACTIVE: windows.THING_SOUND_ACTIVE
    }

    # State name label to partial internal key mappings.
    PROPS_SOUNDNAMES = {
        windows.THING_SOUNDNAME_ALERT: 'Alert',
        windows.THING_SOUNDNAME_ATTACK: 'Attack',
        windows.THING_SOUNDNAME_PAIN: 'Pain',
        windows.THING_SOUNDNAME_DEATH: 'Death',
        windows.THING_SOUNDNAME_ACTIVE: 'Active'
    }

    # Fixed point unit divisor for certain thing properties.
    FIXED_UNIT = 0x10000

    def __init__(self, params):
        windows.ThingsFrameBase.__init__(self, params)
        editormixin.EditorMixin.__init__(self)

        self.SetIcon(wx.Icon('res/editor-things.ico'))

        self.patch = None
        self.pwads = None
        self.clipboard = None
        self.preview_dialog = None

        self.selected_index = 0
        self.thing_is_projectile = False

        self.thingflag_mnemonics = None

        for prop in self.PROPS_STATENAMES.keys():
            item = self.FindWindowById(prop)
            item.SetFont(config.FONT_MONOSPACED_BOLD)

        for prop in self.PROPS_SOUNDNAMES.keys():
            item = self.FindWindowById(prop)
            item.SetFont(config.FONT_MONOSPACED_BOLD)

    def build(self, patch):
        """
        @see EditorMixin.build
        """

        self.patch = patch
        self.pwads = self.GetParent().pwads
        self.clipboard = None
        self.preview_dialog = statepreviewdialog.StatePreviewDialog(self.GetParent())

        self.selected_index = 0

        self.thingflag_mnemonics = None

        self.set_feature_visibility()
        self.flaglist_build()
        self.thinglist_build()
        self.game_build()
        self.renderstyle_build()

    def update(self):
        """
        @see: EditorMixin.update
        """

        self.pwads = self.GetParent().pwads

    def set_feature_visibility(self):
        """
        Sets the visibility of controls based on enabled engine features.
        """

        features = self.patch.engine.features

        self.PanelDamageFactor.Show(('thing.damageFactor' in features))
        self.PanelGravity.Show(('thing.gravity' in features))
        self.PanelGame.Show(('thing.game' in features))
        self.PanelGibHealth.Show(('thing.gibHealth' in features))
        self.PanelSpawnID.Show(('thing.spawnId' in features))
        self.PanelRespawnTime.Show(('thing.respawnTime' in features))
        self.PanelRenderStyle.Show(('thing.renderStyle' in features))
        self.PanelAlpha.Show(('thing.alpha' in features))
        self.PanelScale.Show(('thing.scale' in features))
        self.PanelDecal.Show(('thing.decal' in features))

        self.PanelStateCrash.Show(('thing.stateCrash' in features))
        self.PanelStateFreeze.Show(('thing.stateFreeze' in features))
        self.PanelStateBurn.Show(('thing.stateBurn' in features))

        self.Layout()

    def game_build(self):
        """
        Builds the list of game types.
        """

        self.ThingGame.Clear()
        self.ThingGame.AppendItems([
            'Any',
            'Doom',
            'Heretic',
            'Hexen',
            'Raven'
        ])

    def renderstyle_build(self):
        """
        Builds the list of render styles.
        """

        self.ThingRenderStyle.Clear()
        self.ThingRenderStyle.AppendItems(list(self.patch.engine.render_styles.values()))

    def thinglist_build(self):
        """
        Builds the thing names list from scratch.
        """

        self.ThingList.ClearAll()

        if self.ThingList.GetColumnCount() == 0:
            self.ThingList.InsertColumn(0, 'Idx', width=36)
            self.ThingList.InsertColumn(1, 'Name', width=225)
            self.ThingList.InsertColumn(2, 'ID', width=46)
            self.ThingList.InsertColumn(3, 'Game', width=50)

        for index in range(len(self.patch.things.names)):
            self.ThingList.InsertItem(index, '')
            self.thinglist_update_row(index)

        self.list_autosize(self.ThingList)
        self.ThingList.Select(0, True)

    def thinglist_update_row(self, row_index):
        """
        Updates a thing name in the list.
        """

        thing = self.patch.things[row_index]
        thing_name = self.patch.things.names[row_index]

        self.ThingList.SetItemText(row_index, str(row_index + 1))
        self.ThingList.SetItem(row_index, 1, thing_name)
        self.ThingList.SetItem(row_index, 2, str(thing['id']))
        self.ThingList.SetItem(row_index, 3, thing['game'])

    def thinglist_resize(self, event):
        """
        Resizes the thing name column to match the control's width.
        """

        # ioanch 20160124: check bounds
        col_count = self.ThingList.GetColumnCount()
        columns_width = self.ThingList.GetColumnWidth(0) if col_count > 0 else 0
        if col_count > 3:
            columns_width += self.ThingList.GetColumnWidth(2) + self.ThingList.GetColumnWidth(3)

        width = self.ThingList.GetClientSize()[0] - columns_width - 4
        if col_count > 1:
            self.ThingList.SetColumnWidth(1, width)

    def flaglist_build(self):
        """
        Build the flags list from scratch.
        """

        flaglist = []
        self.thingflag_mnemonics = []

        for mnemonic, flag in self.patch.engine.things.flags.items():
            if 'alias' in flag:
                continue
            flaglist.append(' ' + flag['name'])
            self.thingflag_mnemonics.append(mnemonic)

        self.ThingFlags.SetItems(flaglist)

    def activate(self, event):
        """
        Called when this editor window is activated by the user.
        """

        # Call the editor mixin function that we are overriding.
        editormixin.EditorMixin.activate(self, event)

        if not self:
            return

        # Update the properties being displayed by this window, in case state or sound names have changed.
        self.update_properties()
        self.Layout()

    def edit_copy(self):
        """
        Copies the currently selected thing to this windows' clipboard.
        """

        self.clipboard = {
            'thing': self.patch.things[self.selected_index].clone(),
            'name': copy.copy(self.patch.things.names[self.selected_index])
        }

    def edit_paste(self):
        """
        Pastes the thing on this windows' clipboard over the currently selected thing.
        """

        if self.clipboard is None:
            return

        self.undo_add()

        dup = self.clipboard['thing'].clone()
        dup_name = copy.copy(self.clipboard['name'])

        # Copy references to newly duplicated thing.
        self.patch.things[self.selected_index] = dup
        self.patch.things.names[self.selected_index] = dup_name

        self.update_properties()
        self.is_modified(True)

    def update_properties(self):
        """
        Update the visible properties of the currently selected thing.
        """

        thing = self.patch.things[self.selected_index]
        renderstyle = self.patch.engine.render_styles[thing['renderStyle']]

        self.update_is_projectile()

        # Set basic property text control values.
        self.ThingId.ChangeValue(str(thing['id']))
        self.ThingHealth.ChangeValue(str(thing['health']))
        self.ThingGibHealth.ChangeValue(str(thing['gibHealth']))
        self.ThingRadius.ChangeValue(str(thing['radius'] / self.FIXED_UNIT))
        self.ThingHeight.ChangeValue(str(thing['height'] / self.FIXED_UNIT))
        self.ThingDamage.ChangeValue(str(thing['damage']))
        self.ThingReactionTime.ChangeValue(str(thing['reactionTime']))
        self.ThingPainChance.ChangeValue(str(thing['painChance']))
        self.ThingMass.ChangeValue(str(thing['mass']))
        self.ThingGame.SetSelection(self.ThingGame.FindString(thing['game']))
        self.ThingSpawnId.ChangeValue(str(thing['spawnId']))
        self.ThingRespawnTime.ChangeValue(str(thing['respawnTime']))
        self.ThingRenderStyle.SetSelection(self.ThingRenderStyle.FindString(renderstyle))
        self.ThingAlpha.ChangeValue(str(thing['alpha']))
        self.ThingScale.ChangeValue(str(thing['scale']))
        self.ThingDecal.ChangeValue(thing['decal'])
        self.ThingDamageFactor.ChangeValue(str(thing['damageFactor']))
        self.ThingGravity.ChangeValue(str(thing['gravity']))

        # Speed is in fixed point if this thing is a projectile, normal otherwise
        if self.thing_is_projectile:
            speed = thing['speed'] / self.FIXED_UNIT
        else:
            speed = thing['speed']
        self.ThingSpeed.ChangeValue(str(speed))

        # Set flags.
        flags = thing['flags']
        for index in range(self.ThingFlags.GetCount()):
            mnemonic = self.thingflag_mnemonics[index]
            checked = (mnemonic in flags)
            self.ThingFlags.Check(index, checked)

        # Set state and sound values.
        for name in self.PROPS_STATES.values():
            self.set_display_state(name)
        for name in self.PROPS_SOUNDS.values():
            self.set_display_sound(name)

        # Update name.
        self.thinglist_update_row(self.selected_index)

    def set_display_state(self, state_name):
        """
        Sets state control values based on the partial name of a state thing property.
        """

        thing = self.patch.things[self.selected_index]
        state_index = thing['state' + state_name]
        self.__dict__['ThingState' + state_name].ChangeValue(str(state_index))
        self.__dict__['ThingState' + state_name + 'Name'].SetLabel(self.patch.get_state_name(state_index))

    def set_display_sound(self, sound_name):
        """
        Sets sound control values based on the partial name of a sound thing property.
        """

        thing = self.patch.things[self.selected_index]
        sound_index = thing['sound' + sound_name]
        self.__dict__['ThingSound' + sound_name].ChangeValue(str(sound_index))
        self.__dict__['ThingSound' + sound_name + 'Name'].SetLabel(self.patch.get_sound_name(sound_index))

    def set_value(self, event):
        """
        Sets the currently selected thing's property value.

        Which thing property to change is determined by the text control's id and the PROPS_VALUES lookup table.
        """

        self.undo_add()

        window_id = event.GetId()
        window = self.FindWindowById(window_id)
        value_type = self.PROPS_VALUE_TYPES[window_id]
        if value_type == 'int':
            value = utils.validate_numeric(window)
        elif value_type == 'float' or value_type == 'fixed':
            value = utils.validate_numeric_float(window)
        else:
            value = window.GetValue()

        thing = self.patch.things[self.selected_index]

        # Apply fixed point divisor if the value needs it.
        # This is also necessary for the speed property if the thing is a projectile.
        key = self.PROPS_VALUES[window_id]
        if value_type == 'fixed':
            value *= self.FIXED_UNIT
        elif key == 'speed' and self.thing_is_projectile:
            value *= self.FIXED_UNIT

        thing[key] = value

        self.thinglist_update_row(self.selected_index)
        self.is_modified(True)

    def set_state(self, event):
        """
        Sets the currently selected thing's property value.

        Which thing property to change is determined by the text control's id and the PROPS_VALUES lookup table.
        """

        self.undo_add()

        window_id = event.GetId()
        window = self.FindWindowById(window_id)
        value = utils.validate_numeric(window)

        thing = self.patch.things[self.selected_index]

        # Clamp to valid state indices.
        if value < 0:
            value = 0
        if value >= len(self.patch.states):
            value = len(self.patch.states) - 1

        if str(value) != window.GetValue():
            window.ChangeValue(str(value))

        key = self.PROPS_STATES[window_id]
        thing['state' + key] = value
        self.__dict__['ThingState' + key + 'Name'].SetLabel(self.patch.get_state_name(value))
        self.is_modified(True)
        self.update_is_projectile()
        self.update_properties()

    def set_game(self, event):
        """
        Sets the currently selected thing's game property.
        """

        game = event.GetString()
        self.patch.things[self.selected_index]['game'] = game

        self.thinglist_update_row(self.selected_index)
        self.is_modified(True)

    def set_renderstyle(self, event):
        """
        Sets the currently selected thing's render style property.
        """

        index = event.GetSelection()
        renderstyle = self.patch.engine.render_styles.keys()[index]
        self.patch.things[self.selected_index]['renderStyle'] = renderstyle

        self.is_modified(True)

    def set_sound(self, event):
        """
        Sets the currently selected thing's sound index.

        Which sound to change is determined by the text control's id and the PROPS_SOUNDS lookup table.
        """

        self.undo_add()

        window_id = event.GetId()
        window = self.FindWindowById(window_id)
        value = utils.validate_numeric(window)

        thing = self.patch.things[self.selected_index]

        # Clamp to valid sound indices.
        if value < 0:
            value = 0
        if value > len(self.patch.sounds):
            value = len(self.patch.sounds)

        if str(value) != window.GetValue():
            window.ChangeValue(str(value))

        key = self.PROPS_SOUNDS[window_id]
        thing['sound' + key] = value
        self.__dict__['ThingSound' + key + 'Name'].SetLabel(self.patch.get_sound_name(value))
        self.is_modified(True)

    def set_flags(self, event):
        """
        Sets the currently selected thing's flags value.
        """

        self.undo_add()

        flags_set = set()

        # Iterate over the flags defined in the flags list, adding mnemonics that are set.
        for index in range(self.ThingFlags.GetCount()):
            if not self.ThingFlags.IsChecked(index):
                continue
            flags_set.add(self.thingflag_mnemonics[index])

        self.patch.things[self.selected_index]['flags'] = flags_set
        self.is_modified(True)

    def set_flag_tooltip(self, event):
        """
        Updates the tooltip displayed for the flags list when hovering over a flag.
        """

        index = self.ThingFlags.HitTest(wx.Point(event.GetX(), event.GetY()))
        if index != wx.NOT_FOUND:
            mnemonic = self.thingflag_mnemonics[index]
            tip = '{}\n\nMnemonic: {}'.format(self.patch.engine.things.flags[mnemonic]['description'], mnemonic)
        else:
            tip = ''

        self.ThingFlags.SetToolTip(tip)

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
        self.update_is_projectile()
        self.update_properties()

    def set_sound_external(self, event):
        """
        Sets a sound property based on the sound that is currently selected in the sounds editor.
        """

        self.undo_add()

        # Get a reference to the states editor window.
        parent = self.GetParent()
        sounds_frame = parent.editor_windows[windows.MAIN_TOOL_SOUNDS]

        text_ctrl = self.FindWindowById(self.PROPS_SOUNDSET[event.GetId()])
        text_ctrl.SetValue(str(sounds_frame.selected_row))
        self.is_modified(True)

    def thing_select(self, event):
        """
        Called when a thing is selected from the thing names list.
        """

        self.selected_index = event.GetIndex()
        self.thing_is_projectile = None
        self.update_properties()

    def thing_rename(self, event):
        """
        Called when the current thing needs to be renamed.
        """

        self.thing_rename_action()

    def thing_rename_action(self):
        """
        Renames the currently selected thing.
        """

        thing_name = self.patch.things.names[self.selected_index]
        new_name = wx.GetTextFromUser('Enter a new name for ' + thing_name, caption='Change name',
                                      default_value=thing_name, parent=self)

        if new_name != '':
            self.undo_add()

            self.patch.things.names[self.selected_index] = new_name

            self.update_properties()
            self.is_modified(True)

            parent = self.GetParent()
            parent.editor_windows[windows.MAIN_TOOL_STATES].update_filterlist()

    def thing_restore(self, event):
        """
        Restores the currently selected thing to the one stored in the engine configuration.
        """

        self.undo_add()

        self.patch.things[self.selected_index] = self.patch.engine.things[self.selected_index].clone()
        self.patch.things.names[self.selected_index] = copy.copy(self.patch.engine.things.names[self.selected_index])

        self.update_properties()
        self.is_modified(True)

    def goto_state_event(self, event):
        """
        Changes the selected state in the states editor window to the one of a thing's state property.
        """

        key = self.PROPS_STATENAMES[event.GetId()]
        state_index = self.patch.things[self.selected_index]['state' + key]

        self.goto_state(state_index, statefilter.FILTER_TYPE_THING, self.selected_index)

    def goto_sound_event(self, event):
        """
        Changes the selected sound in the sounds editor window to the one of a thing's sound property.
        """

        key = self.PROPS_SOUNDNAMES[event.GetId()]
        sound_index = self.patch.things[self.selected_index]['sound' + key]

        self.goto_sound(sound_index)

    def sound_play(self, event):
        """
        Plays a sound entry.
        """

        key = self.PROPS_SOUNDNAMES[event.GetId()]
        sound_index = self.patch.things[self.selected_index]['sound' + key]
        if sound_index == 0:
            return

        utils.sound_play(self.patch.sound_names[sound_index - 1], self.pwads)

    def undo_restore_item(self, item):
        """
        @see EditorMixin.undo_restore_item
        """

        index = item['index']

        self.patch.things[index] = item['item']
        self.patch.things.names[index] = item['name']

        self.thinglist_update_row(index)
        self.update_properties()

        self.is_modified(True)

    def undo_store_item(self):
        """
        @see EditorMixin.undo_store_item
        """

        return {
            'item': self.patch.things[self.selected_index].clone(),
            'name': copy.copy(self.patch.things.names[self.selected_index]),
            'index': self.selected_index
        }

    def thing_context(self, event):
        """
        Displays the context menu for things.
        """

        self.ThingList.PopupMenu(self.ThingContext, event.GetPosition())

    def thing_context_copy(self, event):
        """
        Context menu copy redirect.
        """
        self.edit_copy()

    def thing_context_paste(self, event):
        """
        Context menu paste redirect.
        """
        self.edit_paste()

    def thing_context_clear(self, event):
        """
        Clears a thing's properties.
        """

        self.undo_add()

        self.patch.things[self.selected_index] = self.patch.engine.empty_thing.clone()
        self.patch.things.names[self.selected_index] = 'Thing {}'.format(self.selected_index + 1)

        self.update_properties()
        self.is_modified(True)

    def preview_state(self, event):
        """
        Preview animation from a state.
        """

        key = self.PROPS_STATENAMES[event.GetId()]
        state_index = self.patch.things[self.selected_index]['state' + key]

        self.preview_dialog.prepare(self.pwads, self.patch, state_index, self.selected_index)
        self.preview_dialog.ShowModal()

    def update_is_projectile(self):
        """
        Updates the thing_is_projectile variable. If any of the current thing's states sets a momentum then it is no
        a projectile.
        """

        is_before = self.thing_is_projectile
        self.thing_is_projectile = True

        _, states = statefilter.filter_states(self.patch, statefilter.FILTER_TYPE_THING, self.selected_index)
        for state in states:
            if not state['action']:
                continue

            action = self.patch.engine.actions[state['action']]
            if 'setsMomentum' in action and action['setsMomentum']:
                self.thing_is_projectile = False

        # Cast speed property to the new type if needed.
        if is_before is not None and is_before != self.thing_is_projectile:
            thing = self.patch.things[self.selected_index]
            if self.thing_is_projectile:
                thing['speed'] *= ThingsFrame.FIXED_UNIT
            else:
                thing['speed'] /= ThingsFrame.FIXED_UNIT

    def before_save(self):
        self.update_is_projectile()