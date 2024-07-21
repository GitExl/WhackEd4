"""
Table data storage.
"""

import copy
import math
import re
from dataclasses import dataclass
from typing import Dict, Optional, Set, BinaryIO, List

from whacked4.dehacked.engine import Engine


@dataclass
class ThingFlag:
    """
    A thing flag descriptor.
    """

    key: str
    field: str
    name: Optional[str]
    index: Optional[int]
    alias: Optional[str]
    description: Optional[str]

    @staticmethod
    def from_item(key: str, values: Dict):
        """
        Creates a new ThingFLag from JSON item data.
        """

        return ThingFlag(
            key,
            values.get('field', 'flags'),
            values.get('name', None),
            values.get('index', None),
            values.get('alias', None),
            values.get('description', None)
        )


class Table:
    """
    A table containing Dehacked entry objects.
    """

    def __init__(self, entry_class, engine: Engine):
        self.entries = []
        self.entry_class = entry_class
        self.offset = 0
        self.engine = engine
        self.flags: Dict[str, ThingFlag] = {}
        self.names = None

    def read_from_executable(self, count: int, f: BinaryIO):
        """
        Reads a number of entries from an executable.
        """

        for _ in range(count):
            self.entries.append(self.entry_class(self).read_from_executable(f))

    def read_from_json(self, json: List[Dict[str, any]]):
        """
        Reads this table's entries from a JSON object.
        """

        unused_entry = self.entry_class(self)
        unused_entry.unused = True

        index = len(self.entries)
        for json_entry in json:

            # Start from a specific index.
            if '_index' in json_entry:
                next_index = json_entry['_index']
            else:
                next_index = index

            # Add unused entries if needed.
            if next_index > len(self.entries):
                for _ in range(next_index - len(self.entries)):
                    self.entries.append(unused_entry.clone())

            # Overwrite existing entry or add a new one.
            if next_index < len(self.entries):
                self.entries[next_index].from_json(json_entry)
                self.entries[next_index].unused = False
            else:
                self.entries.append(self.entry_class(self).from_json(json_entry))

            index = next_index + 1

    def write_patch_data(self, source_table, f):
        """
        Writes this table's entry to a Dehacked patch file.
        """

        for index, entry in enumerate(self.entries):
            source_entry = source_table.entries[index]

            # Write the current entry index if it returns any data to be written.
            patch_str = entry.get_patch_string(source_entry)
            if patch_str is not None:
                f.write(entry.get_patch_header(index, offset=self.offset))
                f.write(patch_str)

            # Write just a header if only the entry's name has changed.
            elif entry.name != source_table.entries[index].name:
                f.write(entry.get_patch_header(index, offset=self.offset))

    def apply_defaults(self, defaults):
        """
        Apply defaults to each of this table's entries.
        """

        for entry in self.entries:
            entry.apply_defaults(defaults)

    def flags_parse_string(self, field_key: str, value: any):
        """
        Filters a thing's flags value.
        Extended patches can use mnemonics for flag names, separated by plus signs.

        @raise LookupError: if the value contains an unknown mnemonic.
        """
        if not isinstance(value, set):
            flag_parts = re.split(r"[,+| \t\f\r]+", str(value))
        else:
            flag_parts = value

        out = set()
        for flag_str in flag_parts:
            flag_str = flag_str.strip()

            # Flag is any number of bits.
            if flag_str.isdigit():
                keys = self._get_flag_keys_for_bits(field_key, int(flag_str))
                out.update(keys)

            # Flag is a mnemonic.
            else:
                if not self.engine.extended:
                    raise LookupError(f'Encountered thing flag key "{flag_str}" in a'
                                      f'non-extended patch.')

                flag = self.flags.get(f'{field_key}_{flag_str}')
                if flag is None:
                    raise LookupError(f'Ignoring unknown thing flag key "{flag_str}".')

                if flag.alias is not None:
                    original_flag = flag.alias
                    flag = self.flags.get(f'{field_key}_{flag.alias}')
                    if flag is None:
                        raise LookupError(f'Ignoring unknown thing flag alias "{original_flag}".')

                out.add(flag_str)

        return out

    def _get_flag_keys_for_bits(self, field_key: str, bits: int) -> Set[str]:
        out = set()

        for bit in range(0, 32):
            mask = int(math.pow(2, bit))
            if (bits & mask) == 0:
                continue

            for flag in self.flags.values():
                if flag.field != field_key or flag.index is None or flag.index != bit:
                    continue

                out.add(flag.key)
                break

        return out

    def flags_get_string(self, field_key: str, value: str):
        """
        Returns a thing flags value as a string of mnemonics.
        """

        if self.engine.extended:
            return self._flags_get_string_extended(field_key, value)
        return self._flags_get_string_vanilla(field_key, value)

    def _flags_get_string_extended(self, field_key: str, value: str):
        """
        Returns a thing flags value as a string of extended engine mnemonics.
        """

        out = []
        for key in value:
            flag_key = f'{field_key}_{key}'
            if flag_key not in self.flags:
                raise LookupError(f'Unknown thing flag key "{key}" for '
                                  f'field "{field_key}".')

            out.append(key)

        if len(out) == 0:
            return 0

        return '+'.join(out)

    def _flags_get_string_vanilla(self, field_key: str, value: str):
        """
        Returns a thing flags value as a 32-bit integer bitfield.
        """

        bits = 0
        for key in value:
            flag_key = f'{field_key}_{key}'
            flag = self.flags.get(flag_key)
            if flag.index is None:
                raise LookupError(f'Cannot write non-bitfield thing flag "{key}" into '
                                  f'a non-extended patch.')

            bits |= int(math.pow(2, flag.index))

        return bits

    def clone(self):
        """
        Returns a clone of this table.
        """

        dup = copy.copy(self)
        dup_entries = []
        for entry in self.entries:
            dup_entries.append(entry.clone())
        dup.entries = dup_entries

        if self.names is not None:
            dup.names = copy.copy(self.names)

        return dup

    def __repr__(self):
        return f'{self.entry_class}: {self.entries}'

    def __getitem__(self, index):
        return self.entries[index]

    def __setitem__(self, index, value):
        self.entries[index] = value

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        return iter(self.entries)
