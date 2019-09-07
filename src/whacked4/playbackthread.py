import threading
import pyaudio


class PlaybackThread(threading.Thread):
    """
    A thread that uses PyAudio to play back raw sample data.
    """

    def __init__(self, pyaudio_instance, sample_rate, samples):
        threading.Thread.__init__(self)

        self.pyaudio_instance = pyaudio_instance
        self.sample_rate = sample_rate
        self.samples = samples

    def run(self):
        stream = self.pyaudio_instance.open(
            format=pyaudio.paUInt8,
            channels=1,
            rate=self.sample_rate,
            output=True,
            frames_per_buffer=1,
            start=True
        )
        stream.write(self.samples)
        stream.stop_stream()
        stream.close()
