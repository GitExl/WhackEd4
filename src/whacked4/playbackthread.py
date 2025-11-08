"""
Audio playback thread.
"""

import threading
import sounddevice


class PlaybackThread(threading.Thread):
    """
    A thread to play back raw sample data.
    """

    def __init__(self, sample_rate, samples):
        threading.Thread.__init__(self)

        self.sample_rate: int = sample_rate
        self.samples: bytes = samples
        self.current_frame: int = 0

    def run(self):
        event = threading.Event()

        def callback(outdata, frames, time, status):
            chunksize = min(len(self.samples) - self.current_frame, frames)
            outdata[:chunksize] = self.samples[self.current_frame:self.current_frame + chunksize]
            if chunksize < frames:
                raise sounddevice.CallbackStop()
            self.current_frame += chunksize

        stream = sounddevice.RawOutputStream(
            dtype='uint8',
            samplerate=self.sample_rate,
            channels=1,
            callback=callback,
            finished_callback=event.set,
        )
        with stream:
            event.wait()
