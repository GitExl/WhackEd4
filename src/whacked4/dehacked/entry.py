#!/usr/bin/env python
#coding=utf8

from whacked4.dehacked import filters
from whacked4.dehacked.entries import FieldType


class Entry(object):

    # The name of this patch entry.
    NAME = None

    # The struct module structure definition to use when reading this entry directly from an executable.
    STRUCTURE = None

    # A dict of fields in this entry.
    # [internal key] = Dehacked patch key
    FIELDS = None

    def __init__(self, table):
        self.table = table

        self.values = {}
        for key in self.FIELDS.keys():
            self.values[key] = None

    def __getitem__(self, key):
        """
        Returns an item from the fields list.

        @raise KeyError: If the key cannot be found.
        """

        if key not in self.FIELDS:
            raise KeyError('Cannot find {}'.format(key))

        return self.values[key]

    def __setitem__(self, key, value):
        """
        Sets an item in the fields list.

        @raise KeyError: if the key cannot be found.
        """

        if key not in self.FIELDS:
            raise KeyError('Cannot find {}'.format(key))

        self.values[key] = value

    def validate_field_value(self, value, key):
        """
        Validates a patch field value.

        @param value: The value to filter.
        @param key: The field key to filter the value against.

        @returns: A filtered value.
        """

        field = self.FIELDS[key]

        if field.type == FieldType.FLAGS:
            value = filters.filter_thing_flags_read(value, self.table)

        elif field.type == FieldType.INT or field.type == FieldType.ACTION or field.type == FieldType.AMMO or \
                field.type == FieldType.SOUND or field.type == FieldType.SPRITE or field.type == FieldType.STATE:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('Value "{}" for field "{}" is not an integer.'.format(value, key))

        elif field.type == FieldType.FLOAT:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('Value "{}" for field "{}" is not a float.'.format(value, key))

        elif field.type == FieldType.STRING:
            value = str(value)

        return value

    def set_patch_key(self, key, value):
        """
        Sets a field's value directly from a Dehacked patch key.

        @param key: The key as used in a Dehacked patch.
        @param value: The value read from a Dehacked patch.

        @raise ValueError: if the read value is not a number.
        @raise LookupError: if the patch key cannot be found in this entry.
        """

        for internal_key, field in self.FIELDS.iteritems():
            if field.patch_key != key:
                continue

            self[internal_key] = self.validate_field_value(value, field)
            return

        raise LookupError('Cannot find patch key {}'.format(key))

    def read_from_executable(self, f):
        """
        Reads this entry's values from an executable.
        """

        self.values = {}
        data = self.STRUCTURE.unpack(f.read(self.STRUCTURE.size))

        index = 0
        for key in self.FIELDS.keys():
            self.values[key] = data[index]
            index += 1

        return self

    def from_json(self, json):
        """
        Reads this entry's values from a JSON object.
        """

        self.values = {}
        for key, field in self.FIELDS.iteritems():
            self.values[key] = self.validate_field_value(json[key], field)

        return self

    def to_json(self):
        """
        Writes this entry's values to a JSON object. Currently just returns it's values dict.
        """

        return self.values

    def get_patch_header(self, index, table, offset=0):
        """
        Returns a string representing this entry's header in a Dehacked file.
        """

        if hasattr(table, 'names'):
            return '\n{} {} ({})\n'.format(self.NAME, index + offset, table.names[index])
        else:
            return '\n{} {}\n'.format(self.NAME, index + offset)

    def get_patch_string(self, original):
        """
        Returns a string with all of this entry's modified values, for writing to a Dehacked patch.

        @param original: The original entry containing unmodified engine data.
        """

        output = {}

        for key, field in self.FIELDS.iteritems():

            # Skip this entry if needed.
            if field.type == FieldType.ACTION:
                continue

            # Store modified keys in an output dict.
            if self[key] != original[key]:
                output[key] = self[key]

        # No values were modified.
        if len(output) == 0:
            return None

        # Create a list of patch key\value pairs to output.
        output_list = []
        for key, value in output.iteritems():
            field = self.FIELDS[key]

            if field.type == FieldType.FLAGS:
                value = filters.filter_thing_flags_write(value, self.table)

            output_list.append('{} = {}\n'.format(field.patch_key, value))

        return ''.join(output_list)

    def __repr__(self):
        return '{}: {}'.format(self.NAME, self.values)
