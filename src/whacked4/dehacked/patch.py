"""
This module contains classes to create, read and write Dehacked patches.
"""

import copy
from typing import Dict, Optional, List, Tuple, TextIO

from whacked4 import config
from whacked4.dehacked import entries
from whacked4.dehacked import engine
from whacked4.dehacked.engine import Engine
from whacked4.dehacked.entries import (ThingEntry, StateEntry, SoundEntry, WeaponEntry, AmmoEntry,
                                       ParEntry)
from whacked4.dehacked.table import Table
from whacked4.enum import WhackedEnum


class DehackedPatchError(Exception):
    """
    Base class for errors in Dehacked file reading/writing.
    """

    def __init__(self, msg: str):
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


class ParseMode(WhackedEnum):
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


def write_dict(
    f: TextIO,
    items: Dict[str, any],
    source_items: Dict[str, any],
    data: Dict[str, any],
    header: str
):
    """
    Writes a dictionary of key\\value pairs to a Dehacked patch file, if they
    have been modified compared to a source dict.

    :param f: the file object to write to.
    :param items: the modified item dict.
    :param source_items: the original item dict.
    :param data: a dictionary containing information about each key\\value pair
    that is written to the Dehacked file. Each value is another dict containing
    at least a 'patchKey' item that describes what key to write to the file.
    :param header: string to write as header.
    """

    # Build a list of modified items.
    out = {}
    for key, item in items.items():
        if item != source_items[key]:
            out[data[key]['patchKey']] = item

    if len(out) > 0:
        f.write(f'\n{header}\n')
        for key, value in out.items():
            f.write(f'{key} = {value}\n')


class Patch:
    """
    A Dehacked patch object.

    This is initialized from an engine object's data tables.
    """

    FRAME_FLAG_LIT = 0x8000

    def __init__(self, parent_engine: Engine):
        self.filename: Optional[str] = None
        self.engine: Engine = parent_engine
        self.version: int = 0
        self.extended: bool = False

        self.things: Table[ThingEntry] = parent_engine.things.clone()
        self.states: Table[StateEntry] = parent_engine.states.clone()
        self.sounds: Table[SoundEntry] = parent_engine.sounds.clone()
        self.weapons: Table[WeaponEntry] = parent_engine.weapons.clone()
        self.ammo: Table[AmmoEntry] = parent_engine.ammo.clone()
        self.pars: Table[ParEntry] = parent_engine.pars.clone()

        self.strings: Dict[str, str] = copy.deepcopy(parent_engine.strings)
        self.cheats: Dict[str, str] = copy.deepcopy(parent_engine.cheats)
        self.misc: Dict[str, any] = copy.deepcopy(parent_engine.misc)

        self.sprite_names: List[str] = copy.deepcopy(parent_engine.sprite_names)

    def get_ammo_name(self, ammo_index):
        """
        Returns the name of an ammo entry.

        The second to last and last entries are hardcoded.
        """

        if ammo_index == len(self.ammo):
            return 'Unknown'
        if ammo_index == len(self.ammo) + 1:
            return 'Infinite'
        if ammo_index < len(self.ammo):
            return self.ammo[ammo_index].name

        return None

    def write_dehacked(self, filename):
        """
        Writes this patch to a Dehacked file.
        """

        with open(filename, 'w', encoding='latin1') as f:
            # Write header.
            f.write('Patch File for DeHackEd v3.0\n')

            if config.APP_BETA:
                f.write(f'# Created with {config.APP_NAME} {config.APP_VERSION} BETA\n')
            else:
                f.write(f'# Created with {config.APP_NAME} {config.APP_VERSION}\n')

            f.write('# Note: Use the pound sign (\'#\') to start comment lines.\n\n')

            f.write(f'Doom version = {self.version}\n')
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
                return str(e)

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
        for key in self.strings:
            if self.strings[key] != self.engine.strings[key]:
                modified.append(key)

        # Write only modified strings to the patch file.
        for key in modified:
            org_len = len(self.engine.strings[key])
            org_str = self.engine.strings[key]
            new_len = len(self.strings[key])
            new_str = self.strings[key]
            f.write(f'\nText {org_len} {new_len}\n')
            f.write(f'{org_str}{new_str}')

    def write_patch_ext_strings(self, f: TextIO):
        """
        Writes this patch's strings in extended Dehacked format.

        [STRINGS]
        [string key] = [escaped string]
        """

        # Create a list of modified strings, keeping strings not present in the engine.
        out = {}
        for key, value in self.strings.items():
            if key not in self.engine.strings or value != self.engine.strings[key]:
                out[key] = value

        # Write modified string to the patch file.
        if len(out) > 0:
            f.write('\n[STRINGS]\n')
            for name, string in out.items():
                escaped_string = string_escape(string)
                f.write(f'{name} = {escaped_string}\n')

    def write_patch_pars(self, f: TextIO):
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
                map = entry['map']
                seconds = entry['seconds']
                f.write(f'par {map} {seconds}\n')
            else:
                episode = entry['episode']
                map = entry['map']
                seconds = entry['seconds']
                f.write(f'par {episode} {map} {seconds}\n')

    def write_patch_codepointers(self, f: TextIO):
        """
        Writes codepointer data to a Dehacked patch.

        @raise LookupError: if an action pointer index cannot be found, or if there
        is no engine state with the new action pointer.
        """

        if not self.extended:
            self.write_patch_codepointers_extended(f)

        else:
            out = {}

            # Create a dict of modified actions.
            # [state index] = action pointer
            for index, _ in enumerate(self.states):
                action_pointer = self.states[index]['action']
                if action_pointer != self.engine.states[index]['action']:
                    out[index] = action_pointer

            if len(out) > 0:
                f.write('\n[CODEPTR]\n')
                for index, action in out.items():
                    f.write(f'FRAME {index} = {action}\n')

    def write_patch_codepointers_extended(self, f: TextIO):
        """
        Writes extended  codepointer data to a Dehacked patch.
        """

        # For non-extended patches, each state's action has an index. States without an
        # action are skipped. When writing these action pointers to a patch file, state
        # actions are matched to action pointer indices. Their value refers to a state
        # in the original engine data with this particular action.
        for i, state in enumerate(self.states):
            action_pointer = state['action']

            if action_pointer != state['action']:
                # Attempt to find this state's action pointer index in the action
                # index lookup list.
                try:
                    action_pointer_index = self.engine.action_index_to_state.index(i)
                except ValueError as e:
                    raise LookupError(f'Cannot find an action pointer '
                                      f'index for state {i}') from e

                # Find a state in the engine state table that uses the new action pointer.
                state_index = -1
                for j, inner_state in enumerate(self.engine.states):
                    if inner_state['action'] == action_pointer:
                        state_index = j
                        break

                if state_index == -1:
                    raise LookupError(f'Cannot find a state for action pointer {action_pointer}')

                f.write(f'\nPointer {action_pointer_index} (Frame {i})\n')
                f.write(f'Codep Frame = {state_index}\n')

    @staticmethod
    def analyze(filename: str, engines: Dict[str, Engine]) -> Tuple[int, bool]:
        """
        Analyzes a Dehacked patch file without loading it.

        @param filename: The filename of the patch to analyze.
        @param engines: A dict of engine objects.

        @raise DehackedVersionError: if this patch cannot be loaded by any of the
        specified engines, or if the patch does not define a Doom version at all.
        @raise DehackedPatchError: if the patch contains extended Dehacked features
        alongside conflicting normal ones.
        """

        extended = False
        version = 0

        with open(filename, 'r', encoding='latin1') as f:
            while True:
                line = f.readline()
                if not line:
                    break

                # Strip \n and whitespace.
                line = line[:-1].strip()

                # Detect version number.
                # Searches the engines list for an engine that supports loading this patch.
                if line.startswith('Doom version = '):
                    patch_version = int(line[15:])
                    for find_engine in engines.values():
                        if patch_version in find_engine.versions and extended == find_engine.extended:
                            version = patch_version
                            break

                    if version == 0:
                        raise DehackedVersionError(
                            f'{filename} with engine version {version} does not '
                            f'match any supported engine version.'
                        )

                # Detect extended patches from section headers.
                elif line.startswith('[') and line.endswith(']'):
                    extended = True

                # Detect extended patches from thing flag mnemonics.
                elif line.startswith('Bits = ') and not line[7:].isdigit():
                    extended = True

                # Detect normal patches from action pointer values in frames.
                # Mixing action pointers and [CODEPTR] blocks does not make sense.
                elif line.startswith('Action pointer = '):
                    if extended:
                        raise DehackedPatchError('Conflicting patch extension mechanisms.')
                    extended = False

        if version == 0:
            raise DehackedVersionError(f'{filename} does not define a Doom version.')

        return version, extended

    def read_dehacked(self, filename: str):
        """
        Reads a Dehacked file.

        @raise DehackedPatchError: if the patch file has no valid Dehacked header.
        @raise DehackedFormatError: if the patch format is not supported.

        @return: a dict containing non-fatal warnings and messages that occurred
        during the parsing process.
        """

        # State.
        valid: bool = False
        mode: int = ParseMode.NOTHING
        entry_index: int = -1

        # A dict of messages to return.
        messages: Dict[str, str] = {}

        with open(filename, 'r', encoding='latin1') as f:
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
                    raise DehackedPatchError(
                        f'The file {filename} does not have a valid Dehacked header.'
                    )

                # Header pairs.
                if line.startswith('Patch format = '):
                    value = int(line[15:])
                    if value != 6:
                        raise DehackedFormatError(
                            f'{filename} has an unsupported patch format ({value}).'
                        )
                    continue

                line_words = line.split(' ')

                # Entry headers.
                if line.startswith('Thing ') and len(line_words) >= 3:
                    mode = ParseMode.THING
                    entry_index = int(line_words[1]) - 1
                    entry_name = ' '.join(line_words[2:])[1:-1]
                    if entry_index < 0 or entry_index >= len(self.things):
                        messages['NOTHING'] = 'The patch contains thing data that does not exist '\
                                              'in the chosen engine. It will not be loaded.'
                        entry_index = -1
                    else:
                        self.things[entry_index].name = entry_name
                    continue
                if line.startswith('Frame ') and len(line_words) >= 2:
                    mode = ParseMode.STATE
                    entry_index = int(line_words[1])
                    if entry_index < 0 or entry_index >= len(self.states):
                        messages['NOSTATE'] = 'The patch contains state data that does not exist '\
                                              'in the chosen engine. It will not be loaded.'
                        entry_index = -1
                    continue
                if line.startswith('Sound ') and len(line_words) >= 2:
                    mode = ParseMode.SOUND
                    entry_index = int(line_words[1])
                    if entry_index < 0 or entry_index >= len(self.sounds):
                        messages['NOSOUND'] = 'The patch contains sound data that does not exist '\
                                              'in the chosen engine. It will not be loaded.'
                        entry_index = -1
                    continue
                if line.startswith('Weapon ') and len(line_words) >= 3:
                    mode = ParseMode.WEAPON
                    entry_index = int(line_words[1])
                    entry_name = ' '.join(line_words[2:])[1:-1]
                    if entry_index < 0 or entry_index >= len(self.weapons):
                        messages['NOWEAPON'] = 'The patch contains weapon data that does not '\
                                               'exist in the chosen engine. It will not be loaded.'
                        entry_index = -1
                    else:
                        self.weapons[entry_index].name = entry_name
                    continue
                if line.startswith('Ammo ') and len(line_words) >= 3 and line_words[2][0] == '(':
                    mode = ParseMode.AMMO
                    entry_index = int(line_words[1])
                    entry_name = ' '.join(line_words[2:])[1:-1]
                    if entry_index < 0 or entry_index >= len(self.ammo):
                        messages['NOAMMO'] = 'The patch contains ammo data that does not exist '\
                                             'in the chosen engine. It will not be loaded.'
                        entry_index = -1
                    else:
                        self.ammo[entry_index].name = entry_name
                    continue
                if line.startswith('Sprite ') and len(line_words) == 2:
                    mode = ParseMode.SPRITE
                    entry_index = int(line_words[1])
                    messages['UNSUPPORTED_SPRITE'] = 'The patch contains sprite blocks, which '\
                                                     'are unsupported and will not be loaded.'
                    continue
                if line.startswith('Pointer ') and len(line_words) >= 4:
                    mode = ParseMode.POINTER
                    entry_index = int(line_words[3][:-1])
                    continue
                if line.startswith('Cheat 0'):
                    mode = ParseMode.CHEATS
                    continue
                if line.startswith('Misc 0'):
                    mode = ParseMode.MISC
                    continue
                if line.startswith('[PARS]'):
                    mode = ParseMode.PARS
                    continue
                if line.startswith('[CODEPTR]'):
                    mode = ParseMode.POINTERS_EXT
                    continue
                if line.startswith('[STRINGS]'):
                    mode = ParseMode.STRINGS_EXT
                    continue

                # Text header.
                if line.startswith('Text ') and len(line_words) == 3:
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
                            message_key = 'NOSTRING_' + str(len(messages))
                            messages[message_key] = f'The engine string "{original}" could not be '\
                                                    'found. It will not be loaded.'
                        else:
                            self.strings[found_key] = new

                        # Replace sprite names, so that patches can alter them
                        # without offset modifications.
                        for i, name in enumerate(self.engine.sprite_names):
                            if name == original:
                                self.sprite_names[i] = new
                                break

                        # Replace sound names, so that patches can alter them without
                        # offset modifications.
                        for i, sound in enumerate(self.engine.sounds):
                            if sound.name == original:
                                self.sounds[i].name = new
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
                            message_key = 'NOSTRING_' + str(len(messages))
                            messages[message_key] = f'The engine string "{original}" could not be '\
                                                    'found. It will not be loaded.'
                        else:
                            self.strings[key] = new

                    continue

                # Extended mode section contents.
                if mode == ParseMode.PARS:
                    if line_words[0] == 'par':
                        if len(line_words) == 4:
                            par = entries.ParEntry(self.engine.pars).from_json({
                                'episode': int(line_words[1]),
                                'map': int(line_words[2]),
                                'seconds': int(line_words[3]),
                            })

                        elif len(line_words) == 3:
                            par = entries.ParEntry(self.engine.pars).from_json({
                                'episode': 0,
                                'map': int(line_words[1]),
                                'seconds': int(line_words[2]),
                            })
                        else:
                            continue

                        self.pars.entries.append(par)

                    continue

                if mode == ParseMode.STRINGS_EXT:
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
                            value += line.lstrip()[:-1]

                    self.strings[key] = string_unescape(value)
                    continue

                if mode == ParseMode.POINTERS_EXT:
                    pair = line.split(' = ')
                    if len(pair) < 2:
                        continue

                    key = pair[0]
                    value = pair[1]
                    index = int(key.split(' ')[1])

                    if value not in self.engine.actions:
                        messages['UNKNOWN_ACTION_NAME'] = 'Unknown action name ' + value
                    elif index < 0 or index >= len(self.states):
                        messages['INVALID_CODEPOINTER'] = 'Invalid codepointer values were '\
                                                          'encountered.'
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
                    if mode == ParseMode.THING and entry_index != -1:
                        self.things[entry_index].set_patch_key(key, value)
                    elif mode == ParseMode.STATE and entry_index != -1:
                        self.states[entry_index].set_patch_key(key, value)
                    elif mode == ParseMode.SOUND and entry_index != -1:
                        self.sounds[entry_index].set_patch_key(key, value)
                    elif mode == ParseMode.WEAPON and entry_index != -1:
                        self.weapons[entry_index].set_patch_key(key, value)
                    elif mode == ParseMode.AMMO and entry_index != -1:
                        self.ammo[entry_index].set_patch_key(key, value)

                    elif mode == ParseMode.POINTER:
                        if not self.extended and entry_index not in self.engine.action_index_to_state:
                            messages['INVALID_CODEPOINTER_INDEX'] = 'A codepointer was assigned to a state that had none before. It will not be loaded.'
                        else:
                            self.states[entry_index]['action'] = self.engine.states[int(value)]['action']
                    elif mode == ParseMode.CHEATS:
                        table_key = engine.get_key_from_patchkey(self.engine.cheat_data, key)
                        if table_key is None:
                            msg_key = 'PATCH_CHEAT_KEY_' + str(len(messages))
                            messages[msg_key] = f'Unknown patch cheat key {key}. This entry '\
                                                'will be ignored.'
                        else:
                            self.cheats[table_key] = value
                    elif mode == ParseMode.MISC:
                        table_key = engine.get_key_from_patchkey(self.engine.misc_data, key)
                        if table_key is None:
                            msg_key = 'PATCH_MISC_KEY_' + str(len(messages))
                            messages[msg_key] = f'Unknown patch miscellaneous key {key}.' \
                                                'This entry will be ignored.'
                        else:
                            self.misc[table_key] = value

                except DehackedPatchError as e:
                    messages['EXCEPTION'] = 'Exceptions occurred during loading. The patch may '\
                                            'be corrupted.\n\nLast exception:\n' + str(e)

        return messages

    def get_state_name(self, state_index: int) -> str:
        """
        Returns a state's name by combining its sprite name and frame index.

        :param state_index:

        :return:
        """

        if state_index == 0:
            return '-'

        state = self.states[state_index]
        sprite_name = self.get_sprite_name(state['sprite'])
        sprite_frame = state['spriteFrame'] & ~self.FRAME_FLAG_LIT
        sprite_frame_name = chr(sprite_frame + 65)

        return sprite_name + sprite_frame_name

    def get_sprite_name(self, sprite_index: int) -> str:
        """
        Returns a sprite's name.

        :param sprite_index:

        :return:
        """

        if sprite_index < 0 or sprite_index >= len(self.sprite_names):
            return f'{sprite_index:04}'
        return self.sprite_names[sprite_index]

    def get_sound_name(self, sound_index: int) -> str:
        """
        Returns a sound's name.

        :param sound_index:

        :return:
        """

        sound_index -= 1

        # Index 0 indicates no sound.
        if sound_index == -1 or self.sounds[sound_index].unused:
            return '-'

        if sound_index > len(self.engine.sounds):
            return '????'
        return self.sounds[sound_index].name.upper()


def string_escape(string: str) -> str:
    """
    Returns an escaped string for use in Dehacked patch writing.
    """

    string = string.replace('\\', '\\\\')
    string = string.replace('\n', '\\n')
    string = string.replace('\r', '\\r')
    string = string.replace('\t', '\\t')
    string = string.replace('\"', '\\"')

    return string


def string_unescape(string: str) -> str:
    """
    Returns an escaped string for use in Dehacked patch reading.
    """

    string = string.replace('\\\\', '\\')
    string = string.replace('\\n', '\n')
    string = string.replace('\\r', '\r')
    string = string.replace('\\t', '\t')
    string = string.replace('\\"', '\"')

    return string
