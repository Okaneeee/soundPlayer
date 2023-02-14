# **soundPlayer**
Custom module to play **.wav** file in python

#

## ✍️ Author:
- Discord: Okane 🎴#1273
- Twitter: [@Okaneeeeeeeee_e](https://twitter.com/Okaneeeeeeeee_e)
- Github: [Okaneeee](https://github.com/Okaneeee)
- Project link: [soundPlayer](https://github.com/Okaneeee/soundPlayer)

#

## 📋 Table of contents:
1. [Modules/Libraries](#modlib)
2. [Developed](#dev)
3. [How to use](#use)
4. [Copyrights](#cpr)

#

## 📚 Modules/Libraries: <a name="modlib"></a>
- `threading` for multi-threading
- `wave` for parsing & opening WAVE file
- `pyaudio` for PortAudio supports & audio streams

#

## 👨‍💻 Developed: <a name="dev"></a>
- `soundPlayer.py` Main class to play **.wav** file 
- `FileExtensionException` Subclass in soundPlayer to handle extension errors

#

## 🌠 How to use: <a name="use"></a>
Download `requirements.txt`
Install requirements: ```pip install -r requirements.txt```

Download the file `soundPlayer.py` and put it in the directory where you want to use it 
```python
from soundPlayer import SoundPlayer

sound = 'path_to_wav_file'
player = SoundPlayer(sound)

# Play a sound:
player.play()

# Stop the sound being played
player.close()
```

#

## ©️ Copyrights: <a name="cpr"></a>
All the musics used for testing were done by Kevin MacLeod and are under the [Creative Commons licenses](https://creativecommons.org/licenses/by/3.0/).

Check [LICENSE.md](https://github.com/Okaneeee/soundPlayer/blob/main/LICENSE.md)
