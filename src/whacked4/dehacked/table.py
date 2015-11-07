#!/usr/bin/env python
#coding=utf8

import copy


class Table(object):
    """
    A table containing Dehacked entry objects.
    """

    def __init__(self, entry_class, engine):
        self.entries = []
        self.entry_class = entry_class
        self.offset = 0
        self.engine = engine

    def read_from_executable(self, count, f):
        """
        Reads a number of entries from an executable.
        """

        for _ in range(count):
            self.entries.append(self.entry_class(self).read_from_executable(f))

    def read_from_json(self, json):
        """
        Reads this table's entries from a JSON object.
        """

        for json_entry in json:
            self.entries.append(self.entry_class(self).from_json(json_entry))

    def write_patch_data(self, source_table, f):
        """
        Writes this table's entry to a Dehacked patch file.
        """

        for index in range(len(self.entries)):
            entry = self.entries[index]
            source_entry = source_table.entries[index]

            # Write the current entry index if it returns any data to be written.
            patch_str = entry.get_patch_string(source_entry)
            if patch_str is not None:
                f.write(entry.get_patch_header(index, self, offset=self.offset))
                f.write(patch_str)

            # Write just a header if only the entry's name has changed.
            elif hasattr(self, 'names') and self.names[index] != source_table.names[index]:
                f.write(entry.get_patch_header(index, self, offset=self.offset))

    def clone(self):
        """
        Returns a clone of this table.
        """

        dup = copy.copy(self)
        dup_entries = []
        for entry in self.entries:
            dup_entries.append(entry.clone())
        dup.entries = dup_entries

        return dup


    def __repr__(self):
        return '{}: {}'.format(self.entry_class, self.entries)

    def __getitem__(self, index):
        return self.entries[index]

    def __setitem__(self, index, value):
        self.entries[index] = value

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        return iter(self.entries)
