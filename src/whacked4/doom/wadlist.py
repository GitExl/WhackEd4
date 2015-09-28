#!/usr/bin/env python
#coding=utf8

from collections import namedtuple

from whacked4.doom import sound, graphics


SpriteEntry = namedtuple('SpriteEntry', ['lump', 'is_mirrored'])


class WADList(object):
    """
    Maintains a list of WAD files that can be queried for specific lump data.
    """

    def __init__(self):
        self.wads = None

        self.sprites = None
        self.sprite_image_cache = None
        self.palette = None

        self.sound_cache = None

        self.clear()

    def clear(self):
        """
        Empties this WAD list of all data.
        """

        self.wads = []

        self.sprites = {}
        self.sprite_image_cache = {}
        self.palette = None

        self.sound_cache = {}

    def add_wad(self, wad):
        """
        Adds a new WAD to this list.
        """

        self.wads.append(wad)

    def get_lump(self, lump_name):
        """
        Returns a lump with the specified name.

        The last WAD is searched first, in reverse order. This way the lumps in the last WAD that was added will
        override any that were in previously added ones.

        @return: a lump object, or None if the lump could not be found.
        """

        for wad in reversed(self.wads):
            lump = wad.get_lump(lump_name)
            if lump is not None:
                return lump

        return None

    def get_sound(self, lump_name):
        """
        Returns a sound object for a lump name.

        The sound object is cached automatically.
        """

        if lump_name in self.sound_cache:
            return self.sound_cache[lump_name]

        lump = self.get_lump(lump_name)
        if lump is None:
            return

        sound_data = sound.Sound()
        sound_data.read_from(lump.get_data())
        self.sound_cache[lump_name] = sound_data

        return sound_data

    def get_sprite_entry(self, sprite_name, frame_index=0, rotation=0):
        """
        Returns a sprite entry from this WAD list.

        @param sprite_name: the 4 character name of the sprite to return.
        @param frame_index: the index of the sprite frame to return.
        @param rotation: the rotation of the sprite to return.

        @return: a SpriteEntry namedtuple of the requested sprite.
        """

        if sprite_name not in self.sprites:
            return None

        sprite = self.sprites[sprite_name]
        subsprite_string = chr(frame_index + 65) + str(rotation)

        if subsprite_string not in sprite:
            return None

        return sprite[subsprite_string]

    def get_sprite_image(self, lump, mirror):
        """
        Returns an image object from a sprite lump.

        Previously requested sprites are cached so that they will not have to be rendered again. A palette has to be
        loaded for this function to work.
        """

        if self.palette is None:
            return None

        if mirror:
            lump_name = '{}M'.format(lump.name)
        else:
            lump_name = lump.name

        if lump_name in self.sprite_image_cache:
            return self.sprite_image_cache[lump_name]

        image = graphics.Image(lump.get_data(), self.palette, mirror)

        # Add the loaded image to the cache.
        self.sprite_image_cache[lump_name] = image

        return image

    def build_sprite_list(self):
        """
        Builds a lookup table of sprite lumps, and loads a PLAYPAL palette from the current WAD list.

        The lookup table consists of a dict with sprite names as key, in which dicts with rotations and frames
        are stored. For example, the sprite lump TROOA1E1 would create an entry for TROO, which contains a dict
        with lump data for subsprite A1 and E1, both pointing to the same lump.
        """

        sprites = {}
        for wad in self.wads:
            sprites.update(wad.get_sprite_lumps())

        # Build the lookup table by splitting sprite lump names into relevant parts.
        for name, lump in sprites.iteritems():
            sprite_name = name[:4]

            # Use current or create a new sprite dict.
            if sprite_name in self.sprites:
                sprite = self.sprites[sprite_name]
            else:
                sprite = {}
                self.sprites[sprite_name] = sprite

            # Add subsprite.
            subsprite = name[4:6]
            sprite[subsprite] = SpriteEntry(lump, False)

            # Add mirrored sprite as well.
            if len(lump.name) == 8:
                subsprite = name[6:8]
                sprite[subsprite] = SpriteEntry(lump, True)

        # Find a PLAYPAL lump to use as palette.
        playpal = self.get_lump('PLAYPAL')
        if playpal is not None:
            self.palette = graphics.Palette(playpal.get_data())

    def __len__(self):
        return len(self.wads)
