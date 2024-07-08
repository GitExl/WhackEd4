"""
Contains classes to read Doom style patch graphics, and Doom PLAYPAL
lump palette data.
"""

import struct
from typing import Tuple, List, Optional

import wx
from wx import Bitmap


Color = Tuple[int, int, int, int]


class Palette:
    """
    A 256 color RGB palette.
    """

    def __init__(self, data: bytes):
        self.colors: List[Color] = []

        if len(data) < 768:
            raise RuntimeError('Not enough data for a 256 RGB color palette.')

        data = bytearray(data)

        offset = 0
        while offset < 768:
            entry = (data[offset], data[offset + 1], data[offset + 2], 255)
            self.colors.append(entry)
            offset += 3


class Image:
    """
    A Doom style patch.
    """

    S_HEADER = struct.Struct('<HHhh')

    def __init__(self, width, height, top, left, image):
        self.width: int = width
        self.height: int = height
        self.top: int = top
        self.left: int = left
        self.image: Optional[Bitmap] = image
        self.invalid: bool = False

    @staticmethod
    def from_doom_patch(data: bytes, palette: Palette, mirror=False):
        """
        Creates a new Image from Doom patch data.

        :param data: Doom patch data.
        :param palette: Doom palette.
        :param mirror: Should be created as a mirrored version?
        """
        width, height, left, top = Image.S_HEADER.unpack_from(data)

        # Attempt to detect invalid data.
        if width > 2048 or height > 2048 or top > 2048 or left > 2048:
            return Image.create_invalid()
        if width <= 0 or height <= 0:
            return Image.create_invalid()

        # Initialize data for an empty bitmap.
        image_data = bytearray((0, 0, 0, 0) * width * height)

        # Read column offsets.
        offset_struct = struct.Struct('<' + ('I' * width))
        offsets = offset_struct.unpack_from(data[8:8 + (width * 4)])

        # Read columns.
        data = bytearray(data)
        column_index = 0
        while column_index < width:
            offset = offsets[column_index]

            # Attempt to detect invalid data.
            if offset < 0 or offset > len(data):
                return Image.create_invalid()

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
                    if mirror:
                        dest = (
                           (pixel_index + column_top) * width + ((width - 1) - column_index)
                        ) * 4
                    else:
                        dest = (
                           (pixel_index + column_top) * width + column_index
                        ) * 4

                    # Plot pixel from palette.
                    image_data[dest:dest+4] = palette.colors[pixel]

                    pixel_index += 1

                offset += pixel_count + 1

            column_index += 1

        bitmap = wx.Bitmap.FromBufferRGBA(width, height, image_data)
        return Image(width, height, top, left, bitmap)

    @staticmethod
    def create_empty():
        """
        Creates a new empty Image.
        """

        return Image(0, 0, 0, 0, None)

    @staticmethod
    def create_invalid():
        """
        Creates a new "invalid" image.
        """

        image = Image.create_empty()
        image.invalid = True
        return image
