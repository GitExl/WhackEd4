#!/usr/bin/env python
#coding=utf8

"""
Classes for Doom audio reading and playback using the PyAudio PortAudio bindings.
"""

import pyaudio
import struct
import threading


class Sound:
    """
    Doom sound data.
    """
    
    # Doom sound lump header.
    SOUND_HEADER = struct.Struct('<HHI')

    def __init__(self):
        self.format = 0
        self.sample_rate = 0
        self.sample_count = 0
        self.samples = None

    def read_from(self, data):
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
        player = PlaybackThread(self.sample_rate, self.samples)
        player.start()


class PlaybackThread(threading.Thread):
    """
    A thread that uses PyAudio to play back raw sample data.
    """
    
    def __init__(self, sample_rate, samples):
        threading.Thread.__init__(self)
        
        self.sample_rate = sample_rate
        self.samples = samples

    def run(self):
        aud = pyaudio.PyAudio()

        stream = aud.open(format=pyaudio.paUInt8, channels=1, rate=self.sample_rate, output=True)
        stream.write(self.samples)
        stream.stop_stream()
        stream.close()
        
        aud.terminate()