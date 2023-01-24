#from android import *
from lyrics import *
from spotify import *
import os
import eyed3

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


with open('tracks.txt') as tracks:
    for track in tracks:
        trackID = getTrackId(track)
        lyrics = getLyrics(trackID)
        if (lyrics == None):
            continue
        file_name = getFileName(track)
        writeLyrics(lyrics, file_name)


#getTracks()      //to load device tracks into Tracks directory
#moveLyrics()     //send .lrc file back to device







