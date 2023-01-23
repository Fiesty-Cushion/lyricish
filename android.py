from ppadb.client import Client as AdbClient
from convert import *
import os

client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("R5CRA00V4DY")

def getTracks():    
    cwd = os.getcwd()
    tracks = device.shell("ls /sdcard/Music/SpotiFlyer/Tracks")

    listTracks = Convert(tracks)
    newList = [track.replace('_', ' ')[:-4] for track in listTracks if not track.startswith("_")]

    with open('tracks.txt', 'w') as f:
        for track in newList:
            f.write(track)
            f.write("\n")
    
    device.shell(f"adb pull /sdcard/Music/SpotiFlyer/Tracks {cwd}")

def moveLyrics():
    device.push("lyrics/Affection.lrc", "/sdcard/Music/SpotiFlyer/Tracks/Affection.lrc")
    


