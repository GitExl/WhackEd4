#!/usr/bin/env python
#coding=utf8

"""
This module contains classes to create, read and write Dehacked patches.
"""

import copy

from whacked4 import config
from whacked4.dehacked import entries
from whacked4.dehacked import engine
from whacked4.utils import Enum



class DehackedPatchError(Exception):
    """
    Base class for errors in Dehacked file reading\writing.
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class DehackedVersionError(DehackedPatchError):
    """
    Version difference errors in Dehacked file reading.
    """


class DehackedFormatError(DehackedPatchError):
    """
    Patch format version errors in Dehacked file reading.
    """


class DehackedLookupError(DehackedPatchError):
    """
    Patch format key lookup errors in Dehacked file reading.
    """


class ParseMode(Enum):
    """
    Modes for the dehacked patch parser.
    """

    NOTHING = 0
    THING = 1
    STATE = 2
    SOUND = 3
    WEAPON = 4
    AMMO = 5
    SPRITE = 6
    POINTER = 7
    STRING = 8
    MISC = 9
    CHEATS = 10
    PARS = 11
    STRINGS_EXT = 12
    POINTERS_EXT = 13


def write_dict(f, items, source_items, data, header):
    """
    Writes a dictionary of key\\value pairs to a Dehacked patch file, if they have been modified compared to a
    source dict.

    @param f: the file object to write to.
    @param items: the modified item dict.
    @param source_items: the original item dict.
    @param data: a dictionary containing information about each key\\value pair that is written to the Dehacked
    file. Each value is another dict containing at least a 'patchKey' item that describes what key to write to the file.
    """

    # Build a list of modified items.
    out = {}
    for key, item in items.items():
        if item != source_items[key]:
            out[data[key]['patchKey']] = item

    if len(out) > 0:
        f.write('\n{}\n'.format(header))
        for key in out:
            f.write('{} = {}\n'.format(key, out[key]))


class Patch(object):
    """
    A Dehacked patch object.

    This is initialized from an engine object's data tables.
    """

    FRAME_FLAG_LIT = 0x8000

    def __init__(self):
        self.filename = None

        self.engine = None
        self.version = 0
        self.extended = False

        # Table data.
        self.things = None
        self.states = None
        self.sounds = None
        self.weapons = None
        self.ammo = None
        self.strings = None
        self.cheats = None
        self.misc = None
        self.pars = None
        self.sprite_names = None
        self.sound_names = None

    def initialize_from_engine(self, parent_engine):
        """
        Initializes this patch with the data from an engine.
        """

        self.engine = parent_engine
        self.extended = parent_engine.extended

        self.things = parent_engine.things.clone()
        self.states = parent_engine.states.clone()
        self.sounds = parent_engine.sounds.clone()
        self.weapons = parent_engine.weapons.clone()
        self.ammo = parent_engine.ammo.clone()
        self.strings = copy.deepcopy(parent_engine.strings)
        self.cheats = copy.deepcopy(parent_engine.cheats)
        self.misc = copy.deepcopy(parent_engine.misc)
        self.sprite_names = copy.deepcopy(parent_engine.sprite_names)
        self.sound_names = copy.deepcopy(parent_engine.sound_names)

        if parent_engine.extended:
            self.pars = []

    def update_string_externals(self, engine_names, patch_names):
        """
        Updates a names list to reflect their string list name.

        This is used to update sound and sprite names after the strings list has been altered.

        @param engine_names: the list of names in the engine object.
        @param patch_names: the list of names in the patch object.
        """

        if self.extended:
            return

        for name_index, name in enumerate(engine_names):
            if name in self.engine.strings:
                string_index = self.engine.strings.index(name)
                patch_names[name_index] = self.strings[string_index]

    def get_ammo_name(self, ammo_index):
        """
        Returns the name of an ammo entry.

        The second to last and last entries are hardcoded.
        """

        if ammo_index == len(self.ammo):
            return 'Unknown'
        elif ammo_index == len(self.ammo) + 1:
            return 'Infinite'
        elif ammo_index < len(self.ammo):
            return self.ammo.names[ammo_index]

        return None

    def write_dehacked(self, filename):
        """
        Writes this patch to a Dehacked file.
        """

        with open(filename, 'w') as f:
            # Write header.
            f.write('Patch File for DeHackEd v3.0\n')

            if config.APP_BETA:
                f.write('# Created with {} {}\n'.format(config.APP_NAME, config.APP_VERSION))
            else:
                f.write('# Created with {} {} BETA\n'.format(config.APP_NAME, config.APP_VERSION))

            f.write('# Note: Use the pound sign (\'#\') to start comment lines.\n\n')

            f.write('Doom version = {}\n'.format(self.version))
            f.write('Patch format = 6\n\n')

            # Write tables.
            self.things.write_patch_data(self.engine.things, f)
            self.states.write_patch_data(self.engine.states, f)
            self.sounds.write_patch_data(self.engine.sounds, f)
            self.weapons.write_patch_data(self.engine.weapons, f)
            self.ammo.write_patch_data(self.engine.ammo, f)

            # Write simple sections.
            write_dict(f, self.cheats, self.engine.cheats, self.engine.cheat_data, 'Cheat 0')
            write_dict(f, self.misc, self.engine.misc, self.engine.misc_data, 'Misc 0')

            # Write code pointers.
            try:
                self.write_patch_codepointers(f)
            except LookupError as e:
                return e.__str__()

            # Write simple strings.
            if not self.extended:
                self.write_patch_strings(f)

            # Write extended data.
            if self.extended:
                self.write_patch_pars(f)
                self.write_patch_ext_strings(f)

        return None

    def write_patch_strings(self, f):
        """
        Writes this patch's strings in Dehacked format.

        Text [original length] [new length]
        [original string data][new string data]
        """

        # Create a list of modified strings.
        modified = []
        for key, value in self.strings.items():
            if self.strings[key] != self.engine.strings[key]:
                modified.append(key)

        # Write only modified strings to the patch file.
        for key in modified:
            f.write('\nText {} {}\n'.format(len(self.engine.strings[key]), len(self.strings[key])))
            f.write('{}{}'.format(self.engine.strings[key], self.strings[key]))

    def write_patch_ext_strings(self, f):
        """
        Writes this patch's strings in extended Dehacked format.

        [STRINGS]
        [string key] = [escaped string]
        """

        # Create a list of modified strings.
        out = {}
        for key, value in self.strings.items():
            if value != self.engine.strings[key]:
                out[key] = value

        # Write modified string to the patch file.
        if len(out) > 0:
            f.write('\n[STRINGS]\n')
            for name, string in out.items():
                f.write('{} = {}\n'.format(name, string_escape(string)))

    def write_patch_pars(self, f):
        """
        Writes par times to a Dehacked patch.

        [PARS]
        par [[episode]] [map] [time]
        """

        if len(self.pars) == 0:
            return

        f.write('\n[PARS]\n')
        for entry in self.pars:
            if entry['episode'] == 0:
                f.write('par {} {}\n'.format(entry['map'], entry['seconds']))
            else:
                f.write('par {} {} {}\n'.format(entry['episode'], entry['map'], entry['seconds']))

    def write_patch_codepointers(self, f):
        """
        Writes codepointer data to a Dehacked patch.

        @raise LookupError: if an action pointer index cannot be found, or if there is no engine state with the
        new action pointer.
        """

        if not self.extended:
            # For non-extended patches, each state's action has an index. States without an action are skipped.
            # When writing these action pointers to a patch file, state actions are matched to action pointer indices.
            # Their value refers to a state in the original engine data with this particular action.
            for i in range(len(self.states)):
                action_pointer = self.states[i]['action']

                if action_pointer != self.engine.states[i]['action']:
                    # Attempt to find this state's action pointer index in the action index lookup list.
                    try:
                        action_pointer_index = self.engine.action_index_to_state.index(i)
                    except ValueError:
                        raise LookupError('Cannot find an action pointer index for state {}'.format(i))

                    # Find a state in the engine state table that uses the new action pointer.
                    state_index = -1
                    for j in range(len(self.engine.states)):
                        if self.engine.states[j]['action'] == action_pointer:
                            state_index = j
                            break

                    if state_index == -1:
                        raise LookupError('Cannot find a state for action pointer {}'.format(action_pointer))

                    f.write('\nPointer {} (Frame {})\n'.format(action_pointer_index, i))
                    f.write('Codep Frame = {}\n'.format(state_index))

        else:
            out = {}

            # Create a dict of modified actions.
            # [state index] = action pointer
            for index in range(len(self.states)):
                action_pointer = self.states[index]['action']
                if action_pointer != self.engine.states[index]['action']:
                    out[index] = action_pointer

            if len(out) > 0:
                f.write('\n[CODEPTR]\n')
                for index, action in out.items():
                    f.write('FRAME {} = {}\n'.format(index, action))

    def analyze_patch(self, filename, engines):
        """
        Analyzes a Dehacked patch file without loading it.

        This patch object will have it's state altered to reflect the results of the analysis.

        @param filename: The filename of the patch to analyze.
        @param engines: A dict of engine objects.

        @raise DehackedVersionError: if this patch cannot be loaded by any of the specified engines, or if the patch
        does not define a Doom version at all.
        @raise DehackedPatchError: if the patch contains extended Dehacked features alongside conflicting normal ones.
        """

        self.filename = filename
        self.extended = False
        self.version = 0

        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break

                # Strip \n and whitespace.
                line = line[:-1].strip()

                # Detect version number.
                # Searches the engines list for an engine that supports loading this patch.
                if line.startswith('Doom version = '):
                    version = int(line[15:])
                    for find_engine in engines.values():
                        if version in find_engine.versions and self.extended == find_engine.extended:
                            self.version = version
                            break

                    if self.version == 0:
                        raise DehackedVersionError('{} with engine version {} does not match any supported engine'
                                                   'version.'.format(filename, version))

                # Detect extended patches from section headers.
                elif line.startswith('[') and line.endswith(']'):
                    self.extended = True

                # Detect extended patches from thing flag mnemonics.
                elif line.startswith('Bits = ') and not line[7:].isdigit():
                    self.extended = True

                # Detect normal patches from action pointer values in frames.
                # Mixing action pointers and [CODEPTR] blocks does not make sense.
                elif line.startswith('Action pointer = '):
                    if self.extended:
                        raise DehackedPatchError('Conflicting patch extension mechanisms.')
                    self.extended = False

        if self.version == 0:
            raise DehackedVersionError('{} does not define a Doom version.'.format(filename))

    def read_dehacked(self, filename):
        """
        Reads a Dehacked file.

        @raise DehackedPatchError: if the patch file has no valid Dehacked header.
        @raise DehackedFormatError: if the patch format is not supported.

        @return: a dict containing non-fatal warnings and messages that occurred during the parsing process.
        """

        # State.
        valid = False
        mode = ParseMode.NOTHING
        entry_index = -1

        # A dict of messages to return.
        messages = {}

        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line[:-1].strip()

                # Skip comment lines and empty lines.
                if len(line) == 0 or line[0].startswith('#'):
                    continue

                # Validate header line.
                if mode == ParseMode.NOTHING:
                    if line == 'Patch File for DeHackEd v3.0':
                        valid = True
                if not valid:
                    raise DehackedPatchError('The file {} does not have a valid Dehacked header.'.format(filename))

                # Header pairs.
                if line.startswith('Patch format = '):
                    value = int(line[15:])
                    if value != 6:
                        raise DehackedFormatError('{} has an unsupported patch format ({}).'.format(filename, value))
                    continue

                line_words = line.split(' ')

                # Entry headers.
                if line.startswith('Thing ') and len(line_words) >= 3:
                    mode = ParseMode.THING
                    entry_index = int(line_words[1]) - 1
                    entry_name = ' '.join(line_words[2:])[1:-1]
                    self.things.names[entry_index] = entry_name
                    continue
                elif line.startswith('Frame ') and len(line_words) >= 2:
                    mode = ParseMode.STATE
                    entry_index = int(line_words[1])
                    continue
                elif line.startswith('Sound ') and len(line_words) >= 2:
                    mode = ParseMode.SOUND
                    entry_index = int(line_words[1])
                    continue
                elif line.startswith('Weapon ') and len(line_words) >= 3:
                    mode = ParseMode.WEAPON
                    entry_index = int(line_words[1])
                    entry_name = ' '.join(line_words[2:])[1:-1]
                    self.weapons.names[entry_index] = entry_name
                    continue
                elif line.startswith('Ammo ') and len(line_words) >= 3 and line_words[2][0] == '(':
                    mode = ParseMode.AMMO
                    entry_index = int(line_words[1])
                    entry_name = ' '.join(line_words[2:])[1:-1]
                    self.ammo.names[entry_index] = entry_name
                    continue
                elif line.startswith('Sprite ') and len(line_words) == 2:
                    mode = ParseMode.SPRITE
                    entry_index = int(line_words[1])
                    messages['UNSUPPORTED_SPRITE'] = 'The patch contains sprite blocks, which are unsupported and ' \
                                                     'will not be loaded.'
                    continue
                elif line.startswith('Pointer ') and len(line_words) >= 4:
                    mode = ParseMode.POINTER
                    entry_index = int(line_words[3][:-1])
                    continue
                elif line.startswith('Cheat 0'):
                    mode = ParseMode.CHEATS
                    continue
                elif line.startswith('Misc 0'):
                    mode = ParseMode.MISC
                    continue
                elif line.startswith('[PARS]'):
                    mode = ParseMode.PARS
                    continue
                elif line.startswith('[CODEPTR]'):
                    mode = ParseMode.POINTERS_EXT
                    continue
                elif line.startswith('[STRINGS]'):
                    mode = ParseMode.STRINGS_EXT
                    continue

                # Text header.
                elif line.startswith('Text ') and len(line_words) == 3:
                    mode = ParseMode.STRING

                    entry_len1 = int(line_words[1])
                    entry_len2 = int(line_words[2])

                    original = f.read(entry_len1)
                    new = f.read(entry_len2)

                    # Match strings to one in the original engine string table.
                    if not self.extended:
                        found_key = None
                        for key in self.strings:
                            if self.strings[key] == original:
                                found_key = key
                                break

                        if found_key is None:
                            messages['NOSTRING_' + str(len(messages))] = 'The engine string "{}" could not be found. ' \
                                                                         'It will not be loaded.'.format(original)
                        else:
                            self.strings[key] = new

                        # Also replace sprite names, so that patches can alter them without offset modifications.
                        for i in range(len(self.sprite_names)):
                            if self.sprite_names[i] == original:
                                self.sprite_names[i] = new
                                break

                        # Also replace sound names, so that patches can alter them without offset modifications.
                        for i in range(len(self.sound_names)):
                            if self.sound_names[i] == original:
                                self.sound_names[i] = new
                                break

                    # In extended mode, locate the key of the string and replace that.
                    # This ensures that extended patches can still load normal strings.
                    else:
                        key = None
                        for string_key, text in self.strings.items():
                            if text == original:
                                key = string_key
                                break

                        if key is None:
                            messages['NOSTRING_' + str(len(messages))] = 'The engine string "{}" could not be found.' \
                                                                         'It will not be loaded.'.format(original)
                        else:
                            self.strings[key] = new

                    continue

                # Extended mode section contents.
                if mode == ParseMode.PARS:
                    if line_words[0] == 'par':
                        par = entries.ParEntry(self.engine)

                        if len(line_words) == 4:
                            par['episode'] = int(line_words[1])
                            par['map'] = int(line_words[2])
                            par['seconds'] = int(line_words[3])
                        elif len(line_words) == 3:
                            par['episode'] = 0
                            par['map'] = int(line_words[1])
                            par['seconds'] = int(line_words[2])
                        else:
                            continue

                        self.pars.append(par)

                    continue

                elif mode == ParseMode.STRINGS_EXT:
                    pair = line.split(' = ')
                    if len(pair) < 2:
                        continue

                    key = pair[0]
                    value = pair[1]

                    # Read multiline strings.
                    if line.endswith('\\'):

                        # Strip the trailing \
                        value = value[:-1]
                        while True:
                            line = f.readline()
                            if line is None:
                                break

                            # Strip newline.
                            line = line[:-1]

                            # Lines that do not end with \ will terminate the string value.
                            # Lines that do are added without the \
                            if not line.endswith('\\'):
                                value += line.lstrip()
                                break
                            else:
                                value += line.lstrip()[:-1]

                    self.strings[key] = string_unescape(value)
                    continue

                elif mode == ParseMode.POINTERS_EXT:
                    pair = line.split(' = ')
                    if len(pair) < 2:
                        continue

                    key = pair[0]
                    value = pair[1]
                    index = int(key.split(' ')[1])

                    if value not in self.engine.actions:
                        messages['UNKNOWN_ACTION_NAME'] = 'Unknown action name ' + value
                    elif index < 0 or index >= len(self.states):
                        messages['INVALID_CODEPOINTER'] = 'Invalid codepointer values were encountered.'
                    else:
                        self.states[index]['action'] = value

                    continue

                # Key\value pairs.
                pair = line.split(' = ', 1)
                if len(pair) != 2:
                    continue
                key = pair[0]
                value = pair[1]

                try:
                    if mode == ParseMode.THING:
                        self.things[entry_index].set_patch_key(key, value)
                    elif mode == ParseMode.STATE:
                        self.states[entry_index].set_patch_key(key, value)
                    elif mode == ParseMode.SOUND:
                        self.sounds[entry_index].set_patch_key(key, value)
                    elif mode == ParseMode.WEAPON:
                        self.weapons[entry_index].set_patch_key(key, value)
                    elif mode == ParseMode.AMMO:
                        self.ammo[entry_index].set_patch_key(key, value)
                    elif mode == ParseMode.POINTER:
                        self.states[entry_index]['action'] = self.engine.states[int(value)]['action']
                    elif mode == ParseMode.CHEATS:
                        table_key = engine.get_key_from_patchkey(self.engine.cheat_data, key)
                        if table_key is None:
                            messages['PATCH_CHEAT_KEY_' + str(len(messages))] = 'Unknown patch cheat key {}. This' \
                                                                                'entry will be ignored.'.format(key)
                        else:
                            self.cheats[table_key] = value
                    elif mode == ParseMode.MISC:
                        table_key = engine.get_key_from_patchkey(self.engine.misc_data, key)
                        if table_key is None:
                            messages['PATCH_MISC_KEY_' + str(len(messages))] = 'Unknown patch miscellaneous key {}.' \
                                                                               'This entry will be ignored.'.format(key)
                        else:
                            self.misc[table_key] = value

                except Exception as e:
                    messages['EXCEPTION'] = 'Exceptions occurred during loading. The patch may be corrupted.\n\n' \
                                            'Last exception:\n' + str(e)

        return messages

    def get_state_name(self, state_index):
        """
        Returns a state's name by combining it's sprite name and frame index.
        """

        if state_index == 0:
            return '-'

        state = self.states[state_index]

        sprite_name = self.sprite_names[state['sprite']]
        sprite_frame = state['spriteFrame'] & ~self.FRAME_FLAG_LIT
        sprite_frame_name = chr(sprite_frame + 65)

        return sprite_name + sprite_frame_name

    def get_sound_name(self, sound_index):
        """
        Returns a sound's name.
        """

        sound_index -= 1

        # Index 0 indicates no sound.
        if sound_index == -1:
            return '-'

        if sound_index > len(self.engine.sound_names):
            return '????'
        else:
            return self.engine.sound_names[sound_index].upper()


def string_escape(string):
    """
    Returns an escaped string for use in Dehacked patch writing.
    """

    string = string.replace('\\', '\\\\')
    string = string.replace('\n', '\\n')
    string = string.replace('\r', '\\r')
    string = string.replace('\t', '\\t')
    string = string.replace('\"', '\\"')

    return string


def string_unescape(string):
    """
    Returns an escaped string for use in Dehacked patch reading.
    """

    string = string.replace('\\\\', '\\')
    string = string.replace('\\n', '\n')
    string = string.replace('\\r', '\r')
    string = string.replace('\\t', '\t')
    string = string.replace('\\"', '\"')

    return string
