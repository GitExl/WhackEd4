#!/usr/bin/env python
#coding=utf8

from whacked4.doom import sound, graphics


class WADList:
    """
    Maintains a list of WAD files that can be queried for specific lump data.
    """
    
    def __init__(self):
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
        if lump == None:
            return
        
        sound_data = sound.Sound()
        sound_data.read_from(lump.get_data())
        self.sound_cache[lump_name] = sound_data
        
        return sound_data
    
    
    def get_sprite(self, sprite_name, frame_index=0, rotation=0):
        """
        Returns a sprite lump of a sprite in this WAD list.
        
        @param sprite_name: the 4 character name of the sprite to return.
        @param frame_index: the index of the sprite frame to return.
        @param rotation: the rotation of the sprite to return.
        
        @return: a lump of the requested sprite.
        """ 
        
        if not sprite_name in self.sprites:
            return None
        
        sprite = self.sprites[sprite_name]
        subsprite_string = chr(frame_index + 65) + str(rotation)
        
        if not subsprite_string in sprite:
            return None
        
        return sprite[subsprite_string]
    
    
    def get_sprite_image(self, lump):
        """
        Returns an image object from a sprite lump.
        
        Previously requested sprites are cached so that they will not have to be rendered again. A palette has to be
        loaded for this function to work. 
        """
        
        if self.palette is None:
            return None
        
        if lump.name in self.sprite_image_cache:
            return self.sprite_image_cache[lump.name]
        
        image = graphics.Image(lump.get_data(), self.palette)
        
        # Add the loaded image to the cache.
        self.sprite_image_cache[lump.name] = image
        
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
            wad.get_sprite_list(sprites)
        
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
            sprite[subsprite] = lump
            
            # Add mirrored sprite as well.
            if len(lump.name) == 8:
                subsprite = name[6:8]
                sprite[subsprite] = lump
        
        # Find a PLAYPAL lump to use as palette.
        playpal = self.get_lump('PLAYPAL')
        if playpal is not None:
            self.palette = graphics.Palette(playpal.get_data())
            
    
    def __len__(self):
        return len(self.wads)