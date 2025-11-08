"""
Classes for Doom audio reading and playback.
"""

import struct
from typing import Optional

from whacked4 import playbackthread


class Sound:
    """
    Doom sound data.
    """

    # Doom sound lump header.
    SOUND_HEADER = struct.Struct('<HHI')

    def __init__(self):
        self.format: int = 0
        self.sample_rate: int = 0
        self.sample_count: int = 0
        self.samples: Optional[bytes] = None

    def read_from(self, data: bytes):
        """
        Reads sound data from a lump.
        """

        header = self.SOUND_HEADER.unpack_from(data)

        self.format = header[0]
        self.sample_rate = header[1]
        self.sample_count = header[2]

        if self.format != 3:
            return

        # Slice sample data from the rest of the lump.
        self.samples = data[self.SOUND_HEADER.size:]

    def play(self):
        """
        Plays this sound.
        """

        # Start a new playback thread so that this function call does not block.
        player = playbackthread.PlaybackThread(
            self.sample_rate,
            self.samples,
        )
        player.start()
