# Official tq148 bio changer python script.
# do not steal my script or else you will suffer the consequences.
import requests

desc = ['I wonder how long it will take you to realize that my bio changes every second', 'see? what did I tell you?', "I'm legit, gang", "i'm cool lol", "i'm probably the first user to do this."]

cookie = "YOUR_ROBLOSECURITY_TOKEN"
auth_response = requests.post("https://auth.roblox.com/v1/logout", headers = {"cookie": f".ROBLOSECURITY={cookie}"})

if auth_response.status_code == 403:
    if "x-csrf-token" in auth_response.headers:
        token = auth_response.headers["x-csrf-token"]

headers = {
    "cookie": f".ROBLOSECURITY={cookie}",
    "x-csrf-token": token
}

import time, os
while True:
    for i in desc:
        message_response = requests.post("https://accountinformation.roblox.com/v1/description", headers = headers, data = {"description": i})
        print(message_response.status_code)   
        if message_response.status_code == 429:
            time.sleep(60)
        if message_response.status_code ==403:
            os.system('python main.py')
        time.sleep(2)
