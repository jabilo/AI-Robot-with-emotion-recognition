import vlc
import random
import time


Instance = vlc.Instance('--no-xlib')
player = Instance.media_player_new()

def play_rhyme():
    a = random.randint(1,3)
    Media = Instance.media_new('r'+str(a)+'.mp4')
    Media.get_mrl()
    player.set_media(Media)
    
    player.play()
    print('playing')
    while True:
        pass

def stop_rhyme():
    player.stop()
    print("vlc player stoped .....")

