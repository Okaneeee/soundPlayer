from threading import Thread
from wave import Wave_read, open
from pyaudio import PyAudio, Stream
from typing_extensions import Self
from Exception import FileExtensionException

class SoundPlayer:
    """
    Python class to play .wav file 
    """
    def __init__(self: Self, file_name: str):
        extension : list[str] = file_name.split(".")
        if (extension != ".wav"):
            raise FileExtensionException(extension[-1])      

        # Open the wave file
        self.file_name: str = file_name
        self.wf: Wave_read = open(file_name, 'rb')
        self.p: PyAudio = PyAudio()
        self.stream: Stream

    def play(self: Self) -> None:
        """
        Method that starts the audio stream and launches a separate thread that reads the data from the wave file
        and writes it to the stream using stream.write(). This way the method will start playing
        the sound in a non-blocking way and the main thread can continue to execute other code.
        """
        # Opening the audio stream
        self.stream: Stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )
        self.stream.start_stream()
        self.thread: Thread = Thread(target=self._play_sound)
        self.thread.start()

    def _play_sound(self: Self) -> None:
        """
        Method that reads the data from the wave file and writes it to the audio stream using a while loop
        until there's no more data. It then stops the stream.
        """
        self.data = self.wf.readframes(1024)

        while self.data:
            self.stream.write(self.data)
            self.data = self.wf.readframes(1024)
        self.stream.stop_stream()

    def close(self: Self) -> None:
        """
        Method used to close the audio stream and terminate the pyaudio object. 
        Should be called when the sound is finished playing to free up resources that were allocated.
        """
        self.stream.close()
        self.p.terminate()

if __name__ == '__main__':
    from tkinter import Tk
    w: Tk = Tk()
    
    # mp3: str = "./medias/Rollin_at_5.mp3"
    # player = SoundPlayer(mp3) # Should raise an exception

    wav: str = "./medias/Early_Riser.wav"
    player = SoundPlayer(wav) # Should work
    player.play()

    w.mainloop()

    player.close()