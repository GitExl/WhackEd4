#!/usr/bin/env python
#coding=utf8

from collections import namedtuple

from whacked4.dehacked import validators


class FieldType(object):
    """
    Known field data types.
    """

    def __init__(self):
        pass

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
Field = namedtuple('Field', ['patch_key', 'type'])


class Entry(object):

    # The name of this patch entry.
    NAME = None

    # The struct module structure definition to use when reading this entry directly from an executable.
    STRUCTURE = None

    # A dict of fields in this entry.
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
            raise KeyError('Cannot find patch key "{}".'.format(key))

        return self.values[key]

    def __setitem__(self, key, value):
        """
        Sets an item in the fields list.

        @raise KeyError: if the key cannot be found.
        """

        if key not in self.FIELDS:
            raise KeyError('Cannot find patch key "{}".'.format(key))

        self.values[key] = value

    def validate_field_value(self, key, value):
        """
        Validates a patch field value.

        @param key: The field key to validate the value against.
        @param value: The value to validate.

        @returns: A validated value.
        """

        field = self.FIELDS[key]

        if field.type == FieldType.FLAGS:
            value = validators.thing_flags_read(value, self.table)

        elif field.type == FieldType.INT or field.type == FieldType.AMMO or field.type == FieldType.SOUND or \
                field.type == FieldType.SPRITE or field.type == FieldType.STATE:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('Value "{}" for field "{}" is not an integer.'.format(value, key))

        elif field.type == FieldType.FLOAT:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('Value "{}" for field "{}" is not a float.'.format(value, key))

        elif field.type == FieldType.STRING or field.type == FieldType.ACTION or field.type == FieldType.ENUM_GAME or \
                field.type == FieldType.ENUM_RENDER_STYLE:
            value = str(value)

        return value

    def set_patch_key(self, patch_key, value):
        """
        Sets a field's value directly from a Dehacked patch key.

        @param patch_key: The key as used in a Dehacked patch.
        @param value: The value read from a Dehacked patch.

        @raise LookupError: if the patch key cannot be found in this entry.
        """

        for key, field in self.FIELDS.iteritems():
            if field.patch_key != patch_key:
                continue

            self.values[key] = self.validate_field_value(key, value)
            return

        raise LookupError('Cannot find patch key "{}".'.format(patch_key))

    def read_from_executable(self, f):
        """
        Reads this entry's values from an executable.
        """

        self.values = {}
        data = self.STRUCTURE.unpack(f.read(self.STRUCTURE.size))

        for index, key in enumerate(self.FIELDS.keys()):
            self.values[key] = data[index]

        return self

    def from_json(self, json):
        """
        Reads this entry's values from a JSON object.
        """

        self.values = {}
        for key, field in self.FIELDS.iteritems():
            self.values[key] = self.validate_field_value(key, json[key])

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

            # Skip actions, these are stored in a separate "fake" table.
            if field.type == FieldType.ACTION:
                continue

            # Store modified keys in an output dict.
            if self.values[key] != original.values[key]:
                output[key] = self.values[key]

        # No values were modified.
        if len(output) == 0:
            return None

        # Create a list of patch key\value pairs to output.
        output_list = []
        for key, value in output.iteritems():
            field = self.FIELDS[key]

            if field.type == FieldType.FLAGS:
                value = validators.thing_flags_write(value, self.table)

            output_list.append('{} = {}'.format(field.patch_key, value))

        return '\n'.join(output_list) + '\n'

    def __repr__(self):
        return '{}: {}'.format(self.NAME, self.values)
