import json
import struct


class ExecutableReader:

    def __init__(self, engine):
        self.engine = engine

    def read_executable(self, engine_filename, exe_filename):
        """
        Reads engine data from a game executable, using a JSON file as base.

        @param engine_filename: The filename of the configuration file containing direction on how to read the data
        from the executable.
        @param exe_filename: The filename of the game executable to read engine data from.

        @raise KeyError: if the executable data file does not contain all necessary data.
        """

        with open(engine_filename, 'r') as f:
            exe_config = json.load(f)

        try:
            self.engine.versions = exe_config['versions']
            self.engine.extended = exe_config['extended']
            self.engine.name = exe_config['name']

            self.engine.actions = exe_config['actions']
            self.engine.action_index_to_state = exe_config['actionIndexToState']

            self.engine.misc_data = exe_config['miscData']
            self.engine.cheat_data = exe_config['cheatData']

            self.engine.used_states = exe_config['usedStates']

            with open(exe_filename, 'rb') as f:
                f.seek(exe_config['thingOffset'])
                self.engine.things.read_from_executable(exe_config['thingCount'], f)
                self.engine.things.names = exe_config['thingNames']
                self.engine.things.flags = exe_config['thingFlags']

                f.seek(exe_config['stateOffset'])
                self.engine.states.read_from_executable(exe_config['stateCount'], f)

                f.seek(exe_config['weaponOffset'])
                self.engine.weapons.read_from_executable(exe_config['weaponCount'], f)
                self.engine.weapons.names = exe_config['weaponNames']

                f.seek(exe_config['soundOffset'])
                self.engine.sounds.read_from_executable(exe_config['soundCount'], f)

                # Read tables that require more work.
                self.read_executable_sprite_names(f, exe_config)
                self.read_executable_sound_names(f, exe_config)
                self.read_executable_cheats(f, exe_config)
                self.read_executable_misc(f)
                self.read_executable_strings(f, exe_config)

                self.read_executable_ammo(f, exe_config)
                self.engine.ammo.names = exe_config['ammoNames']

        except KeyError:
            raise Exception('Invalid executable data.')

    def read_executable_sound_names(self, f, exe_config):
        """
        Reads sound names from an executable.

        @param f: the file handle to read from.
        @param exe_config: the executable configuration to use.
        """

        self.engine.sound_names = []
        for sound in self.engine.sounds:
            f.seek(sound['namePointer'] + exe_config['dataSegment'])
            text = _read_string(f)
            self.engine.sound_names.append(text)

    def read_executable_strings(self, f, exe_config):
        """
        Reads strings from an executable.

        @param f: the file handle to read from.
        @param exe_config: the executable configuration to use.
        """

        f.seek(exe_config['stringOffset'])

        self.engine.strings = []
        for _ in range(exe_config['stringCount']):
            text = _read_string(f)

            # Seek ahead to the next offset dividable by 4.
            if f.tell() % 4 != 0:
                f.read(4 - (f.tell() % 4))

            self.engine.strings.append(text)

    def read_executable_misc(self, f):
        """
        Reads miscellaneous data from an executable.

        @param f: the file handle to read from.
        """

        int_struct = struct.Struct('<i')
        byte_struct = struct.Struct('<B')

        self.engine.misc = {}
        for name, item in self.engine.misc_data.items():
            f.seek(item['offsets'][0])

            # An item's data type defines its byte length.
            data_type = item['type']
            if data_type == 'int':
                self.engine.misc[name] = int_struct.unpack(f.read(4))[0]
            elif data_type == 'byte' or data_type == 'boolean':
                self.engine.misc[name] = byte_struct.unpack(f.read(1))[0]
            else:
                raise Exception('Unknown miscellaneous data type {}'.format(data_type))

    def read_executable_ammo(self, f, exe_config):
        """
        Reads ammo data from an executable.

        @param f: the file handle to read from.
        @param exe_config: the executable configuration to use.
        """

        single_struct = struct.Struct('<i')
        count = exe_config['ammoCount']

        # Read the maximum ammo amounts first.
        f.seek(exe_config['ammoOffset'])
        for index in range(count):
            ammo_entry = self.engine.ammo.entries.AmmoEntry(self)

            data = single_struct.unpack(f.read(single_struct.size))
            ammo_entry['maximum'] = data[0]

            self.engine.ammo.entries.append(ammo_entry)

        # Read the clip sizes second.
        for index in range(count):
            data = single_struct.unpack(f.read(single_struct.size))

            ammo_entry = self.engine.ammo.entries[index]
            ammo_entry['clip'] = data[0]

    def read_executable_cheats(self, f, exe_config):
        """
        Reads and decrypts cheat code strings from an executable.

        @param f: the file handle to read from.
        @param exe_config: the executable configuration to use.
        """

        self.engine.cheats = {}
        for name, data in self.engine.cheat_data.items():
            f.seek(exe_config['cheatOffset'] + data['offset'])
            text = f.read(data['length'])

            self.engine.cheats[name] = _decrypt_cheat_string(text)

    def read_executable_sprite_names(self, f, exe_config):
        """
        Reads sprite names from an executable.

        @param f: the file handle to read from.
        @param exe_config: the executable configuration to use.
        """

        pointers = []
        self.engine.sprite_names = []
        spritename_struct = struct.Struct('<I')

        # Read pointers to the sprite names.
        f.seek(exe_config['spriteOffset'])
        for _ in range(exe_config['spriteCount']):
            offset = spritename_struct.unpack(f.read(4))[0]
            pointers.append(offset)

        # Read actual strings.
        for index in range(exe_config['spriteCount']):
            f.seek(pointers[index] + exe_config['dataSegment'])
            self.engine.sprite_names.append(f.read(4))


def _read_string(f):
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


def _decrypt_cheat_string(text):
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
