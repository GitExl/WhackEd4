#!/usr/bin/env python
#coding=utf8

"""
Contains classes to read Doom style patch graphics, and Doom PLAYPAL lump palette data.
"""

import struct
import wx


class Palette():
    """
    A 256 color RGB palette.
    """
    
    def __init__(self, data):
        self.colors = []
        
        data = bytearray(data)
        
        offset = 0
        while offset < 768:
            entry = [data[offset], data[offset + 1], data[offset + 2], 255]
            self.colors.append(entry)
            offset += 3


class Image():
    """
    A Doom style patch.
    """
    
    S_HEADER = struct.Struct('<HHhh')
    
    
    def __init__(self, data, palette):
        # Read header.
        width, height, top, left = self.S_HEADER.unpack_from(data)
        
        # Initialize an empty bitmap.
        image_data = bytearray([0, 0, 0, 0] * width * height)
        
        # Read column offsets.
        offset_struct = struct.Struct('<' + ('I' * width))
        offsets = offset_struct.unpack_from(data[8:8 + (width * 4)])
        
        # Read columns.
        data = bytearray(data)
        column_index = 0
        column_top = 0
        prev_delta = 0
        while column_index < width:
            offset = offsets[column_index]
            
            prev_delta = 0
            while True:
                column_top = data[offset]
                
                # Column end.
                if column_top == 255:
                    break
                
                # Tall columns are extended.
                if column_top <= prev_delta:
                    column_top += prev_delta
                prev_delta = column_top
                
                pixel_count = data[offset + 1]
                offset += 3
                
                pixel_index = 0
                while pixel_index < pixel_count:
                    pixel = data[offset + pixel_index]
                    dest = ((pixel_index + column_top) * width + column_index) * 4
                    
                    # Plot pixel from palette.
                    image_data[dest] = palette.colors[pixel][0]
                    image_data[dest + 1] = palette.colors[pixel][1]
                    image_data[dest + 2] = palette.colors[pixel][2]
                    image_data[dest + 3] = 255
                    
                    pixel_index += 1
                
                offset += pixel_count + 1
                
            column_index += 1
        
        self.width = width
        self.height = height
        self.top = top
        self.left = left
        
        # Create usable bitmap.
        self.image = wx.BitmapFromBufferRGBA(width, height, image_data)