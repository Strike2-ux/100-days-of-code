import requests, json, os, time,
from replit import db

while(True):
    time.sleep(1)
    os.system("Clear")
    result = requests.get("https:/icanhazdadjoke.com/", headers={"Accept":"application/json"})
    joke = result.json()

    jk = joke["joke"]
    id = joke["id"]
    print(jk)
    answer = input("\n (s)ave joke, (l)oad old jokes, (n)ew joke\n>").lower()
    if answer=="n":
        continue
    elif answer == "s":
        db[id] == jk
        print("\nSAVED\n")
        continue
    else:
        keys = db.keys()
        for key in keys:
            result = requests.get(f"https:/icanhazdadjoke.com/j/{key}", headers={"Accept":"application/json"})
            joke = result.json()
            print(joke["joke"])
            print("\n")
            time.sleep(1)


'''
import requests
import json
import os
import time
from replit import db

while True:
    time.sleep(1)
    os.system("clear")
    result = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    joke = result.json()

    jk = joke["joke"]
    joke_id = joke["id"]
    print(jk)
    answer = input("\n (s)ave joke, (l)oad old jokes, (n)ew joke\n>").lower()
    if answer == "n":
        continue
    elif answer == "s":
        db[joke_id] = jk
        print("\nSAVED\n")
        continue
    elif answer == "l":
        keys = db.keys()
        for key in keys:
            result = requests.get(f"https://icanhazdadjoke.com/j/{key}", headers={"Accept": "application/json"})
            joke = result.json()
            print(joke["joke"])
            print("\n")
            time.sleep(1)
    else:
        print("\nInvalid option. Please choose 'n' for new joke, 's' to save, or 'l' to load old jokes.\n")
'''