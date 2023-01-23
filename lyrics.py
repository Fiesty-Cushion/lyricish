import requests

def getLyrics(trackID):
    token = "<special_token>"
    api_url = "<secret_url>"

    response = requests.get(api_url, headers={"app-platform": "WebPlayer", "authorization": f"Bearer {token}"})
    
    return response.json()
    

