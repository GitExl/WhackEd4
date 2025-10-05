"""
WAD list and sprite management.
"""

from collections import OrderedDict
from typing import Dict, List, Optional, Tuple

from whacked4.doom import sound, graphics
from whacked4.doom.graphics import Image, Palette
from whacked4.doom.sound import Sound
from whacked4.doom.wad import Lump, WAD


class SpriteFrame:
    """
    Describes a sprite's animation frame and all of its possible rotations.
    """

    def __init__(self, index: str):
        self.index: str = index
        self.rotations: Dict[int, Lump] = {}
        self.is_mirrored: Dict[int, bool] = {}
        self.has_rotations: bool = False

    def add_rotation(self, rotation: int, lump: Lump, is_mirrored: bool):
        """
        Adds a new rotation to this frame. Any 0-rotations will overwrite all others.
        See https://github.com/id-Software/DOOM/blob/master/linuxdoom-1.10/r_things.c#L101
        """

        if rotation == 0:
            self.rotations = {0: lump}
            self.is_mirrored = {0: False}
            self.has_rotations = False

        else:
            self.rotations[int(rotation)] = lump
            self.is_mirrored[int(rotation)] = is_mirrored
            self.has_rotations = True

    def get_rotation_lump(self, rotation: int) -> Tuple[Lump, bool]:
        """
        Returns a sprite lump for a given rotation.

        :param rotation: rotation index
        """

        return self.rotations.get(rotation, None), self.is_mirrored.get(rotation, False)


class SpriteEntry:
    """
    Defines a sprite entry and it's frames and rotations.
    """

    def __init__(self, name: str):
        self.name: str = name

        self.frames: Dict[str, SpriteFrame] = {}

    def add_frame(self, frame_name: str, rotation: int, lump: Lump, is_mirrored: bool):
        """
        Adds a new frame to this sprite.

        :param frame_name: 4 character name
        :param rotation: rotation index
        :param lump: lump with image data
        :param is_mirrored: is this a mirrored version of another rotation?
        """

        if frame_name not in self.frames:
            frame = SpriteFrame(frame_name)
            self.frames[frame_name] = frame
        else:
            frame = self.frames[frame_name]

        frame.add_rotation(rotation, lump, is_mirrored)

    def get_frame_lump(self, frame_name: str, rotation: int) -> Tuple[Optional[Lump], bool]:
        """
       Returns a lump for a given frame.

        :param frame_name: 4 character frame name
        :param rotation: rotation index
        """

        frame = self.frames.get(frame_name, None)
        if frame:
            return frame.get_rotation_lump(rotation)

        return None, False


class WADList:
    """
    Maintains a list of WAD files that can be queried for specific lump data.
    """

    def __init__(self):
        self.wads: List[WAD] = []

        self.sprites: Dict[str, SpriteEntry] = {}
        self.sprite_image_cache: Dict[str, Image] = {}

        self.palette: Optional[Palette] = None

        self.sound_cache: Dict[str, Sound] = {}

    def clear(self):
        """
        Empties this WAD list of all data.
        """

        self.wads.clear()

        self.sprites.clear()
        self.sprite_image_cache.clear()
        self.palette = None

        self.sound_cache.clear()

    def add_wad(self, wad: WAD):
        """
        Adds a new WAD to this list.
        """

        self.wads.append(wad)

    def get_lump(self, lump_name: str) -> Optional[Lump]:
        """
        Returns a lump with the specified name.

        The last WAD is searched first, in reverse order. This way the lumps in the last
        WAD that was added will override any that were in previously added ones.

        @return: a lump object, or None if the lump could not be found.
        """

        for wad in reversed(self.wads):
            lump = wad.get_lump(lump_name)
            if lump is not None:
                return lump

        return None

    def get_sound(self, lump_name: str) -> Optional[Sound]:
        """
        Returns a sound object for a lump name.

        The sound object is cached automatically.
        """

        if lump_name in self.sound_cache:
            return self.sound_cache[lump_name]

        lump = self.get_lump(lump_name)
        if lump is None:
            return None

        sound_data = sound.Sound()
        sound_data.read_from(lump.get_data())
        self.sound_cache[lump_name] = sound_data

        return sound_data

    def get_sprite_lump(
        self,
        sprite_name: str,
        frame_index: int = 0,
        rotation: int = 0
    ) -> Tuple[Optional[Lump], bool]:
        """
        Returns a sprite entry from this WAD list.

        @param sprite_name: the 4 character name of the sprite to return.
        @param frame_index: the index of the sprite frame to return.
        @param rotation: the rotation of the sprite to return.

        @return: a Lump and is_mirrored bool of the requested sprite.
        """

        if sprite_name not in self.sprites:
            return None, False

        sprite = self.sprites[sprite_name]
        frame_name = chr(frame_index + 65)
        rotation = int(rotation)

        return sprite.get_frame_lump(frame_name, rotation)

    def get_sprite_image(self, lump: Lump, mirror: bool) -> Optional[Image]:
        """
        Returns an image object from a sprite lump.

        Previously requested sprites are cached so that they will not have to be
        rendered again. A palette has to be loaded for this function to work.
        """

        if self.palette is None:
            return None

        if mirror:
            lump_name = f'{lump.name}M'
        else:
            lump_name = lump.name

        if lump_name in self.sprite_image_cache:
            return self.sprite_image_cache[lump_name]

        image = Image.from_doom_patch(lump.get_data(), self.palette, mirror)

        # Add the loaded image to the cache.
        self.sprite_image_cache[lump_name] = image

        return image

    def build_sprite_list(self):
        """
        Builds a lookup table of sprite lumps, and loads a PLAYPAL palette
        from the current WAD list.
        """

        sprite_lumps: Dict[str, Lump] = OrderedDict()
        for wad in self.wads:
            sprite_lumps.update(wad.get_sprite_lumps())

        # Create a list of sprite names.
        for name in sprite_lumps.keys():
            sprite_name = name[0:4]
            self.sprites[sprite_name] = SpriteEntry(sprite_name)

        # Add sprite lumps for each sprite.
        for sprite_key, sprite_entry in self.sprites.items():

            for lump_name, lump in sprite_lumps.items():
                if len(lump_name) < 6:
                    continue

                if lump_name[0:4] != sprite_key:
                    continue

                frame = lump_name[4]
                try:
                    rotation = int(lump_name[5])
                except ValueError:
                    continue

                sprite_entry.add_frame(frame, rotation, lump, False)

                # Mirrored sprite lump.
                if len(lump_name) == 8:
                    frame = lump_name[6]
                    rotation = int(lump_name[7])
                    sprite_entry.add_frame(frame, rotation, lump, True)

        # Find a PLAYPAL lump to use as palette.
        playpal = self.get_lump('PLAYPAL')
        if playpal is not None:
            self.palette = graphics.Palette(playpal.get_data())

    def __len__(self) -> int:
        return len(self.wads)
