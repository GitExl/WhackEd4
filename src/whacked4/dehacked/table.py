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
        self.names = None

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
        for entry in self.entries:
            entry.apply_defaults(defaults)

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
        return '{}: {}'.format(self.entry_class, self.entries)

    def __getitem__(self, index):
        return self.entries[index]

    def __setitem__(self, index, value):
        self.entries[index] = value

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        return iter(self.entries)
