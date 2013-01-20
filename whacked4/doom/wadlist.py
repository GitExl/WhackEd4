from doom import image
class WADList():
    
    def __init__(self):
        self.clear()
        
        
    def clear(self):
        self.wads = []
        
        self.sprites = {}
        self.sprite_bitmap_cache = {}
        self.palette = None
    
    
    def __len__(self):
        return len(self.wads)
    
    
    def add_wad(self, wad):
        self.wads.append(wad)
        
    
    def get_lump(self, lump_name):
        for wad in reversed(self.wads):
            lump = wad.get_lump(lump_name)
            if lump is not None:
                return lump
        
        return None
    
    
    def get_sprite(self, sprite_name, frame_index=0, rotation=0):
        if not sprite_name in self.sprites:
            return None
        
        sprite = self.sprites[sprite_name]
        subsprite_string = chr(frame_index + 65) + str(rotation)
        
        if not subsprite_string in sprite:
            return None
        
        return sprite[subsprite_string]
    
    
    def get_sprite_bitmap(self, lump):
        if self.palette is None:
            return None
        
        if lump.name in self.sprite_bitmap_cache:
            return self.sprite_bitmap_cache[lump.name]
        
        bitmap = image.Image(lump.get_data(), self.palette)
        self.sprite_bitmap_cache[lump.name] = bitmap
        
        return bitmap
            
    
    def build_sprite_list(self):
        sprites = {}
        for wad in self.wads:
            wad.get_sprite_list(sprites)
        
        # Build a lookup table for sprites and rotations.
        # sprite_name_dict[rotation_dict[lump]]
        for name, lump in sprites.iteritems():
            sprite_name = name[:4]
            
            if sprite_name in self.sprites:
                sprite = self.sprites[sprite_name]
            else:
                sprite = {}
                self.sprites[sprite_name] = sprite
                
            subsprite = name[4:6]
            sprite[subsprite] = lump
            
            if len(lump.name) == 8:
                subsprite = name[6:8]
                sprite[subsprite] = lump
        
        # Find a PLAYPAL lump to use as palette.
        playpal = self.get_lump('PLAYPAL')
        if playpal is not None:
            self.palette = image.Palette(playpal.get_data())