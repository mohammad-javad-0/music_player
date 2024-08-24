import pygame
from mutagen.mp3 import MP3
from os import listdir

index = 0
music_list = listdir('music')

def main(obj):
    pygame.init()
    play_music(obj)


def show_button(obj, music_index):
    if music_index == 0:
        obj.last_music_pushButton.setHidden(True)
    elif music_index == len(music_list) - 1:
        obj.next_music_pushButton.setHidden(True)
    else:
        obj.next_music_pushButton.setHidden(False)
        obj.last_music_pushButton.setHidden(False)

def play_music(obj):
    global index, music_list
    show_button(obj, index)
    music_length = int(MP3(f"music/{music_list[index]}").info.length)
    hour = music_length // 3600
    minute = (music_length % 3600) // 60
    second = (music_length % 3600) % 60
    obj.music_name_label.setText(f"{music_list[index]} :\t{hour:02}:{minute:02}:{second:02}")
    pygame.mixer.music.load(f"music/{music_list[index]}")
    pygame.mixer.music.play()


def change_music(obj, state):
    global index, music_list
    pygame.mixer.music.stop()
    if state == "last":
        index -= 1
    else:
        index += 1

    if obj.music_pushButton.objectName() == "pause":
        obj.music_pushButton.setIcon(QtGui.QIcon("icons/pause.png"))
        obj.music_pushButton.setIconSize(QtCore.QSize(100, 50))
        obj.music_pushButton.setObjectName("play")
    play_music(obj)

def connect_play_button(obj):
    if obj.music_pushButton.objectName() == "play":
        obj.music_pushButton.setIcon(QtGui.QIcon("icons/play.png"))
        obj.music_pushButton.setIconSize(QtCore.QSize(100, 50))
        obj.music_pushButton.setObjectName("pause")
        pygame.mixer.music.pause()

    else:
        obj.music_pushButton.setIcon(QtGui.QIcon("icons/pause.png"))
        obj.music_pushButton.setIconSize(QtCore.QSize(100, 50))
        obj.music_pushButton.setObjectName("play")
        pygame.mixer.music.unpause()