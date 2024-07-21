"""
Data table entry code.
"""

import copy

from dataclasses import dataclass
from struct import Struct
from typing import Optional, Dict, Self, BinaryIO

from whacked4.dehacked.table import Table
from whacked4.enum import WhackedEnum


class FieldType(WhackedEnum):
    """
    Known field data types.
    """

    INT = 'int'
    FLOAT = 'float'
    STRING = 'string'
    STATE = 'state'
    SOUND = 'sound'
    AMMO = 'ammo'
    SPRITE = 'sprite'
    FLAGS = 'flags'
    ACTION = 'action'
    ENUM_GAME = 'enum_game'
    ENUM_RENDER_STYLE = 'enum_render_style'


# Stores information about a Dehacked field.
@dataclass
class Field:
    """
    A single dehacked table field.
    """

    patch_key: str
    type: FieldType


class Entry:
    """
    A single entry in a Dehacked data table.
    """

    # The name of this patch entry.
    NAME: Optional[str] = None

    # The struct definition to use when reading this entry directly from an executable.
    STRUCTURE: Optional[Struct] = None

    # A dict of fields in this entry.
    FIELDS: Optional[Dict[str, Field]] = None

    def __init__(self, table: Table):
        self.name: Optional[str] = None
        self.table: Table = table
        self.values: Dict[str, any] = {}
        self.extra_values: Dict[str, any] = {}
        self.unused: bool = False

    def __getitem__(self, key: str) -> any:
        """
        Returns an item from the fields list.
        """

        return self.values[key]

    def __setitem__(self, key: str, value: any):
        """
        Sets an item in the fields list.

        @raise KeyError: if the key cannot be found.
        """

        if key not in self.values:
            raise KeyError(f'Cannot find patch key "{key}".')

        self.values[key] = value

    def __contains__(self, item: str) -> bool:
        return item in self.values

    def parse_field_value(self, key: str, value: any) -> any:
        """
        Validates a patch field value.

        @param key: The field key to validate the value against.
        @param value: The value to validate.

        @returns: A validated value.
        """

        field = self.FIELDS.get(key)

        if field.type == FieldType.FLAGS:
            return self.table.flags_parse_string(key, value)

        if field.type in {FieldType.INT, FieldType.AMMO,
                          FieldType.SOUND, FieldType.SPRITE, FieldType.STATE}:
            try:
                return int(value)
            except ValueError as e:
                raise ValueError(f'Value "{value}" for field "{key}" is not an integer.') from e

        if field.type == FieldType.FLOAT:
            try:
                return float(value)
            except ValueError as e:
                raise ValueError(f'Value "{value}" for field "{key}" is not a float.') from e

        if field.type in {FieldType.STRING, FieldType.ACTION,
                          FieldType.ENUM_GAME, FieldType.ENUM_RENDER_STYLE}:
            return str(value)

        raise ValueError(f'Unknown field value type "{field.type}".')

    def set_patch_key(self, patch_key: str, value: any):
        """
        Sets a field's value directly from a Dehacked patch key.

        @param patch_key: The key as used in a Dehacked patch.
        @param value: The value read from a Dehacked patch.

        @raise LookupError: if the patch key cannot be found in this entry.
        """

        for key, field in self.FIELDS.items():
            if field.patch_key != patch_key:
                continue

            self.values[key] = self.parse_field_value(key, value)
            return

        # No known patch key found, store it as extra values.
        self.extra_values[patch_key] = value

    def read_from_executable(self, f: BinaryIO):
        """
        Reads this entry's values from an executable.
        """

        self.values = {}
        data = self.STRUCTURE.unpack(f.read(self.STRUCTURE.size))

        for index, key in enumerate(self.FIELDS.keys()):
            self.values[key] = data[index]

        return self

    def from_json(self, json: Dict[str, any]):
        """
        Reads this entry's values from a JSON object.
        """

        if '_name' in json:
            self.name = json['_name']

        for key in self.FIELDS.keys():
            if key not in json:
                continue
            self.values[key] = self.parse_field_value(key, json[key])

        return self

    def to_json(self) -> Dict[str, any]:
        """
        Writes this entry's values to a JSON object. Currently just returns
        its values dict.
        """

        return self.values

    def get_patch_header(self, index: int, offset: int = 0) -> str:
        """
        Returns a string representing this entry's header in a Dehacked file.
        """

        if self.name is not None:
            return f'\n{self.NAME} {index + offset} ({self.name})\n'
        return f'\n{self.NAME} {index + offset}\n'

    def get_patch_string(self, original: Self) -> Optional[str]:
        """
        Returns a string with all of this entry's modified values, for writing to a
        Dehacked patch.

        @param original: The original entry containing unmodified engine data.
        """

        output = {}
        for key, field in self.FIELDS.items():

            # Skip actions, these are stored in a separate "fake" table.
            if field.type == FieldType.ACTION:
                continue

            if key not in self.values:
                continue

            # Store modified keys in an output dict.
            if self.values[key] != original.values[key]:
                output[key] = self.values[key]

        # No values were modified.
        if len(output) == 0:
            return None

        # Create a list of patch key\value pairs to output.
        output_list = []
        for key, value in output.items():
            field = self.FIELDS.get(key)

            if field.type == FieldType.FLAGS:
                value = self.table.flags_get_string(key, value)

            output_list.append(f'{field.patch_key} = {value}')

        # Add extra values.
        for key, value in self.extra_values.items():
            output_list.append(f'{key} = {value}')

        return '\n'.join(output_list) + '\n'

    def apply_defaults(self, default_entry: Self):
        """
        Apply default property values to this entry,

        :param default_entry:

        :return:
        """
        if self.name is None:
            self.name = default_entry.name

        for key, value in default_entry.values.items():
            if key not in self.values:
                self.values[key] = self.parse_field_value(key, value)

    def clone(self) -> Self:
        """
        Returns a clone of this entry.
        """

        dup = copy.copy(self)
        dup.values = copy.copy(self.values)
        dup.extra_values = copy.copy(self.extra_values)
        dup.name = self.name

        return dup

    def __repr__(self) -> str:
        return f'{self.NAME}: {self.values}'
