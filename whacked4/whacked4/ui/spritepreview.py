#!/usr/bin/env python
#coding=utf8

from whacked4 import utils
import wx


class SpritePreview(wx.Panel):
    """
    Renders a sprite preview to a StaticBitmap control.
    """
    
    # Indicates that no sprite should be drawn at all.
    CLEAR = 0xDEADBEEF
    
    
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.NO_BORDER):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=wx.STATIC_BORDER)
        
        # WAD list to use for sprite rendering.
        self.wads = None
        
        # The current sprite being displayed.
        self.sprite = None
        
        # The baseline at which to render sprites. Consider this to be the invisible floor on which sprites are placed.
        self.baseline_factor = 0.8
        
        # The icon to display instead of missing sprites.
        self.missing = wx.Bitmap('res/icon-missing.png', wx.BITMAP_TYPE_PNG)
        
        # Create "floor" fill color.
        floor_colour = utils.mix_colours(self.GetBackgroundColour(), wx.Colour(0, 0, 0), 0.6)
        self.floor_brush = wx.Brush(floor_colour)
        self.create_floor_points()
        
        self.Bind(wx.EVT_PAINT, self.paint)
        
        
    def set_source(self, wads):
        """
        Sets the source WAD list to use to retrieve and render the sprite from.
        """
        
        self.wads = wads
        
        
    def show_sprite(self, sprite_name, sprite_frame):
        """
        Shows a sprite.
        """
        
        self.sprite = None
        
        # Refresh sprite preview with new sprite.
        if self.wads is not None:
            # Try to get a no-rotation sprite.
            sprite_lump = self.wads.get_sprite(sprite_name, sprite_frame, 0)
            
            # Try to get a 0 rotation (front-facing) sprite.
            if sprite_lump is None:
                sprite_lump = self.wads.get_sprite(sprite_name, sprite_frame, 1)

            if sprite_lump is not None:
                self.sprite = self.wads.get_sprite_image(sprite_lump)
        
        self.Refresh()
            
    
    def paint(self, event):
        """
        Called when this control is painted.
        """
        
        dc = wx.BufferedPaintDC(self)
        dc.Clear()
        
        # Draw a floor polygon.
        dc.SetBrush(self.floor_brush)
        dc.SetPen(wx.TRANSPARENT_PEN)
        dc.DrawPolygon(self.floor_points, 0, 0)
        
        if self.sprite == self.CLEAR:
            return
        
        size = self.GetClientSizeTuple()
        if self.sprite is not None:
            baseline = size[1] * self.baseline_factor
            
            x = size[0] / 2 - self.sprite.width / 2
            y = baseline - self.sprite.height
            x + self.sprite.left
            y + self.sprite.top
            dc.DrawBitmap(self.sprite.image, x, y, True)
        
        # Display the missing image bitmap if no sprite is set.
        else:
            x = size[0] / 2 - self.missing.GetWidth() / 2
            y = size[1] / 2 - self.missing.GetHeight() / 2
            dc.DrawBitmap(self.missing, x, y, True)
            
            
    def clear(self):
        """
        Clears this sprite preview.
        """
        
        self.sprite = self.CLEAR
        self.Refresh()
            
            
    def set_baseline_factor(self, factor):
        """
        Sets the baseline at which to draw the sprite preview.
        """
        
        if factor < 0:
            factor = 0
        elif factor > 1:
            factor = 1
            
        self.baseline_factor = factor
        self.create_floor_points()
        
        
    def create_floor_points(self):
        size = self.GetClientSizeTuple()
        baseline = size[1] * self.baseline_factor
        
        self.floor_points = [
            wx.Point(0, baseline),
            wx.Point(size[0], baseline),
            wx.Point(size[0], size[1]),
            wx.Point(0, size[1])
        ]
