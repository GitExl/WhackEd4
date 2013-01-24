#!/usr/bin/env python
#coding=utf8

"""
This module contains classes to create, read and write Dehacked patches.
"""

from app import config
from dehacked import entries
import copy


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
     

class Patch:
    """
    A Dehacked patch object.
    
    This is initialized from an engine object's data tables.
    """
    
    FRAMEFLAG_LIT = 0x8000


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
        
        
    def initialize_from_engine(self, engine):
        """
        Initializes this patch with the data from an engine.
        """
        
        self.engine = engine
        
        self.things = copy.deepcopy(engine.things)
        self.states = copy.deepcopy(engine.states)
        self.sounds = copy.deepcopy(engine.sounds)
        self.weapons = copy.deepcopy(engine.weapons)
        self.ammo = copy.deepcopy(engine.ammo)
        self.strings = copy.deepcopy(engine.strings)
        self.cheats = copy.deepcopy(engine.cheats)
        self.misc = copy.deepcopy(engine.misc)
        self.sprite_names = copy.deepcopy(engine.sprite_names)
        self.sound_names = copy.deepcopy(engine.sound_names)
        
        if engine.extended == True:
            self.pars = []
        
    
    def write_dehacked(self, filename):
        """
        Writes this patch to a Dehacked file.
        """
        
        with open(filename, 'w') as f:
            # Write header.
            f.write('Patch File for DeHackEd v3.0\n')
            f.write('# Created with {} {}\n'.format(config.APP_NAME, config.APP_VERSION))
            f.write('# Note: Use the pound sign (\'#\') to start comment lines.\n\n')
            
            f.write('Doom version = {}\n'.format(self.version))
            f.write('Patch format = 6\n\n')
            
            # Write tables.
            self.things.write_patch_data(self.engine.things, f, self.extended)
            self.states.write_patch_data(self.engine.states, f, False)
            self.sounds.write_patch_data(self.engine.sounds, f, False)
            self.weapons.write_patch_data(self.engine.weapons, f, False)
            self.ammo.write_patch_data(self.engine.ammo, f, False)
            
            # Write simple sections.
            self.write_dict(f, self.cheats, self.engine.cheats, self.engine.cheat_data, 'Cheat 0')
            self.write_dict(f, self.misc, self.engine.misc, self.engine.misc_data, 'Misc 0')
            
            # Write code pointers.
            self.write_patch_codepointers(f)
            
            # Write simple strings.
            if self.extended == False:
                self.write_patch_strings(f)
            
            # Write extended data.    
            if self.extended == True:
                self.write_patch_pars(f)
                self.write_patch_ext_strings(f)


    def write_patch_strings(self, f):
        """
        Writes this patch's strings in Dehacked format.
        
        Text [original length] [new length]
        [original string data][new string data]
        """
        
        # Create a list of modified strings.
        out = []
        for index in range(len(self.strings)):
            if self.strings[index] != self.engine.strings[index]:
                out.append(index)
        
        # Write modified strings to the patch file.
        if len(out) > 0:
            for index in out:
                f.write('\nText {} {}\n'.format(len(self.engine.strings[index]), len(self.strings[index])))
                f.write('{}{}'.format(self.engine.strings[index], self.strings[index]))
                
    
    def write_patch_ext_strings(self, f):
        """
        Writes this aptch's strings in extended Deahcked format.
        
        [STRINGS]
        [string key] = [escaped string]
        """
        
        # Create a list of modified strings.
        out = {}
        for key, value in self.strings.iteritems():
            if value != self.engine.strings[key]:
                out[key] = value
        
        # Write modified string to the patch file.
        if len(out) > 0:
            f.write('\n[STRINGS]\n')
            for name, string in out.iteritems():
                f.write('{} = {}\n'.format(name, self.string_escape(string)))
    
    
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
        
        if self.extended == False:
            # For non-extended patches, each state's action has an index. States without an action are skipped.
            # When writing these action pointers to a patch file, state actions are matched to action pointer indices.
            # Their value refers to a state in the original engine data with this particular action.
            for i in range(len(self.states)):
                actionpointer = self.states[i]['action']
                
                if actionpointer != self.engine.states[i]['action']:
                    # Attempt to find this state's action pointer index in the action index lookup list.
                    try:
                        actionpointer_index = self.engine.action_index_to_state.index(i)
                    except ValueError:
                        raise LookupError('Cannot find an action pointer index for state {}'.format(i))
                
                    # Find a state in the engine state table that uses the new action pointer.
                    state_index = -1
                    for j in range(len(self.engine.states)):
                        if self.engine.states[j]['action'] == actionpointer:
                            state_index = j
                            break
                        
                    if state_index == -1:
                        raise LookupError('Cannot find a state for action pointer {}'.format(actionpointer))
                
                    f.write('\nPointer {} (Frame {})\n'.format(actionpointer_index, i))
                    f.write('Codep Frame = {}\n'.format(state_index))
        
        else:
            out = {}
            
            # Create a dict of modified actions.
            # [state index] = action pointer
            for index in range(len(self.states)):
                actionpointer = self.states[index]['action']
                if actionpointer != self.engine.states[index]['action']:
                    out[index] = actionpointer
                    
            if len(out) > 0:
                f.write('\n[CODEPTR]\n')
                for index, action in out.iteritems():
                    f.write('FRAME {} = {}\n'.format(index, action))
    
    
    def write_dict(self, f, items, source_items, data, header):
        """
        Writes a dictionary of key\value pairs to a Dehacked patch file, if they have been modified compared to a
        source dict.
        
        @param f: the file object to write to.
        @param items: the modified item dict.
        @param source_items: the original item dict.
        @param data: a dictionary containing information about each key\value pair that is written to the Dehacked
        file. Each value is another dict containing at least a 'patchKey' item that describes what key to write to the file.   
        """
        
        # Build a list of modified items.
        out = {}
        for key, item in items.iteritems():
            if item != source_items[key]:
                out[data[key]['patchKey']] = item
                
        if len(out) > 0:
            f.write('\n{}\n'.format(header))
            for key in out:
                f.write('{} = {}\n'.format(key, out[key]))
                
                
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
                    for engine in engines.itervalues():
                        if version in engine.versions and self.extended == engine.extended:
                            self.version = version
                            break
                    
                    if self.version == 0:
                        raise DehackedVersionError('{} with engine version {} does not match any supported engine version.'.format(filename, version))

                # Detect extended patches from section headers.
                elif line.startswith('[') and line.endswith(']'):
                    self.extended = True
                
                # Detect extended patches from thing flag mnemonics.
                elif line.startswith('Bits = ') and line[7:].isdigit() == False:
                    self.extended = True
                
                # Detect normal patches from action pointer values in frames.
                # Mixing action pointers and [CODEPTR] blocks does not make sense.
                elif line.startswith('Action pointer = '):
                    if self.extended == True:
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
        
        # Parsing modes.
        MODE_NOTHING = 0
        MODE_THING = 1
        MODE_STATE = 2
        MODE_SOUND = 3
        MODE_WEAPON = 4
        MODE_AMMO = 5
        MODE_SPRITE = 6
        MODE_POINTER = 7
        MODE_STRING = 8
        MODE_MISC = 9
        MODE_CHEATS = 10
        MODE_PARS = 11
        MODE_STRINGS_EXT = 12
        MODE_POINTERS_EXT = 13
        
        # State.
        valid = False
        mode = MODE_NOTHING
        entry_index = -1
        entry_len1 = 0
        entry_len2 = 0
        entry_name = None
        
        # A dict of messages to return.
        messages = {}
        
        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line[:-1].strip()

                # Skip comment lines and empty lines.
                if len(line) == 0 or line[0].startswith('#') == True:
                    continue
                
                # Validate header line.
                if mode == MODE_NOTHING:
                    if line == 'Patch File for DeHackEd v3.0':
                        valid = True
                if valid == False:
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
                    mode = MODE_THING
                    entry_index = int(line_words[1]) - 1
                    entry_name = ' '.join(line_words[2:])[1:-1]
                    continue
                elif line.startswith('Frame ') and len(line_words) == 2:
                    mode = MODE_STATE
                    entry_index = int(line_words[1])
                    continue
                elif line.startswith('Sound ') and len(line_words) == 2:
                    mode = MODE_SOUND
                    entry_index = int(line_words[1])
                    continue
                elif line.startswith('Weapon ') and len(line_words) >= 3:
                    mode = MODE_WEAPON
                    entry_index = int(line_words[1])
                    entry_name = ' '.join(line_words[2:])[1:-1]
                    continue
                elif line.startswith('Ammo ') and len(line_words) >= 3 and line_words[2][0] == '(':
                    mode = MODE_AMMO
                    entry_index = int(line_words[1])
                    entry_name = ' '.join(line_words[2:])[1:-1]
                    continue
                elif line.startswith('Sprite ') and len(line_words) == 2:
                    mode = MODE_SPRITE
                    entry_index = int(line_words[1])
                    messages['UNSUPPORTED_SPRITE'] = 'The patch contains sprite blocks, which are unsupported and will not be loaded.'
                    continue
                elif line.startswith('Pointer ') and len(line_words) >= 4:
                    mode = MODE_POINTER
                    entry_index = int(line_words[3][:-1])
                    continue
                elif line.startswith('Cheat 0'):
                    mode = MODE_CHEATS
                    continue
                elif line.startswith('Misc 0'):
                    mode = MODE_MISC
                    continue
                elif line.startswith('[PARS]'):
                    mode = MODE_PARS
                    continue
                elif line.startswith('[CODEPTR]'):
                    mode = MODE_POINTERS_EXT
                    continue
                elif line.startswith('[STRINGS]'):
                    mode = MODE_STRINGS_EXT
                    continue
                
                # Text header.
                elif line.startswith('Text ') and len(line_words) == 3:
                    mode = MODE_STRING
                    
                    entry_len1 = int(line_words[1])
                    entry_len2 = int(line_words[2])
                    
                    original = f.read(entry_len1)
                    new = f.read(entry_len2)
                    
                    # Match strings to one in the original engine string table.
                    if self.extended == False:
                        index = -1
                        for i in range(len(self.strings)):
                            if self.strings[i] == original:
                                index = i
                                break
                        
                        if index == -1:
                            messages['NOSTRING_' + str(len(messages))] = 'The engine string "{}" could not be found. It will not be loaded.'.format(original)
                        
                        self.strings[index] = new
                        
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
                        for string_key, text in self.strings.iteritems():
                            if text == original:
                                key = string_key
                                break
                        
                        if key is None:
                            messages['NOSTRING_' + str(len(messages))] = 'The engine string "{}" could not be found. It will not be loaded.'.format(original)
                        else:
                            self.strings[key] = new
                    
                    continue

                # Extended mode section contents.
                if mode == MODE_PARS:
                    if line_words[0] == 'par':
                        par = entries.ParEntry()
                        
                        if len(line_words) == 4:
                            par['episode'] = int(line_words[1])
                            par['map'] = int(line_words[2])
                            par['seconds'] = int(line_words[3])
                        elif len(line_words) == 3:
                            par['map'] = int(line_words[1])
                            par['seconds'] = int(line_words[2])
                        else:
                            continue
                            
                        self.pars.append(par)
                    
                    continue
                
                elif mode == MODE_STRINGS_EXT:
                    pair = line.split(' = ')
                    if len(pair) < 2:
                        continue
                    
                    key = pair[0]
                    value = pair[1]
                    
                    # Read multiline strings.
                    if line.endswith('\\') == True:
                        
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
                            if line.endswith('\\') == False:
                                value += line.lstrip()
                                break
                            else:
                                value += line.lstrip()[:-1]
                    
                    self.strings[key] = self.string_unescape(value)
                    continue
                
                elif mode == MODE_POINTERS_EXT:
                    pair = line.split(' = ')
                    if len(pair) < 2:
                        continue
                    
                    key = pair[0]
                    value = pair[1]
                    index = int(key.split(' ')[1])
                    self.states[index]['action'] = value
                    continue
            
                # Key\value pairs.
                pair = line.split(' = ', 1)
                if len(pair) != 2:
                    continue
                key = pair[0]
                value = pair[1]
                 
                if mode == MODE_THING:
                    self.things.names[entry_index] = entry_name
                    self.things[entry_index].set_patch_key(key, value, self.things, self.extended)
                elif mode == MODE_STATE:
                    self.states[entry_index].set_patch_key(key, value, self.states, False)
                elif mode == MODE_SOUND:
                    self.sounds[entry_index].set_patch_key(key, value, self.sounds, False)
                elif mode == MODE_WEAPON:
                    self.weapons.names[entry_index] = entry_name
                    self.weapons[entry_index].set_patch_key(key, value, self.weapons, False)
                elif mode == MODE_AMMO:
                    self.ammo.names[entry_index] = entry_name
                    self.ammo[entry_index].set_patch_key(key, value, self.ammo, False)
                elif mode == MODE_SPRITE:
                    pass
                elif mode == MODE_POINTER:
                    self.states[entry_index]['action'] = self.engine.states[int(value)]['action']
                elif mode == MODE_CHEATS:
                    key = self.engine.get_key_from_patchkey(self.engine.cheat_data, key)
                    self.cheats[key] = value
                elif mode == MODE_MISC:
                    key = self.engine.get_key_from_patchkey(self.engine.misc_data, key)
                    self.misc[key] = value
        
        return messages
                    
                    
    def get_state_name(self, state_index):
        """
        Returns a state's name by combining it's sprite name and frame index.
        """
        
        if state_index == 0:
            return '-'
        
        state = self.states[state_index]
        
        # Get sprite frame character.
        sprite_frame = state['spriteFrame'] & ~self.FRAMEFLAG_LIT
        sprite_frame = chr(sprite_frame + 65)
        
        # Get sprite name.
        sprite_index = state['sprite']
        if sprite_index >= len(self.sprite_names):
            sprite_name = '????'
        else:
            sprite_name = self.sprite_names[sprite_index]
        
        return '{}{}'.format(sprite_name, sprite_frame)
    
    
    def get_sound_name(self, sound_index):
        """
        Returns a sound's name.
        """
        
        # Index 0 indicates no sound.
        if sound_index == 0:
            return '-'
        
        if sound_index > len(self.engine.sound_names):
            return '????'
        else:
            return self.engine.sound_names[sound_index - 1].upper()
        
        
    def string_escape(self, string):
        """
        Returns an escaped string for use in Dehacked patch writing.
        """
        
        string = string.replace('\\', '\\\\')
        string = string.replace('\n', '\\n')
        string = string.replace('\r', '\\r')
        string = string.replace('\t', '\\t')
        string = string.replace('\"', '\\"')
        
        return string
    
    
    def string_unescape(self, string):
        """
        Returns an escaped string for use in Dehacked patch reading.
        """
        
        string = string.replace('\\\\', '\\')
        string = string.replace('\\n', '\n')
        string = string.replace('\\r', '\r')
        string = string.replace('\\t', '\t')
        string = string.replace('\\"', '\"')
        
        return string