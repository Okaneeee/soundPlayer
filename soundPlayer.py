from threading import Thread
from wave import Wave_read, open
from pyaudio import PyAudio, Stream
from typing_extensions import Self
from Exception import FileExtensionException

class SoundPlayer:
    def __init__(self: Self, file_name: str):        
        # Open the wave file
        self.file_name: str = file_name
        self.wf: Wave_read = open(file_name, 'rb')
        self.p: PyAudio = PyAudio()
        self.stream: Stream

    def play(self: Self):
        # Open the audio stream
        self.stream: Stream = self.p.open(
            format=self.p.get_format_from_width(self.wf.getsampwidth()),
            channels=self.wf.getnchannels(),
            rate=self.wf.getframerate(),
            output=True
        )
        # Start the stream
        self.stream.start_stream()
        # Create a new thread to read and write the data
        # Alllow the music to be playing in a non-blocking way
        self.thread: Thread = Thread(target=self._play_sound)
        self.thread.start()

    def _play_sound(self: Self):
        self.data = self.wf.readframes(1024)
        # Write the data to the stream until there's no more data
        while self.data:
            self.stream.write(self.data)
            self.data = self.wf.readframes(1024)
        # Stop the stream
        self.stream.stop_stream()

    def close(self: Self):
        # Close the stream and terminate the pyaudio object
        self.stream.close()
        self.p.terminate()