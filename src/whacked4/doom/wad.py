#!/usr/bin/env python
#coding=utf8

"""
Contains Doom WAD file reading classes.
"""

import struct


class WADError(Exception):
    """
    Base class for errors in WAD files.
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class WADTypeError(WADError):
    """
    The WAD file has an invalid type.
    """


class Lump(object):
    """
    A lump that is part of a WAD file.

    It is recommended to access a lump's data through the get_data() method to prevent having to load an entire
    WAD's data in memory.
    """

    def __init__(self, name, size, offset, owner):
        self.name = name
        self.size = size
        self.offset = offset
        self.data = None
        self.owner = owner

    def get_data(self):
        """
        Returns this lump's data.

        If the data has not yet been read, it will open the WAD file and read it before returning it.
        """

        if self.data is None:
            with open(self.owner.filename, 'rb') as f:
                f.seek(self.offset)
                self.data = f.read(self.size)

        return self.data


class WADReader(object):
    """
    Reads Doom WAD files.
    """

    TYPE_IWAD = 'IWAD'
    TYPE_PWAD = 'PWAD'

    S_HEADER = struct.Struct("<4sII")
    S_LUMP = struct.Struct("<II8s")

    def __init__(self, filename):
        self.filename = None
        self.lumps = None
        self.type = None

        self.read(filename)

    def read(self, filename):
        """
        Reads a WAD file's header and lump directory.

        @raise WADTypeError: if the WAD file is not of a valid type (IWAD or PWAD).
        """

        with open(filename, 'rb') as f:

            # Read and validate header. Should contain PWAD or IWAD magic bytes.
            wad_type, entry_count, dir_offset = self.S_HEADER.unpack(f.read(self.S_HEADER.size))
            wad_type = wad_type.decode('ascii')
            if wad_type != self.TYPE_IWAD and wad_type != self.TYPE_PWAD:
                raise WADTypeError('Invalid WAD type "{}"'.format(type))

            # Read lump directory.
            f.seek(dir_offset)
            self.lumps = []
            for _ in range(entry_count):
                offset, size, name = self.S_LUMP.unpack(f.read(self.S_LUMP.size))

                # Strip trailing NULL characters.
                name = name.decode('ascii').split('\x00')[0]

                self.lumps.append(Lump(name, size, offset, self))

        self.filename = filename
        self.type = wad_type

    def get_lump(self, lump_name):
        """
        Searches this WAD's lump directory for a lump by name.

        @return: the first matching lump with the specified name, or None if no lump with that name could be found.
        """

        for lump in reversed(self.lumps):
            if lump.name == lump_name:
                return lump

        return None

    def get_sprite_lumps(self):
        sprites = {}
        section_active = False

        # Note that these are iterated in reverse, so reverse logic applies for deleting the start and end of
        # the sprite list.
        for lump in reversed(self.lumps):
            if lump.name == 'SS_START' or lump.name == 'S_START':
                section_active = False
                continue
            elif lump.name == 'SS_END' or lump.name == 'S_END':
                section_active = True
                continue
            elif section_active:
                sprites[lump.name] = lump

        return sprites
