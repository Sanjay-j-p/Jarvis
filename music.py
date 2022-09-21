import os
import random
import time
import vlc
from mutagen.mp3 import MP3
music_folder = 'G:\\song\\'
music = ['3']
random_music = music_folder + random.choice(music) + '.mp3'
audio = MP3(random_music)
a=audio.info.length
player = vlc.MediaPlayer(random_music)
player.play()
time.sleep(a)
player.stop()
