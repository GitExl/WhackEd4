"""
Contains Doom WAD file reading classes.
"""

import struct
from typing import List, Optional, Dict


class WADError(Exception):
    """
    Base class for errors in WAD files.
    """

    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg


class WADTypeError(WADError):
    """
    The WAD file has an invalid type.
    """


class Lump:
    """
    A lump that is part of a WAD file.

    It is recommended to access a lump's data through the get_data() method to
    prevent having to load an entire WAD's data in memory.
    """

    def __init__(self, name: str, size: int, offset: int, owner):
        self.name: str = name
        self.size: int = size
        self.offset: int = offset
        self.data: Optional[bytes] = None
        self.owner: WAD = owner

    def get_data(self) -> bytes:
        """
        Returns this lump's data.

        If the data has not yet been read, it will open the WAD file and read
        it before returning it.
        """

        if self.data is None:
            with open(self.owner.filename, 'rb') as f:
                f.seek(self.offset)
                self.data = f.read(self.size)

        return self.data


class WAD:
    """
    Reads Doom WAD files.
    """

    TYPE_IWAD = 'IWAD'
    TYPE_PWAD = 'PWAD'

    S_HEADER = struct.Struct("<4sII")
    S_LUMP = struct.Struct("<II8s")

    def __init__(self, filename: str, wad_type: str):
        self.filename: str = filename
        self.type: str = wad_type

        self.lumps: List[Lump] = []

    @staticmethod
    def from_file(filename: str):
        """
        Reads a WAD file's header and lump directory.

        @raise WADTypeError: if the WAD file is not of a valid type (IWAD or PWAD).
        """

        with open(filename, 'rb') as f:

            # Read and validate header. Should contain PWAD or IWAD magic bytes.
            wad_type, entry_count, dir_offset = WAD.S_HEADER.unpack(f.read(WAD.S_HEADER.size))
            wad_type = wad_type.decode('ascii')
            if wad_type not in {WAD.TYPE_IWAD, WAD.TYPE_PWAD}:
                raise WADTypeError(f'Invalid WAD type "{wad_type}"')

            wad = WAD(filename, wad_type)

            # Read lump directory.
            f.seek(dir_offset)
            for _ in range(entry_count):
                offset, size, name = WAD.S_LUMP.unpack(f.read(WAD.S_LUMP.size))

                # Strip trailing NULL characters.
                decoded_name = name.decode('ascii', errors='replace')
                name = decoded_name.split('\x00')[0]

                wad.lumps.append(Lump(name, size, offset, wad))

        # chex[3].wad detection.
        if (wad_type == WAD.TYPE_PWAD and wad.get_lump('E1M1') and wad.get_lump('E3M1')
            and wad.get_lump('W94_1') and wad.get_lump('POSSH0M0')):
            wad.type = WAD.TYPE_IWAD

        return wad

    def get_lump(self, lump_name: str) -> Optional[Lump]:
        """
        Searches this WAD's lump directory for a lump by name.

        @return: the first matching lump with the specified name, or None if
        no lump with that name could be found.
        """

        for lump in reversed(self.lumps):
            if lump.name == lump_name:
                return lump

        return None

    def get_sprite_lumps(self) -> Dict[str, Lump]:
        """
        Returns a dict of all sprite lumps.
        """

        sprites = {}
        section_active = False

        # Note that these are iterated in reverse, so reverse logic applies for
        # deleting the start and end of the sprite list.
        for lump in reversed(self.lumps):
            if lump.name in {'SS_START', 'S_START'}:
                section_active = False
                continue

            if lump.name in {'SS_END', 'S_END'}:
                section_active = True
                continue

            if section_active:
                sprites[lump.name] = lump

        return sprites
