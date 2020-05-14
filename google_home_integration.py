import requests

def read_on_google_home_mini(url,text):   
    json = {
        "broadcast": 'true',
        "user": "App",
        "command": text
    }

    requests.post(url, data = json)
