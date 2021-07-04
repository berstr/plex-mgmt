import requests
import json
import os
import re

import config
from modules import synology
from modules.classes import PlexSong as plex
from modules import helper

files = None
audio_files = None
video_files = None

def menu():
    __init(config.SYNOLOGY_MUSIC_INBOX)
    
    while True:
        print('')
        print("1 -> import song")
        print("2 -> list inbox raw (all entries)")
        print("e -> return to main menu")
        print('')
        user = input("=> ")
        if user == "e":
            return
        elif user == "1":
            menue_import_songs()
        elif user == "2":
            menu_list_inbox_raw()
        

def __init(foldername): # , files,audio_files, video_files ):
    global files, audio_files, video_files
    print('read files from Synology: %s  ......' % (foldername))
    files = synology.list_files(foldername)
    audio_files = synology.filter_audio_files(files)
    video_files = synology.filter_video_files(files)


def menue_import_songs():
    list_inbox()
    while True:
        song_number = input("select song number to import (e to return) -> ")
        if song_number == "e":
            return
        else:
            import_song(audio_files[int(song_number)-1])

def import_song(file):
    print('Import new song: %s' % (file))

def list_inbox():    
    i = 1
    for audio_file in audio_files:
        print('[%s] %s' % (i, audio_file.filename))
        video_file = synology.search_video_file(audio_file, video_files)
        if video_file != None:
            print('   video: %s' % (video_file.filename))
        meta = helper.parse_filename(audio_file.name)
        print('   valid filename: %s' % (meta))
        i = i + 1


def menu_list_inbox_raw():  
    files = synology.list_files(config.SYNOLOGY_MUSIC_INBOX)
    i = 1
    for file in files:
        print('[%s] %s' % (i, file.filename))
        i = i + 1
       