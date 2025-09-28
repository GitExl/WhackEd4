"""
Thing editor UI.
"""

from math import floor
from typing import List, Tuple, Dict, Set, Optional

import wx
from wx import Window, SizeEvent, ActivateEvent, CommandEvent, ListEvent, MouseEvent, MenuEvent

from whacked4 import utils, config
from whacked4.dehacked.entries import ThingEntry
from whacked4.dehacked.entry import Entry
from whacked4.dehacked.patch import Patch
from whacked4.dehacked.statequery.query import StateFilterQuery
from whacked4.dehacked.statequery.stateindexsort import StateIndexSort
from whacked4.dehacked.statequery.thingfilter import ThingStateFilter
from whacked4.dehacked.table import ThingFlag
from whacked4.doom.wadlist import WADList
from whacked4.ui import editormixin, windows
from whacked4.ui.dialogs.statepreviewdialog import StatePreviewDialog
from whacked4.ui.editormixin import UndoItem
from whacked4.ui.editors import statesframe


class ThingsFrame(editormixin.EditorMixin, windows.ThingsFrameBase):
    """
    Things editor window.
    """

    # Text control to internal key mappings.
    PROPS_VALUES: Dict[int, str] = {
        windows.THING_VAL_NAME: 'name',
        windows.THING_VAL_OBIT_NAME: 'obituaryName',
        windows.THING_VAL_OBIT_NAME_PLURAL: 'obituaryNamePlural',
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
        windows.THING_VAL_DROPPED_ITEM_ID: 'droppedItemId',
        windows.THING_VAL_PICKUP_RADIUS: 'pickupRadius',
        windows.THING_VAL_PROJECTILE_PASS_HEIGHT: 'projectilePassHeight',
        windows.THING_VAL_FULLBRIGHT: 'fullbright',
        windows.THING_VAL_BLOOD_ID: 'bloodId',
        windows.THING_VAL_SHADOW_OFFSET: 'shadowOffset',
    }

    # Value types for text control validation.
    PROPS_VALUE_TYPES: Dict[int, str] = {
        windows.THING_VAL_NAME: 'str',
        windows.THING_VAL_OBIT_NAME: 'str',
        windows.THING_VAL_OBIT_NAME_PLURAL: 'str',
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
        windows.THING_VAL_DROPPED_ITEM_ID: 'int',
        windows.THING_VAL_PICKUP_RADIUS: 'fixed',
        windows.THING_VAL_PROJECTILE_PASS_HEIGHT: 'fixed',
        windows.THING_VAL_FULLBRIGHT: 'bool',
        windows.THING_VAL_BLOOD_ID: 'int',
        windows.THING_VAL_SHADOW_OFFSET: 'fixed',
    }

    # State text control to partial internal key mappings.
    PROPS_STATES: Dict[int, str] = {
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
    PROPS_STATENAMES: Dict[int, str] = {
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
    PROPS_STATESET: Dict[int, int] = {
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
    PROPS_SOUNDS: Dict[int, str] = {
        windows.THING_SOUND_ALERT: 'Alert',
        windows.THING_SOUND_ATTACK: 'Attack',
        windows.THING_SOUND_PAIN: 'Pain',
        windows.THING_SOUND_DEATH: 'Death',
        windows.THING_SOUND_ACTIVE: 'Active'
    }

    # Sound set button to partial internal key mappings.
    PROPS_SOUNDSET: Dict[int, int] = {
        windows.THING_SOUNDSET_ALERT: windows.THING_SOUND_ALERT,
        windows.THING_SOUNDSET_ATTACK: windows.THING_SOUND_ATTACK,
        windows.THING_SOUNDSET_PAIN: windows.THING_SOUND_PAIN,
        windows.THING_SOUNDSET_DEATH: windows.THING_SOUND_DEATH,
        windows.THING_SOUNDSET_ACTIVE: windows.THING_SOUND_ACTIVE
    }

    # State name label to partial internal key mappings.
    PROPS_SOUNDNAMES: Dict[int, str] = {
        windows.THING_SOUNDNAME_ALERT: 'Alert',
        windows.THING_SOUNDNAME_ATTACK: 'Attack',
        windows.THING_SOUNDNAME_PAIN: 'Pain',
        windows.THING_SOUNDNAME_DEATH: 'Death',
        windows.THING_SOUNDNAME_ACTIVE: 'Active'
    }

    # Fixed point unit divisor for certain thing properties.
    FIXED_UNIT = 0x10000

    def __init__(self, parent: Window):
        windows.ThingsFrameBase.__init__(self, parent)
        editormixin.EditorMixin.__init__(self)

        self.SetIcon(wx.Icon('res/editor-things.png'))

        self.patch: Optional[Patch] = None
        self.pwads: Optional[WADList] = None
        self.clipboard: Optional[Entry] = None
        self.preview_dialog: Optional[StatePreviewDialog] = None

        self.selected_index: int = 0
        self.thing_is_projectile: bool = False

        self.thingflag_mnemonics: List[Tuple[str, ThingFlag]] = []

        for prop in self.PROPS_STATENAMES:
            item = self.FindWindowById(prop)
            item.SetFont(config.FONT_MONOSPACED_BOLD)

        for prop in self.PROPS_SOUNDNAMES:
            item = self.FindWindowById(prop)
            item.SetFont(config.FONT_MONOSPACED_BOLD)

    def build(self, patch: Patch):
        """
        @see EditorMixin.build
        """

        self.patch = patch
        self.pwads = self.GetMDIParent().pwads
        self.clipboard = None
        self.preview_dialog = StatePreviewDialog(self.GetParent())

        self.selected_index = 0

        self.set_feature_visibility()
        self.flaglist_build()
        self.thinglist_build()
        self.game_build()
        self.renderstyle_build()

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

        self.PanelObituaryName.Show(('thing.obituaryName' in features))
        self.PanelObituaryNamePlural.Show(('thing.obituaryNamePlural' in features))
        self.PanelDamageFactor.Show(('thing.damageFactor' in features))
        self.PanelGravity.Show(('thing.gravity' in features))
        self.PanelGame.Show(('thing.game' in features))
        self.PanelGibHealth.Show(('thing.gibHealth' in features))
        self.PanelDroppedItemID.Show(('thing.droppedItemId' in features))
        self.PanelPickupRadius.Show(('thing.pickupRadius' in features))
        self.PanelProjectilePassHeight.Show(('thing.projectilePassHeight' in features))
        self.PanelFullbright.Show(('thing.fullbright' in features))
        self.PanelSpawnID.Show(('thing.spawnId' in features))
        self.PanelRespawnTime.Show(('thing.respawnTime' in features))
        self.PanelRenderStyle.Show(('thing.renderStyle' in features))
        self.PanelAlpha.Show(('thing.alpha' in features))
        self.PanelScale.Show(('thing.scale' in features))
        self.PanelDecal.Show(('thing.decal' in features))
        self.PanelBloodID.Show(('thing.bloodId' in features))
        self.PanelShadowOffset.Show(('thing.shadowOffset' in features))

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
            self.ThingList.InsertColumn(0, '', width=floor(36 * self.GetDPIScaleFactor()))
            self.ThingList.InsertColumn(1, 'Name', width=floor(225 * self.GetDPIScaleFactor()))
            self.ThingList.InsertColumn(2, 'ID', width=floor(46 * self.GetDPIScaleFactor()))
            if 'thing.game' in self.patch.engine.features:
                self.ThingList.InsertColumn(3, 'Game', width=floor(50 * self.GetDPIScaleFactor()))

        for index, _ in enumerate(self.patch.things):
            self.ThingList.InsertItem(index, '')
            self.thinglist_update_row(index)

        self.list_autosize(self.ThingList)
        self.ThingList.Select(0, True)

    def thinglist_update_row(self, row_index: int):
        """
        Updates a thing name in the list.
        """

        thing = self.patch.things[row_index]

        self.ThingList.SetItemText(row_index, str(row_index + 1))
        self.ThingList.SetItem(row_index, 1, thing.name)
        self.ThingList.SetItem(row_index, 2, str(thing['id']))
        if 'thing.game' in self.patch.engine.features:
            self.ThingList.SetItem(row_index, 3, thing['game'])

    def thinglist_resize(self, event: SizeEvent):
        """
        Resizes the thing name column to match the control's width.
        """

        if not self.ThingList.GetColumnCount():
            return

        columns_width = 0
        for column in range(self.ThingList.GetColumnCount()):
            if column == 1:
                continue
            columns_width += self.ThingList.GetColumnWidth(column)

        name_width = self.ThingList.GetClientSize()[0] - columns_width - 4
        self.ThingList.SetColumnWidth(1, name_width)

        # Required on macOS to allow the list to actually resize when window resizes.
        event.Skip()

    def flaglist_build(self):
        """
        Build the flags list from scratch.
        """

        self.thingflag_mnemonics.clear()
        flag_indices = {}

        list_index = 0
        for flag in self.patch.engine.things.flags.values():
            if flag.alias is not None:
                continue

            if flag.index is not None:
                flag_index = flag.index
            else:
                flag_index = list_index

            use_key = f'{flag.field}_{flag_index:03}_{flag.key}'
            if use_key in flag_indices:
                self.thingflag_mnemonics[flag_indices[use_key]] = (use_key, flag)
            else:
                self.thingflag_mnemonics.append((use_key, flag))
                flag_indices[use_key] = len(self.thingflag_mnemonics) - 1

            list_index += 1

        self.thingflag_mnemonics.sort(key=lambda tup: tup[0])

        flag_names = []
        for _, flag in self.thingflag_mnemonics:
            flag_names.append(' ' + flag.name)

        self.ThingFlags.SetItems(flag_names)

    def activate(self, event: ActivateEvent):
        """
        Called when this editor window is activated by the user.
        """

        # Call the editor mixin function that we are overriding.
        editormixin.EditorMixin.activate(self, event)

        if not self:
            return

        # Update the properties being displayed by this window, in case state or sound names have
        # changed.
        self.update_properties()

        # Fix weird property layout issues.
        self.PanelProperties.Layout()
        self.PanelProperties.SendSizeEvent()

    def edit_copy(self):
        """
        Copies the currently selected thing to this windows' clipboard.
        """

        self.clipboard = {
            'thing': self.patch.things[self.selected_index].clone(),
        }

    def edit_paste(self):
        """
        Pastes the thing on this windows' clipboard over the currently selected thing.
        """

        if self.clipboard is None:
            return

        self.undo_add()

        dup = self.clipboard['thing'].clone()

        # Copy references to newly duplicated thing.
        self.patch.things[self.selected_index] = dup

        self.update_is_projectile(reset=True)
        self.update_properties()
        self.is_modified(True)

    def update_properties(self):
        """
        Update the visible properties of the currently selected thing.
        """

        if not self.patch:
            return

        thing = self.patch.things[self.selected_index]

        self.update_is_projectile()

        # Set basic property text control values.
        self.ThingName.ChangeValue(str(thing.name))
        self.ThingId.ChangeValue(str(thing['id']))
        self.ThingHealth.ChangeValue(str(thing['health']))
        self.ThingRadius.ChangeValue(str(thing['radius'] / self.FIXED_UNIT))
        self.ThingHeight.ChangeValue(str(thing['height'] / self.FIXED_UNIT))
        self.ThingDamage.ChangeValue(str(thing['damage']))
        self.ThingReactionTime.ChangeValue(str(thing['reactionTime']))
        self.ThingPainChance.ChangeValue(str(thing['painChance']))
        self.ThingMass.ChangeValue(str(thing['mass']))

        if 'thing.obituaryName' in self.patch.engine.features:
            self.ThingObituaryName.ChangeValue(str(thing['obituaryName']))
        if 'thing.obituaryNamePlural' in self.patch.engine.features:
            self.ThingObituaryNamePlural.ChangeValue(str(thing['obituaryNamePlural']))
        if 'thing.gibHealth' in self.patch.engine.features:
            self.ThingGibHealth.ChangeValue(str(thing['gibHealth']))
        if 'thing.game' in self.patch.engine.features:
            self.ThingGame.SetSelection(self.ThingGame.FindString(thing['game']))
        if 'thing.spawnId' in self.patch.engine.features:
            self.ThingSpawnId.ChangeValue(str(thing['spawnId']))
        if 'thing.respawnTime' in self.patch.engine.features:
            self.ThingRespawnTime.ChangeValue(str(thing['respawnTime']))
        if 'thing.renderStyle' in self.patch.engine.features:
            render_style = self.patch.engine.render_styles[thing['renderStyle']]
            self.ThingRenderStyle.SetSelection(self.ThingRenderStyle.FindString(render_style))
        if 'thing.alpha' in self.patch.engine.features:
            self.ThingAlpha.ChangeValue(str(thing['alpha']))
        if 'thing.scale' in self.patch.engine.features:
            self.ThingScale.ChangeValue(str(thing['scale']))
        if 'thing.decal' in self.patch.engine.features:
            self.ThingDecal.ChangeValue(thing['decal'])
        if 'thing.damageFactor' in self.patch.engine.features:
            self.ThingDamageFactor.ChangeValue(str(thing['damageFactor']))
        if 'thing.gravity' in self.patch.engine.features:
            self.ThingGravity.ChangeValue(str(thing['gravity']))
        if 'thing.droppedItemId' in self.patch.engine.features:
            self.ThingDroppedItemID.ChangeValue(str(thing['droppedItemId']))
        if 'thing.pickupRadius' in self.patch.engine.features:
            self.ThingPickupRadius.ChangeValue(str(thing['pickupRadius'] / self.FIXED_UNIT))
        if 'thing.projectilePassHeight' in self.patch.engine.features:
            self.ThingProjectilePassHeight.ChangeValue(
                str(thing['projectilePassHeight'] / self.FIXED_UNIT)
            )
        if 'thing.fullbright' in self.patch.engine.features:
            self.ThingFullbright.SetValue(thing['fullbright'])
        if 'thing.bloodId' in self.patch.engine.features:
            self.ThingBloodID.SetValue(str(thing['bloodId']))
        if 'thing.shadowOffset' in self.patch.engine.features:
            self.ThingShadowOffset.SetValue(str(thing['shadowOffset'] / self.FIXED_UNIT))

        # Speed is in fixed point if this thing is a projectile, normal otherwise
        if self.thing_is_projectile:
            speed = thing['speed'] / self.FIXED_UNIT
        else:
            speed = thing['speed']
        self.ThingSpeed.ChangeValue(str(speed))

        # Set flags.
        for index in range(self.ThingFlags.GetCount()):
            _, flag = self.thingflag_mnemonics[index]
            checked = flag.key in thing[flag.field]
            self.ThingFlags.Check(index, checked)

        # Set state and sound values.
        for name in self.PROPS_STATES.values():
            self.set_display_state(name)
        for name in self.PROPS_SOUNDS.values():
            self.set_display_sound(name)

        # Update name.
        self.thinglist_update_row(self.selected_index)

    def set_display_state(self, state_name: str):
        """
        Sets state control values based on the partial name of a state thing property.
        """

        thing = self.patch.things[self.selected_index]
        state_key = 'state' + state_name
        if state_key not in thing:
            return
        state_index = thing[state_key]

        label = self.patch.get_state_name(state_index)
        self.__dict__['ThingState' + state_name].ChangeValue(str(state_index))
        self.__dict__['ThingState' + state_name + 'Name'].SetLabel(label)

    def set_display_sound(self, sound_name: str):
        """
        Sets sound control values based on the partial name of a sound thing property.
        """

        sound = self.patch.things[self.selected_index]
        sound_key = 'sound' + sound_name
        sound_index = sound[sound_key]
        if sound_key not in sound:
            return

        label = self.patch.get_sound_name(sound_index)
        self.__dict__['ThingSound' + sound_name].ChangeValue(str(sound_index))
        self.__dict__['ThingSound' + sound_name + 'Name'].SetLabel(label)

    def set_value(self, event: CommandEvent):
        """
        Sets the currently selected thing's property value.

        Which thing property to change is determined by the text control's id and the
        PROPS_VALUES lookup table.
        """

        self.undo_add()

        window_id = event.GetId()
        window = self.FindWindowById(window_id)
        value_type = self.PROPS_VALUE_TYPES[window_id]
        if value_type == 'int':
            value = utils.validate_numeric(window)
        elif value_type in {'float', 'fixed'}:
            value = utils.validate_numeric_float(window)
        elif value_type == 'bool':
            value = int(window.GetValue())
        else:
            value = window.GetValue()

        thing = self.patch.things[self.selected_index]

        # Apply fixed point divisor if the value needs it.
        # This is also necessary for the speed property if the thing is a projectile.
        key = self.PROPS_VALUES[window_id]
        if value_type == 'fixed':
            value = int(value * self.FIXED_UNIT)
        elif key == 'speed' and self.thing_is_projectile:
            value = int(value * self.FIXED_UNIT)

        # Special case handling for name field.
        if key == 'name':
            thing.name = value
            parent = self.GetMDIParent()
            parent.editor_windows[windows.MAIN_TOOL_STATES].update_filter_list()
        else:
            thing[key] = value

        self.thinglist_update_row(self.selected_index)
        self.is_modified(True)

    def set_state(self, event: CommandEvent):
        """
        Sets the currently selected thing's property value.

        Which thing property to change is determined by the text control's id and the
        PROPS_VALUES lookup table.
        """

        self.undo_add()

        window_id = event.GetId()
        window = self.FindWindowById(window_id)
        value = utils.validate_numeric(window)

        thing = self.patch.things[self.selected_index]

        # Clamp to valid state indices.
        value = max(0, min(value, len(self.patch.states) - 1))

        if str(value) != window.GetValue():
            wx.Bell()
            window.ChangeValue(str(value))

        key = self.PROPS_STATES[window_id]
        thing['state' + key] = value
        self.__dict__['ThingState' + key + 'Name'].SetLabel(self.patch.get_state_name(value))
        self.is_modified(True)
        self.update_is_projectile()
        self.update_properties()

    # def set_game(self, event):
    #     """
    #     Sets the currently selected thing's game property.
    #     """
    #
    #     game = event.GetString()
    #     self.patch.things[self.selected_index]['game'] = game
    #
    #     self.thinglist_update_row(self.selected_index)
    #     self.is_modified(True)

    def set_renderstyle(self, event: ListEvent):
        """
        Sets the currently selected thing's render style property.
        """

        index = event.GetSelection()
        renderstyle = list(self.patch.engine.render_styles.keys())[index]
        self.patch.things[self.selected_index]['renderStyle'] = renderstyle

        self.is_modified(True)

    def set_sound(self, event: CommandEvent):
        """
        Sets the currently selected thing's sound index.

        Which sound to change is determined by the text control's id and the PROPS_SOUNDS
        lookup table.
        """

        self.undo_add()

        window_id = event.GetId()
        window = self.FindWindowById(window_id)
        value = utils.validate_numeric(window)

        thing = self.patch.things[self.selected_index]

        # Clamp to valid sound indices.
        value = max(0, min(value, len(self.patch.sounds) - 1))
        if str(value) != window.GetValue():
            wx.Bell()
            window.ChangeValue(str(value))

        key = self.PROPS_SOUNDS[window_id]
        thing['sound' + key] = value
        self.__dict__['ThingSound' + key + 'Name'].SetLabel(self.patch.get_sound_name(value))
        self.is_modified(True)

    def set_flags(self, event: ListEvent):
        """
        Sets the currently selected thing's flags value.
        """

        self.undo_add()

        flags_field_set: Dict[str, Set[str]] = {}

        # Iterate over the flags defined in the flags list, adding mnemonics that are set.
        for index in range(self.ThingFlags.GetCount()):
            if not self.ThingFlags.IsChecked(index):
                continue

            index, flag = self.thingflag_mnemonics[index]
            if flag.field not in flags_field_set:
                flags_field_set[flag.field] = set()

            flags_field_set[flag.field].add(flag.key)

        for field, flags_set in flags_field_set.items():
            self.patch.things[self.selected_index][field] = flags_set

        self.is_modified(True)

    def set_flag_tooltip(self, event: MouseEvent):
        """
        Updates the tooltip displayed for the flags list when hovering over a flag.
        """

        tip = ''
        index = self.ThingFlags.HitTest(wx.Point(event.GetX(), event.GetY()))
        if index != wx.NOT_FOUND:
            index, flag = self.thingflag_mnemonics[index]
            patch_key = ThingEntry.FIELDS[flag.field].patch_key
            if flag.description:
                tip = f'{flag.description}\n\nMnemonic: {flag.key}\nField: {patch_key}'
            else:
                tip = f'Mnemonic: {flag.key}\nField: {patch_key}'

        self.ThingFlags.SetToolTip(tip)

    def set_state_external(self, event: CommandEvent):
        """
        Sets a state property based on the state that is currently selected in the
        state editor.
        """

        self.undo_add()

        # Get a reference to the states editor window.
        parent = self.GetMDIParent()
        states_frame = parent.editor_windows[windows.MAIN_TOOL_STATES]

        text_ctrl = self.FindWindowById(self.PROPS_STATESET[event.GetId()])
        text_ctrl.SetValue(str(states_frame.get_selected_state_index()))
        self.is_modified(True)
        self.update_is_projectile()
        self.update_properties()

    def set_sound_external(self, event: CommandEvent):
        """
        Sets a sound property based on the sound that is currently selected in the
        sound editor.
        """

        # Get a reference to the states editor window.
        parent = self.GetMDIParent()
        sounds_frame = parent.editor_windows[windows.MAIN_TOOL_SOUNDS]

        row_index = sounds_frame.selected_row
        sound = self.patch.sounds[row_index - 1]
        if sound.unused:
            row_index = 0

        self.undo_add()
        text_ctrl = self.FindWindowById(self.PROPS_SOUNDSET[event.GetId()])
        text_ctrl.SetValue(str(row_index))
        self.is_modified(True)

    def thing_select(self, event: ListEvent):
        """
        Called when a thing is selected from the thing names list.
        """

        self.selected_index = event.GetIndex()
        self.thing_is_projectile = None
        self.update_properties()

    def thing_restore(self, event: CommandEvent):
        """
        Restores the currently selected thing to the one stored in the engine configuration.
        """

        self.undo_add()

        thing_clone = self.patch.engine.things[self.selected_index].clone()
        self.patch.things[self.selected_index] = thing_clone

        self.update_is_projectile(reset=True)
        self.update_properties()
        self.is_modified(True)

    def goto_state_event(self, event: CommandEvent):
        """
        Changes the selected state in the states editor window to the one of a thing's
        state property.
        """

        key = self.PROPS_STATENAMES[event.GetId()]
        state_index = self.patch.things[self.selected_index]['state' + key]

        self.goto_state(state_index, statesframe.FILTER_TYPE_THING, self.selected_index)

    def goto_sound_event(self, event: CommandEvent):
        """
        Changes the selected sound in the sounds editor window to the one of a thing's
        sound property.
        """

        key = self.PROPS_SOUNDNAMES[event.GetId()]
        sound_index = self.patch.things[self.selected_index]['sound' + key]

        self.goto_sound(sound_index)

    def sound_play(self, event: CommandEvent):
        """
        Plays a sound entry.
        """

        key = self.PROPS_SOUNDNAMES[event.GetId()]
        sound_index = self.patch.things[self.selected_index]['sound' + key]
        if sound_index == 0:
            return

        utils.sound_play(self.patch.sounds[sound_index - 1].name, self.pwads)

    def undo_restore_item(self, item: UndoItem):
        """
        @see EditorMixin.undo_restore_item
        """

        index = item['index']

        self.patch.things[index] = item['item']

        self.update_is_projectile(reset=True)
        self.thinglist_update_row(index)
        self.update_properties()

        self.is_modified(True)

    def undo_store_item(self) -> UndoItem:
        """
        @see EditorMixin.undo_store_item
        """

        return {
            'item': self.patch.things[self.selected_index].clone(),
            'index': self.selected_index
        }

    def thing_context(self, event: ListEvent):
        """
        Displays the context menu for things.
        """

        self.ThingList.PopupMenu(self.ThingContext, event.GetPoint())

    def thing_context_copy(self, event: MenuEvent):
        """
        Context menu copy redirect.
        """
        self.edit_copy()

    def thing_context_paste(self, event: MenuEvent):
        """
        Context menu paste redirect.
        """
        self.edit_paste()

    def thing_context_clear(self, event: MenuEvent):
        """
        Clears a thing's properties.
        """

        self.undo_add()

        self.patch.things[self.selected_index] = self.patch.engine.default_thing.clone()

        self.update_is_projectile(reset=True)
        self.update_properties()
        self.is_modified(True)

    def preview_state(self, event: MenuEvent):
        """
        Preview animation from a state.
        """

        key = self.PROPS_STATENAMES[event.GetId()]
        state_index = self.patch.things[self.selected_index]['state' + key]

        self.preview_dialog.prepare(self.pwads, self.patch, state_index, self.selected_index)
        self.preview_dialog.ShowModal()

    def update_is_projectile(self, reset: bool = False):
        """
        Updates the thing_is_projectile variable. If any of the current thing's states sets
        a momentum then it is not a projectile.
        """

        if reset:
            is_before = None
        else:
            is_before = self.thing_is_projectile

        self.thing_is_projectile = True

        state_query = StateFilterQuery(self.patch)
        state_query.sort(StateIndexSort(self.patch))

        thing = self.patch.things[self.selected_index]
        state_query.filter(ThingStateFilter(self.patch, thing))

        query_results = state_query.execute()

        for _, _, state in query_results:
            if not state['action']:
                continue

            action = self.patch.engine.actions[state['action']]
            if action.sets_momentum:
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
