import requests
import os

token = os.getenv("ACCESS_TOKEN")

def getsToken():
    api_url = "_____________________________________"

    response = requests.get(api_url)
    data = response.json()
    return data.accessToken

def getLyrics(trackID):
    api_url = f"____________________________________"

    response = requests.get(api_url, headers={"app-platform": "WebPlayer", "authorization": f"Bearer {token}"})
    if response.status_code == 200:
        return response.json()
    
def getTrackId(track_name):
    query = track_name.replace(" ", "%20")
    api_url = f"https://api.spotify.com/v1/search?type=track&q={query}&limit=1&market=us"

    response = requests.get(api_url, headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"})
    data = response.json()

    trackID = data["tracks"]["items"][0]["id"]
    return trackID

