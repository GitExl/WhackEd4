#!/usr/bin/env python
#coding=utf8

from collections import OrderedDict

from whacked4.doom import sound, graphics


class SpriteFrame(object):
    """
    Describes a sprite'a animation frame and all of it's possible rotations.
    """

    def __init__(self, index):
        self.index = index
        self.rotations = {}
        self.is_mirrored = {}
        self.has_rotations = False

    def add_rotation(self, rotation, lump, is_mirrored):
        """
        Adds a new rotation to this frame. Any 0-rotations will overwrite all others.
        Also see https://github.com/id-Software/DOOM/blob/master/linuxdoom-1.10/r_things.c#L101
        """

        if rotation == '0':
            self.rotations = {'0': lump}
            self.is_mirrored = {'0': False}
            self.has_rotations = False

        else:
            self.rotations[rotation] = lump
            self.is_mirrored[rotation] = is_mirrored
            self.has_rotations = True

    def get_rotation_lump(self, rotation):
        return self.rotations.get(rotation, None), self.is_mirrored.get(rotation, False)


class SpriteEntry(object):
    """
    Defines a sprite entry and it's frames and rotations.
    """

    def __init__(self, name):
        self.name = name

        self.frames = {}

    def add_frame(self, frame_name, rotation, lump, is_mirrored):
        if frame_name not in self.frames:
            frame = SpriteFrame(frame_name)
            self.frames[frame_name] = frame
        else:
            frame = self.frames[frame_name]

        frame.add_rotation(rotation, lump, is_mirrored)

    def get_frame_lump(self, frame_name, rotation):
        frame = self.frames.get(frame_name, None)
        if frame:
            return frame.get_rotation_lump(rotation)

        return None, False


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

    def get_sprite_lump(self, sprite_name, frame_index=0, rotation=0):
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
        rotation = str(rotation)

        return sprite.get_frame_lump(frame_name, rotation)

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
        """

        sprite_lumps = OrderedDict()
        for wad in self.wads:
            sprite_lumps.update(wad.get_sprite_lumps())

        # Create a list of sprite names.
        for name in sprite_lumps.keys():
            sprite_name = name[0:4]
            self.sprites[sprite_name] = SpriteEntry(sprite_name)

        # Add sprite lumps for each sprite.
        for sprite_key, sprite_entry in self.sprites.items():

            for lump_name, lump in sprite_lumps.items():
                if lump_name[0:4] != sprite_key:
                    continue

                frame = lump_name[4]
                rotation = lump_name[5]
                sprite_entry.add_frame(frame, rotation, lump, False)

                # Mirrored sprite lump.
                if len(lump_name) == 8:
                    frame = lump_name[6]
                    rotation = lump_name[7]
                    sprite_entry.add_frame(frame, rotation, lump, True)

        # Find a PLAYPAL lump to use as palette.
        playpal = self.get_lump('PLAYPAL')
        if playpal is not None:
            self.palette = graphics.Palette(playpal.get_data())

    def __len__(self):
        return len(self.wads)
