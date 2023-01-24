import datetime
from spotify import *


def getFileName(file_name):
    char_replace = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '[', ']', ' ', '.', "'", ',']
    newFileName = file_name.split(" - ", 1)[0]
    for char in char_replace:
        newFileName = newFileName.replace(char, "_")
    return newFileName

def writeLyrics(trackInfo, file_name):
    i = 0

    with open(f'lyrics/{file_name}.lrc', 'w', encoding="utf-8") as f:
        for x in trackInfo["lyrics"]["lines"]:
            #get lyrics from source
            lyrics = trackInfo["lyrics"]["lines"][i]["words"]
            startTime = trackInfo["lyrics"]["lines"][i]["startTimeMs"]

            #parse the time-stamp
            timeStamp = str(datetime.timedelta(seconds=int(startTime)/1000))
            listTime = list(timeStamp)
            del listTime[0:2]
            del listTime[8:11]
            newTimeStamp = "".join(listTime)

            #write to .lrc file
            f.write("[")
            f.write(newTimeStamp)
            f.write("]")
            f.write(lyrics)
            f.write("\n")
            i+=1



