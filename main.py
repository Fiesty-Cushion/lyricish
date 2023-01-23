from android import *
from tracks import *
import os
import eyed3

def trackDetails():
    directory = os.fsencode(f"{os.getcwd()}\Tracks")
    
    with open ('tracks.txt', 'w', encoding="utf-8") as f:
        for track in os.listdir(directory):
            fileName = os.fsdecode(track)
            audiofile = eyed3.load(f"Tracks/{fileName}")
            title = audiofile.tag.title
            artist = audiofile.tag.artist
            f.write(title)
            f.write(" - ")
            f.write(artist)
            f.write("\n")

trackDetails()
#getTracks()
#fetchLyrics()
#moveLyrics()







