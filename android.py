from ppadb.client import Client as AdbClient
import os

client = AdbClient(host="127.0.0.1", port=5037)
#device id can be obtained using adb platform tools
device = client.device("<DEVICE_ID>")

def Convert(string):
    li = list(string.split("\n"))
    return li

#pulls track files from device
def getTracks():    
    device.shell(f"adb pull /sdcard/<PATH_TO_TRACK_FILES> {os.getcwd()}")

def moveLyrics():
    device.push("lyrics/", "/sdcard/<PATH_TO_TRACK_FILES>")
    


