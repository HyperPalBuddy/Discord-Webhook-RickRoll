'''
Webhook RickRoll By HyperPalBuddy

'''


import time
import requests

url = 'Enter Webhook URL Here'

lyrics = ["Never gonna give you up",
            "Never gonna let you down",
            "Never gonna run around and desert you",
            'Never gonna make you cry',
            "Never gonna say goodbye",
            "Never gonna tell a lie and hurt you"]

def spammer(msg,url):
    try:
        data = requests.post(url, json={'content': msg})
        if data.status_code == 204:
            print("Sent Msg="+msg)
    except:
        print("Bad Webhook :" + url)
        time.sleep(5)
        exit()

while True:
    for i in range(6):
        spammer(lyrics[i],url)
