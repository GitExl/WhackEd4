import json

from json.encoder import JSONEncoder

from whacked4.dehacked import table, entries, entry
from whacked4.dehacked.action import Action


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
        self.versions = []

        # If True, this engine support Boom extended patch features.
        self.extended = False

        # The nice name of this engine for usage in a UI.
        self.name = 'UNNAMED'

        # Things table.
        self.things = table.Table(entries.ThingEntry, self)
        self.things.offset = 1
        self.things.names = []
        self.things.flags = {}

        # Weapons table.
        self.weapons = table.Table(entries.WeaponEntry, self)
        self.weapons.names = []

        # Ammo table.
        self.ammo = table.Table(entries.AmmoEntry, self)
        self.ammo.names = []

        # Sound table.
        self.sounds = table.Table(entries.SoundEntry, self)
        self.sound_names = []

        # Cheats table.
        self.cheats = {}
        self.cheat_data = {}

        # Cheats table.
        self.misc = {}
        self.misc_data = {}

        # States table.
        self.states = table.Table(entries.StateEntry, self)

        # Strings dictionary.
        self.strings = {}

        # Sprite names.
        self.sprite_names = []

        # A list mapping action indices to state indices.
        self.action_index_to_state = []

        # A dict of actions available to this engine.
        self.actions = {}

        # A set of state indices whose use is hardcoded in the game executable.
        self.used_states = set()

        # A list of hacks to enable for this engine.
        self.hacks = {}

        # A list of supported render styles.
        self.render_styles = {}

        # A set of supported features.
        self.features = set()

        # Defaults for new entries and unnamed fields.
        self.default_state = entries.StateEntry(self)
        self.default_thing = entries.ThingEntry(self)
        self.default_weapon = entries.WeaponEntry(self)
        self.default_ammo = entries.AmmoEntry(self)
        self.default_sound = entries.SoundEntry(self)

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

        # try:

        if not is_base_table:
            self.versions = data['versions']
            self.extended = data['extended']
            self.name = data['name']

        self.default_state.from_json(data['defaultState'])
        self.default_thing.from_json(data['defaultThing'])
        self.default_weapon.from_json(data['defaultWeapon'])
        self.default_ammo.from_json(data['defaultAmmo'])
        self.default_sound.from_json(data['defaultSound'])

        # If any base tables are referenced, load them first.
        if 'baseTables' in data:
            base_tables = data['baseTables']
            for base_table in base_tables:
                base_filename = 'cfg/basetables_{}.json'.format(base_table)
                self.merge_data(base_filename, True)

        self.features.update(set(data['features']))

        self.things.names += data['thingNames']
        self.things.flags.update(data['thingFlags'])
        self.things.read_from_json(data['things'])
        if len(self.things.names) != len(self.things):
            raise DehackedEngineError('Thing and thing names sizes do not match.')

        self.weapons.names += data['weaponNames']
        self.weapons.read_from_json(data['weapons'])
        if len(self.weapons.names) != len(self.weapons):
            raise DehackedEngineError('Weapon and weapon name sizes do not match.')

        self.ammo.names += data['ammoNames']
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

        self.sprite_names += data['spriteNames']
        self.used_states.update(set(data['usedStates']))
        self.hacks.update(data['hacks'])

        self.render_styles.update(data['renderStyles'])

        self.sound_names += data['soundNames']
        if len(self.sound_names) != len(self.sounds):
            raise DehackedEngineError('Sound and sound names sizes do not match.')

        if not self.extended:
            self.action_index_to_state += data['actionIndexToState']

        # except KeyError as e:
        #     raise DehackedEngineError('Invalid engine table data. KeyError {}'.format(e))

    @staticmethod
    def clear_false(data):
        """
        Removes items from data that have "False" as their value.
        """

        unset = set()

        for key, value in data.items():
            if not value:
                unset.add(key)

        for key in unset:
            del data[key]

        return data

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

        for key, action in self.actions.items():
            if action.name == action_name:
                return key

        return None

    def is_compatible(self, patch):
        """
        Returns True if the patch can be loaded with this engine.

        @param patch: the patch to examine.
        """

        version_match = (patch.version in self.versions)
        if patch.extended and not self.extended:
            extension_match = False
        else:
            extension_match = True

        return version_match and extension_match


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
