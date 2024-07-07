"""
Custom sprite preview control.
"""

from math import floor
from typing import Optional, List

from wx import Bitmap, Brush, Point, MouseEvent, PaintEvent, MemoryDC, SizeEvent

from whacked4 import utils
import wx

from whacked4.doom.graphics import Image
from whacked4.doom.wadlist import WADList


class SpritePreview(wx.Panel):
    """
    Renders a sprite preview to a StaticBitmap control.
    """

    # The sensitivity of mouse dragging moving the sprite's rotation. Lower values are more sensitive.
    DRAG_SENSITIVITY = 20

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.NO_BORDER):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style | wx.NO_FULL_REPAINT_ON_RESIZE)

        # WAD list to use for sprite rendering.
        self.wads: Optional[WADList] = None

        # The current sprite being displayed.
        self.sprite: Optional[Image] = None
        self.sprite_name: Optional[str] = None
        self.sprite_frame: Optional[int] = None
        self.angle: int = 1
        self.offset_x: int = 0
        self.offset_y: int = 0
        self.is_clear: bool = False

        # The baseline at which to render sprites. Consider this to be the invisible floor on which sprites are placed.
        self.baseline_factor: float = 0.8

        # Scale to draw sprites at.
        self.scale: float = 1.0 * self.GetDPIScaleFactor()

        # The icon to display instead of missing sprites.
        self.missing: Bitmap = wx.Bitmap('res/icon-missing.png', wx.BITMAP_TYPE_PNG)
        self.invalid: Bitmap = wx.Bitmap('res/icon-invalid.png', wx.BITMAP_TYPE_PNG)

        # Create "floor" fill color.
        floor_colour = utils.mix_colors(self.GetBackgroundColour(), wx.Colour(0, 0, 0), 0.65)
        self.floor_brush: Brush = wx.Brush(floor_colour)
        self.floor_points: List[Point] = self.create_floor_points()

        # Paint setup.
        self.src_dc: MemoryDC = wx.MemoryDC()
        self.buffer: Optional[Bitmap] = None
        self.Bind(wx.EVT_SIZE, self.resize)
        self.Bind(wx.EVT_PAINT, self.paint)

        # Dragging setup.
        self.drag_point_start: Optional[Point] = None
        self.drag_angle_start: int = self.angle
        self.lock_angle: bool = False

        self.Bind(wx.EVT_LEFT_DOWN, self.drag_start)
        self.Bind(wx.EVT_LEFT_UP, self.drag_end)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.drag_end)
        self.Bind(wx.EVT_MOTION, self.drag_move)

        self.update_size()
        self.update_cursor()

    def drag_start(self, event: MouseEvent):
        if self.lock_angle:
            return

        self.drag_point_start = event.GetLogicalPosition(wx.WindowDC(self))
        self.drag_angle_start = self.angle
        self.update_cursor()

    def drag_end(self, event: MouseEvent):
        if self.drag_point_start is None:
            return

        self.drag_point_start = None
        self.update_cursor()

    def drag_move(self, event: MouseEvent):
        if self.drag_point_start is None:
            return

        drag_point_end = event.GetLogicalPosition(wx.WindowDC(self))
        drag_distance = drag_point_end.x - self.drag_point_start.x

        drag_angle = (self.drag_angle_start - 1) - (drag_distance / (SpritePreview.DRAG_SENSITIVITY * self.GetDPIScaleFactor()))
        drag_angle = int((drag_angle % 8) + 1)

        if self.angle != drag_angle:
            self.angle = drag_angle
            self.show_sprite(self.sprite_name, self.sprite_frame)

    def update_cursor(self):
        if self.lock_angle:
            self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
        elif self.drag_point_start is None:
            self.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        else:
            self.SetCursor(wx.Cursor(wx.CURSOR_SIZEWE))

    def set_source(self, wads: WADList):
        """
        Sets the source WAD list to use to retrieve and render the sprite from.
        """

        self.wads = wads

    def show_sprite(self, sprite_name: str, sprite_frame: int, offset_x: int = 0, offset_y: int = 0):
        """
        Shows a sprite.
        """

        self.sprite = None
        self.sprite_name = sprite_name
        self.sprite_frame = sprite_frame

        self.offset_x = offset_x
        self.offset_y = offset_y

        # Refresh sprite preview with new sprite.
        if self.wads is not None:
            self.sprite, self.lock_angle = self.get_sprite_lump(sprite_name, sprite_frame, self.angle)

        self.is_clear = False
        self.update_cursor()
        self.update_paint()

    def get_sprite_lump(self, sprite_name: str, sprite_frame: int, angle: int):
        sprite = None

        # Try to get a rotation sprite.
        sprite_lump, is_mirrored = self.wads.get_sprite_lump(sprite_name, sprite_frame, angle)
        lock_angle = False

        # Try to get a 0 rotation (front-facing) sprite.
        if sprite_lump is None:
            sprite_lump, is_mirrored = self.wads.get_sprite_lump(sprite_name, sprite_frame, 0)
            lock_angle = True

        if sprite_lump is not None:
            sprite = self.wads.get_sprite_image(sprite_lump, is_mirrored)

        return sprite, lock_angle

    def paint(self, event: PaintEvent):
        """
        Called when this control is painted.
        """

        wx.BufferedPaintDC(self, self.buffer)

    def update_paint(self):
        dc = wx.MemoryDC()
        dc.SelectObject(self.buffer)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()

        # Draw a floor polygon.
        dc.SetBrush(self.floor_brush)
        dc.SetPen(wx.TRANSPARENT_PEN)
        dc.DrawPolygon(self.floor_points, 0, 0)

        if not self.is_clear:
            self.blit_sprite(dc, self.sprite, self.offset_x, self.offset_y)

        # Delete context and copy drawing to screen.
        del dc
        self.Refresh(False)
        self.Update()

    def blit_sprite(self, dc: MemoryDC, sprite: Image, offset_x: int, offset_y: int):

        # Determine what icon or sprite to render.
        bitmap = None
        if sprite is None:
            bitmap = self.missing
        elif sprite.invalid:
            bitmap = self.invalid
        elif sprite.image is None:
            bitmap = self.missing

        size = self.GetClientSize()

        # Draw sprite.
        if bitmap is None and sprite.image is not None:
            bitmap = sprite.image
            baseline = size[1] * self.baseline_factor

            x = size[0] / 2
            y = baseline

            # Adjust sprite coordinates on whether it is to be used as a thing, or a screen graphic (like weapons).
            if sprite.left > 0 and sprite.top > 0:
                x -= (sprite.left - offset_x) * self.scale
                y -= (sprite.top - offset_y) * self.scale
            else:
                x -= (bitmap.GetWidth() / 2 - offset_x) * self.scale
                y -= (bitmap.GetHeight() - offset_y) * self.scale

        # Draw informational bitmap.
        else:
            x = size[0] / 2 - (bitmap.GetWidth() * self.scale) / 2
            y = size[1] / 2 - (bitmap.GetHeight() * self.scale) / 2

        x = int(x)
        y = int(y)

        self.src_dc.SelectObject(bitmap)
        if self.scale != 1:
            dc.StretchBlit(x, y, floor(bitmap.Width * self.scale), floor(bitmap.Height * self.scale), self.src_dc, 0, 0, bitmap.Width, bitmap.Height, wx.COPY, True)
        else:
            dc.Blit(x, y, bitmap.Width, bitmap.Height, self.src_dc, 0, 0, wx.COPY, True)

    def resize(self, event: SizeEvent):
        self.update_size()

    def update_size(self):
        size = self.GetClientSize()
        if size[0] <= 0 or size[1] <= 0:
            return

        self.buffer = wx.Bitmap(size[0], size[1])
        self.update_paint()

    def clear(self):
        """
        Clears this sprite preview.
        """

        self.is_clear = True
        self.update_paint()

    def set_baseline_factor(self, factor: float):
        """
        Sets the baseline at which to draw the sprite preview.
        """

        if factor < 0:
            factor = 0
        elif factor > 1:
            factor = 1

        self.baseline_factor = factor
        self.floor_points = self.create_floor_points()

    def set_scale(self, scale: float):
        self.scale = scale * self.GetDPIScaleFactor()
        self.floor_points = self.create_floor_points()
        self.update_paint()

    def create_floor_points(self) -> List[Point]:
        size = self.GetClientSize()
        baseline = int(size[1] * self.baseline_factor)

        return [
            wx.Point(0, baseline),
            wx.Point(size[0], baseline),
            wx.Point(size[0], size[1]),
            wx.Point(0, size[1])
        ]
