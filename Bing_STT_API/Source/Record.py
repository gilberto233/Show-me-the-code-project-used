"""
Script based on the example of the pyaudio project. Check the following link
to get further information: http://people.csail.mit.edu/hubert/pyaudio/
These will record a five second voice sample used to be analysted.
"""
import pyaudio, wave

class Recorder():

    def __init__(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 5
        self.WAVE_OUTPUT_FILENAME = "output.wav"

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def get_file_name(self):
        return self.WAVE_OUTPUT_FILENAME

if __name__ == '__main__':
    instance = Recorder()
