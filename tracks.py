import datetime
from lyrics import *

def fetchLyrics():
    track = getLyrics(trackID="0e7ipj03S05BNilyu5bRzt")
    i = 0

    with open('lyrics/Affection.lrc', 'w', encoding="utf-8") as f:
        for x in track["lyrics"]["lines"]:
            #get lyrics from source
            lyrics = track["lyrics"]["lines"][i]["words"]
            startTime = track["lyrics"]["lines"][i]["startTimeMs"]

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



