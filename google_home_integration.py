import requests

# Node.js server need to be working. In terminal with admin privelages - npm run start. (pm2 kill to stop server)
url = 'http://192.168.0.111:3000/assistant'

def read_on_google_home_mini(text):   
    json = {
        "broadcast": 'true',
        "user": "App",
        "command": text
    }

    requests.post(url, data = json)
