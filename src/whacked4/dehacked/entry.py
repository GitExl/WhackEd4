#!/usr/bin/env python
#coding=utf8

from whacked4.dehacked import filters


class Entry(object):

    # The name of this patch entry.
    NAME = None

    # The struct module structure definition to use when reading this entry directly from an executable.
    STRUCTURE = None

    # A dict of fields in this entry.
    # [internal key] = Dehacked patch key
    FIELDS = None

    # A list of fields to skip when writing a Dehacked patch.
    SKIP = None

    # A dict of fields that are run through a filter when read or written.
    # See dehacked.filters module.
    # [internal key] = filter function base name
    FILTER = None

    def __init__(self):
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

    def set_patch_key(self, key, value, table, extended):
        """
        Sets a field's value directly from a Dehacked patch key.

        @param key: The key as used in a Dehacked patch.
        @param value: The value read from a Dehacked patch.
        @param table: The table that this entry is a part of.
        @param extended: Set to True if this entry is from an extended engine.

        @raise ValueError: if the read value is not a number.
        @raise LookupError: if the patch key cannot be found in this entry.
        """

        for internalKey, patchKey in self.FIELDS.iteritems():

            if patchKey == key:
                # Filter the read value first.
                # Filter only if this entry has a FILTER and if the internal key has a filter function
                # associated with it.
                if self.FILTER is not None and internalKey in self.FILTER:
                    value = filters.__dict__[self.FILTER[internalKey] + '_read'](value, table, extended)

                # Validate expected integer values.
                if type(value) is not set:
                    try:
                        value = int(value)
                    except ValueError:
                        raise ValueError('Value {} for {} is not a number.'.format(value, key))

                self[internalKey] = value
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

    def from_json(self, json, table, extended):
        """
        Reads this entry's values from a JSON object.
        """

        self.values = {}

        for key in self.FIELDS.keys():
            value = json[key]
            if self.FILTER is not None and key in self.FILTER:
                value = filters.__dict__[self.FILTER[key] + '_read'](value, table, extended)
            self.values[key] = value

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

    def get_patch_string(self, original, table, extended):
        """
        Returns a string with all of this entry's modified values.

        @param original: The original entry containing unmodified engine data.
        @param table: The table that this entry belongs to.
        @param extended: Set to True if a filter is for an extended engine.
        """

        output = {}

        for key in self.FIELDS.keys():
            # Skip this entry if needed.
            if self.SKIP is not None and key in self.SKIP:
                continue

            # Store modified keys in an output dict.
            if self[key] != original[key]:
                output[key] = self[key]

        if len(output) > 0:
            output_list = []

            # Create a list of patch key\value pairs to output.
            for key, value in output.iteritems():

                # Filter the value about to be written to the patch.
                if self.FILTER is not None and key in self.FILTER:
                    value = filters.__dict__[self.FILTER[key] + '_write'](value, table, extended)

                output_list.append('{} = {}\n'.format(self.FIELDS[key], value))

            return ''.join(output_list)

        # No values were modified.
        return None

    def __repr__(self):
        return '{}: {}'.format(self.NAME, self.values)
