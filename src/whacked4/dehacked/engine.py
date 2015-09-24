#!/usr/bin/env python
#coding=utf8

from collections import OrderedDict
from json.encoder import JSONEncoder
from whacked4.dehacked import table, entries, entry
import json
import struct


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
        self.versions = None

        # If True, this engine support Boom extended patch features.
        self.extended = False

        # The nice name of this engine for usage in a UI.
        self.name = None

        # Things table.
        self.things = table.Table(entries.ThingEntry, self)
        self.things.offset = 1
        self.things.names = None
        self.things.flags = None

        # Weapons table.
        self.weapons = table.Table(entries.WeaponEntry, self)
        self.weapons.names = None

        # Ammo table.
        self.ammo = table.Table(entries.AmmoEntry, self)
        self.ammo.names = None

        # Sound table.
        self.sounds = table.Table(entries.SoundEntry, self)
        self.sound_names = None

        # Cheats table.
        self.cheats = None
        self.cheat_data = None

        # Cheats table.
        self.misc = None
        self.misc_data = None

        # States table.
        self.states = table.Table(entries.StateEntry, self)

        # Strings dictionary.
        self.strings = None

        # Sprite names.
        self.sprite_names = None

        # A dictionary mapping action indices to state indices.
        self.action_index_to_state = None

        # A dict of actions available to this engine.
        self.actions = None

        # A list of state indices whose use is hardcoded in the game executable.
        self.used_states = None

        # A list of hacks to enable for this engine.
        self.hacks = None

        # A list of supported render styles.
        self.render_styles = None

    def read_table(self, filename):
        """
        Reads engine data from a JSON table configuration file.

        @raise KeyError: if the table file is missing data.
        """

        with open(filename, 'r') as f:
            data = json.load(f, object_pairs_hook=OrderedDict)

        try:
            self.versions = data['versions']
            self.extended = data['extended']
            self.name = data['name']

            self.things.names = data['thingNames']
            self.things.flags = data['thingFlags']
            self.things.read_from_json(data['things'])
            if len(self.things.names) != len(self.things):
                raise DehackedEngineError('Thing and thing names sizes do not match.')

            self.weapons.names = data['weaponNames']
            self.weapons.read_from_json(data['weapons'])
            if len(self.weapons.names) != len(self.weapons):
                raise DehackedEngineError('Weapon and weapon name sizes do not match.')

            self.ammo.names = data['ammoNames']
            self.ammo.read_from_json(data['ammo'])

            self.actions = data['actions']
            self.states.read_from_json(data['states'])
            self.sounds.read_from_json(data['sounds'])

            self.strings = data['strings']

            self.misc = data['misc']
            self.misc_data = data['miscData']

            self.cheats = data['cheats']
            self.cheat_data = data['cheatData']

            self.sprite_names = data['spriteNames']
            self.used_states = data['usedStates']
            self.hacks = data['hacks']

            if 'renderStyles' in data:
                self.render_styles = data['renderStyles']
            else:
                self.render_styles = {}

            self.sound_names = data['soundNames']
            if len(self.sound_names) != len(self.sounds):
                raise DehackedEngineError('Sound and sound names sizes do not match.')

            if not self.extended:
                self.action_index_to_state = data['actionIndexToState']

        except KeyError as e:
            raise DehackedEngineError('Invalid engine table data. Exception: {}'.format(e))

    def read_executable(self, engine_filename, exe_filename):
        """
        Reads engine data from a game executable, using a JSON file as base.

        @param engine_filename: The filename of the configuration file containing direction on how to read the data
        from the executable.
        @param exe_filename: The filename of the game executable to read engine data from.

        @raise KeyError: if the executable data file does not contain all necessary data.
        """

        with open(engine_filename, 'r') as f:
            exe_config = json.load(f, object_pairs_hook=OrderedDict)

        try:
            self.versions = exe_config['versions']
            self.extended = exe_config['extended']
            self.name = exe_config['name']

            self.actions = exe_config['actions']
            self.action_index_to_state = exe_config['actionIndexToState']

            self.misc_data = exe_config['miscData']
            self.cheat_data = exe_config['cheatData']

            self.hacks = exe_config['hacks']
            self.used_states = exe_config['usedStates']

            with open(exe_filename, 'rb') as f:
                f.seek(exe_config['thingOffset'])
                self.things.read_from_executable(exe_config['thingCount'], f)
                self.things.names = exe_config['thingNames']
                self.things.flags = exe_config['thingFlags']

                f.seek(exe_config['stateOffset'])
                self.states.read_from_executable(exe_config['stateCount'], f)

                f.seek(exe_config['weaponOffset'])
                self.weapons.read_from_executable(exe_config['weaponCount'], f)
                self.weapons.names = exe_config['weaponNames']

                f.seek(exe_config['soundOffset'])
                self.sounds.read_from_executable(exe_config['soundCount'], f)

                # Read tables that require more work.
                self.read_executable_sprite_names(f, exe_config)
                self.read_executable_sound_names(f, exe_config)
                self.read_executable_cheats(f, exe_config)
                self.read_executable_misc(f)
                self.read_executable_strings(f, exe_config)

                self.read_executable_ammo(f, exe_config)
                self.ammo.names = exe_config['ammoNames']

        except KeyError:
            raise DehackedEngineError('Invalid executable data.')

    def write_table(self, filename):
        """
        Writes this engine's table data to a JSON file.
        """

        obj = {
            'versions': self.versions,
            'extended': self.extended,
            'name': self.name,

            'things': self.things,
            'thingNames': self.things.names,
            'thingFlags': self.things.flags,

            'weapons': self.weapons,
            'weaponNames': self.weapons.names,

            'states': self.states,
            'sounds': self.sounds,

            'ammo': self.ammo,
            'ammoNames': self.ammo.names,

            'strings': self.strings,

            'cheats': self.cheats,
            'cheatData': self.cheat_data,

            'misc': self.misc,
            'miscData': self.misc_data,

            'spriteNames': self.sprite_names,
            'soundNames': self.sound_names,
            'actions': self.actions,
            'actionIndexToState': self.action_index_to_state,
            'usedStates': self.used_states,
            'hacks': self.hacks
        }

        with open(filename, 'w') as f:
            f.write(json.dumps(obj, indent=4, sort_keys=False, cls=EngineJSONEncoder))

    def read_executable_sound_names(self, f, exe_config):
        """
        Reads sound names from an executable.
        """

        self.sound_names = []
        for sound in self.sounds:
            f.seek(sound['namePointer'] + exe_config['dataSegment'])
            text = read_string(f)
            self.sound_names.append(text)

    def read_executable_strings(self, f, exe_config):
        """
        Reads strings from an executable.
        """

        f.seek(exe_config['stringOffset'])

        self.strings = []
        for _ in range(exe_config['stringCount']):
            text = read_string(f)

            # Seek ahead to the next offset dividable by 4.
            if f.tell() % 4 != 0:
                f.read(4 - (f.tell() % 4))

            self.strings.append(text)

    def read_executable_misc(self, f):
        """
        Reads miscellaneous data from an executable.
        """

        int_struct = struct.Struct('<i')
        byte_struct = struct.Struct('<B')

        self.misc = {}
        for name, item in self.misc_data.iteritems():
            f.seek(item['offsets'][0])

            # An item's data type defines its byte length.
            data_type = item['type']
            if data_type == 'int':
                self.misc[name] = int_struct.unpack(f.read(4))[0]
            elif data_type == 'byte' or data_type == 'boolean':
                self.misc[name] = byte_struct.unpack(f.read(1))[0]
            else:
                raise DehackedEngineError('Unknown miscellaneous data type {}'.format(data_type))

    def read_executable_ammo(self, f, exe_config):
        """
        Reads ammo data from an executable.
        """

        single_struct = struct.Struct('<i')
        count = exe_config['ammoCount']

        # Read the maximum ammo amounts first.
        f.seek(exe_config['ammoOffset'])
        for index in range(count):
            ammo_entry = entries.AmmoEntry(self)

            data = single_struct.unpack(f.read(single_struct.size))
            ammo_entry['maximum'] = data[0]

            self.ammo.entries.append(ammo_entry)

        # Read the clip sizes second.
        for index in range(count):
            data = single_struct.unpack(f.read(single_struct.size))

            ammo_entry = self.ammo.entries[index]
            ammo_entry['clip'] = data[0]

    def read_executable_cheats(self, f, exe_config):
        """
        Reads and decrypts cheat code strings from an executable.
        """

        self.cheats = {}
        for name, data in self.cheat_data.iteritems():
            f.seek(exe_config['cheatOffset'] + data['offset'])
            text = f.read(data['length'])

            self.cheats[name] = decrypt_cheat_string(text)

    def read_executable_sprite_names(self, f, exe_config):
        """
        Reads sprite names from an executable.
        """

        pointers = []
        self.sprite_names = []
        spritename_struct = struct.Struct('<I')

        # Read pointers to the sprite names.
        f.seek(exe_config['spriteOffset'])
        for _ in range(exe_config['spriteCount']):
            offset = spritename_struct.unpack(f.read(4))[0]
            pointers.append(offset)

        # Read actual strings.
        for index in range(exe_config['spriteCount']):
            f.seek(pointers[index] + exe_config['dataSegment'])
            self.sprite_names.append(f.read(4))

    def get_action_from_key(self, key):
        """
        Returns an action value from an action key.

        @raise LookupError: if there is no such action key.
        """

        key = str(key)
        if key in self.actions:
            return self.actions[key]

        raise LookupError('Cannot find an action with key {}'.format(key))

    def get_action_key_from_name(self, action_name):
        """
        Returns an action key from an action name.
        """

        for key, item in self.actions.iteritems():
            if item['name'] == action_name:
                return key

        return None

    def is_compatible(self, patch):
        """
        Returns True if the patch can be loaded with this engine.
        """

        version_match = (patch.version in self.versions)
        if patch.extended and not self.extended:
            extension_match = False
        else:
            extension_match = True

        return version_match and extension_match


class EngineJSONEncoder(JSONEncoder):
    """
    A small encoder object to assist the json module in encoding engine table objects and entries.
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


def read_string(f):
    """
    Reads a null-terminated string from a file.
    """

    chars = []
    while True:
        char = f.read(1)
        if char == b'\0':
            break
        chars.append(char)

    return ''.join(chars)


def decrypt_cheat_string(text):
    """
    Decrypts an executable cheat string into a readable one.
    """

    text = bytearray(text)
    output = bytearray(text)

    i = 0
    while i < len(text) and text[i] != 0:
        output[i] = text[i] & 36
        output[i] |= (text[i] & 128) >> 7
        output[i] |= (text[i] & 64) >> 5
        output[i] |= (text[i] & 16) >> 1
        output[i] |= (text[i] & 8) << 1
        output[i] |= (text[i] & 2) << 5
        output[i] |= (text[i] & 1) << 7

        i += 1

    return bytes(output).encode('ascii')


def get_key_from_patchkey(data, patch_key):
    """
    Returns an internal entry key from a key used in a Dehacked patch file.

    This is used by the cheats and miscellaneous sections, since they do not have an associated table.

    @raise LookupError: if the patch key cannot be found.
    """

    for key, item in data.iteritems():
        if item['patchKey'] == patch_key:
            return key

    return None
