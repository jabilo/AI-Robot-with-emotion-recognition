import vlc
import random
import time


Instance = vlc.Instance('--no-xlib')
player = Instance.media_player_new()

def play_story():
    # a = random.randint(1,3)
    a = 1
    Media = Instance.media_new('s'+str(a)+'.mp4')
    Media.get_mrl()
    player.set_media(Media)
    # player.set_fullscreen(True)
    player.play()
    print('playing')
    while True:
        pass

def stop_story():
    player.stop()
    print("vlc player stoped .....")