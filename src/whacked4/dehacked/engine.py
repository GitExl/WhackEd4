import json

from json.encoder import JSONEncoder
from typing import List, Dict, Set

from whacked4.dehacked import table, entries, entry
from whacked4.dehacked.action import Action
from whacked4.dehacked.entry import Entry
from whacked4.dehacked.table import Table


class DehackedEngineError(Exception):
    """
    Base class for engine table errors.
    """


class Engine(object):
    """
    An engine contains all the data needed to be able to edit Dehacked patches. This data can be extracted from a
    game executable, or loaded from a JSON file.
    """

    def __init__(self):

        # A list of versions supported by this engine.
        self.versions: List[int] = []

        # If True, this engine support Boom extended patch features.
        self.extended: bool = False

        # The nice name of this engine for usage in a UI.
        self.name: str = 'UNNAMED'

        # Things table.
        self.things: Table = table.Table(entries.ThingEntry, self)
        self.things.offset = 1
        self.things.flags = {}

        # Other tables.
        self.states: Table = table.Table(entries.StateEntry, self)
        self.weapons: Table = table.Table(entries.WeaponEntry, self)
        self.ammo: Table = table.Table(entries.AmmoEntry, self)
        self.sounds: Table = table.Table(entries.SoundEntry, self)

        # Cheats table.
        self.cheats: Dict[str, str] = {}
        self.cheat_data: Dict[str, Dict[str, str]] = {}

        # Cheats table.
        self.misc: Dict[str, int] = {}
        self.misc_data: Dict[str, Dict[str, str]] = {}

        # Strings dictionary.
        self.strings: Dict[str] = {}

        # Sprite names.
        self.sprite_names: List[str] = []

        # A list mapping action indices to state indices.
        self.action_index_to_state: List[int] = []

        # A dict of actions available to this engine.
        self.actions: Dict[Action] = {}

        # A set of state indices whose use is hardcoded in the game executable.
        self.used_states: Set[int] = set()

        # A list of supported render styles.
        self.render_styles: Dict[str] = {}

        # A set of supported features.
        self.features: Set[str] = set()

        # Defaults for new entries and unnamed fields.
        self.default_state: Entry = entries.StateEntry(self)
        self.default_thing: Entry = entries.ThingEntry(self)
        self.default_weapon: Entry = entries.WeaponEntry(self)
        self.default_ammo: Entry = entries.AmmoEntry(self)
        self.default_sound: Entry = entries.SoundEntry(self)

    def merge_data(self, filename, is_base_table=False):
        """
        Reads and merges engine data from a JSON table configuration file into the current engine.

        @param filename: the name of the file to read table data from.
        @param is_base_table: if True, only base table data will be merged.

        @raise KeyError: if the table file is missing data.
        """

        data = None
        with open(filename, 'r') as f:
            try:
                data = json.load(f)
            except ValueError as e:
                print('Error in table file {}'.format(filename))
                raise e

        try:
            if not is_base_table:
                self.versions = data['versions']
                self.extended = data['extended']
                self.name = data['name']

            # Load parents before any other data.
            if 'parent' in data:
                parent = data['parent']
                parent_filename = 'cfg/{}.json'.format(parent)
                self.merge_data(parent_filename, True)

            self.default_state.from_json(data['defaultState'])
            self.default_thing.from_json(data['defaultThing'])
            self.default_weapon.from_json(data['defaultWeapon'])
            self.default_ammo.from_json(data['defaultAmmo'])
            self.default_sound.from_json(data['defaultSound'])

            self.features.update(set(data['features']))

            self.things.flags.update(data['thingFlags'])
            self.things.read_from_json(data['things'])

            self.weapons.read_from_json(data['weapons'])
            self.ammo.read_from_json(data['ammo'])

            for key, value in data['actions'].items():
                self.actions[key] = Action.from_json(value)

            self.states.read_from_json(data['states'])
            self.sounds.read_from_json(data['sounds'])

            self.strings.update(data['strings'])

            self.misc.update(data['misc'])
            self.misc_data.update(data['miscData'])

            self.cheats.update(data['cheats'])
            self.cheat_data.update(data['cheatData'])

            self.used_states.update(set(data['usedStates']))
            self.render_styles.update(data['renderStyles'])
            self.sprite_names += data['spriteNames']

            if not self.extended:
                self.action_index_to_state += data['actionIndexToState']

        except KeyError as e:
            raise DehackedEngineError('Invalid engine table data. KeyError {}'.format(e))

    def apply_defaults(self):
        """
        Apply table defaults. Best run after all table data has been fully loaded.
        """

        self.states.apply_defaults(self.default_state)
        self.things.apply_defaults(self.default_thing)
        self.weapons.apply_defaults(self.default_weapon)
        self.ammo.apply_defaults(self.default_ammo)
        self.sounds.apply_defaults(self.default_sound)

    def get_action_key_from_name(self, action_name):
        """
        Returns an action key from an action name. Useful for getting action names for non-extended engines.

        @param action_name: the name of the action to find the key of.
        """

        if self.extended:
            return action_name

        for key, action in self.actions.items():
            if action.name == action_name:
                return key

        return None

    def is_compatible(self, patch):
        """
        Returns True if the patch can be loaded with this engine.

        @param patch: the patch to examine.
        """

        if patch.version not in self.versions:
            return False
        if patch.extended and not self.extended:
            return False

        return True


class EngineJSONEncoder(JSONEncoder):
    """
    A small encoder object to assist the json module in encoding engine Table and Entry objects.
    """

    def default(self, o):
        if isinstance(o, entry.Entry):
            return o.to_json()

        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)

        return JSONEncoder.default(self, o)


def get_key_from_patchkey(data, patch_key):
    """
    Returns an internal entry key from a key used in a Dehacked patch file.
    This is used by the cheats and miscellaneous sections, since they do not have an associated table.

    @param data: a dict of cheat or misc data.
    @param patch_key: the string used in a patch file to identify.

    @raise LookupError: if the patch key cannot be found.
    """

    for key, item in data.items():
        if item['patchKey'] == patch_key:
            return key

    return None
