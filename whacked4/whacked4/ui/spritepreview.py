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

    # The sensitivity of mouse dragging moving the sprite's rotation. Lower values are more sensitive.
    DRAG_SENSITIVITY = 20
    
    
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
        self.invalid = wx.Bitmap('res/icon-invalid.png', wx.BITMAP_TYPE_PNG)
        
        # Create "floor" fill color.
        floor_colour = utils.mix_colours(self.GetBackgroundColour(), wx.Colour(0, 0, 0), 0.6)
        self.floor_brush = wx.Brush(floor_colour)
        self.create_floor_points()
        
        # Sprite setup.
        self.sprite_name = None
        self.sprite_frame = None
        self.angle = 1

        # Paint setup.
        self.Bind(wx.EVT_PAINT, self.paint)

        # Dragging setup.
        self.drag_point_start = None
        self.drag_angle_start = self.angle
        self.lock_angle = False

        self.Bind(wx.EVT_LEFT_DOWN, self.drag_start)
        self.Bind(wx.EVT_LEFT_UP, self.drag_end)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.drag_end)
        self.Bind(wx.EVT_MOTION, self.drag_move)

        self.update_cursor()
        

    def drag_start(self, event):
        if self.lock_angle == True:
            return

        self.drag_point_start = event.GetLogicalPosition(wx.WindowDC(self))
        self.drag_angle_start = self.angle
        self.update_cursor()


    def drag_end(self, event):
        if self.drag_point_start is None:
            return

        self.drag_point_start = None
        self.update_cursor()


    def drag_move(self, event):
        if self.drag_point_start is None:
            return

        drag_point_end = event.GetLogicalPosition(wx.WindowDC(self))
        drag_distance = drag_point_end.x - self.drag_point_start.x
        
        drag_angle = (self.drag_angle_start - 1) - (drag_distance / SpritePreview.DRAG_SENSITIVITY)
        drag_angle = (drag_angle % 8) + 1
        
        if self.angle != drag_angle:
            self.angle = drag_angle
            self.show_sprite(self.sprite_name, self.sprite_frame)


    def update_cursor(self):
        if self.lock_angle == True:
            self.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        elif self.drag_point_start is None:
            self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        else:
            self.SetCursor(wx.StockCursor(wx.CURSOR_SIZEWE))
        
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
        self.sprite_name = sprite_name
        self.sprite_frame = sprite_frame
        
        # Refresh sprite preview with new sprite.
        if self.wads is not None:

            # Try to get a rotation sprite.
            sprite_data = self.wads.get_sprite(sprite_name, sprite_frame, self.angle)
            self.lock_angle = False
            
            # Try to get a 0 rotation (front-facing) sprite.
            if sprite_data is None:
                sprite_data = self.wads.get_sprite(sprite_name, sprite_frame, 0)
                self.lock_angle = True

            if sprite_data is not None:
                self.sprite = self.wads.get_sprite_image(sprite_data[0], sprite_data[1])
        
        self.update_cursor()
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

        # Determine what icon or sprite to render.
        bitmap = None
        if self.sprite is None:
            bitmap = self.missing
        elif self.sprite.invalid == True:
            bitmap = self.invalid
        elif self.sprite.image is None:
            bitmap = self.missing
            
        size = self.GetClientSizeTuple()

        # Draw sprite.
        if bitmap is None:
            bitmap = self.sprite.image
            baseline = size[1] * self.baseline_factor
            
            x = size[0] / 2 - self.sprite.width / 2
            y = baseline - self.sprite.height
            x + self.sprite.left
            y + self.sprite.top

            dc.DrawBitmap(bitmap, x, y, True)
        
        # Draw informational bitmap.
        else:
            x = size[0] / 2 - bitmap.GetWidth() / 2
            y = size[1] / 2 - bitmap.GetHeight() / 2
            dc.DrawBitmap(bitmap, x, y, True)

            
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
