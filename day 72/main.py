from replit import db
import datetime, os, time, random

def addEntry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry

def viewEntry():
  keys = db.prefix("2")
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if(opt.lower()[0]=="e"):
      break



keys = db.keys()
if len(keys)<1:
  print("First Run > Create account")
  username = input("Username > ")
  password = input("Password > ")
  salt = random.randint(0,9999999)
  newPassword = hash(f"{password}{salt}")
  db[username] = {"password": newPassword, "salt": salt}
else:
  print("Log in")
  username = input("Username > ")
  password = input("Password > ")
  if username not in keys:
    print("Username or password incorrect")
    exit()
  salt = db[username]["salt"]
  newPassword = hash(f"{password}{salt}")
  if db[username]["password"]!=newPassword:
    print("Username or password incorrect")
    exit()
while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()
'''
from replit import db
import datetime
import os
import time
import random
import hashlib

def add_entry():
    time.sleep(1)
    os.system("clear")
    timestamp = datetime.datetime.now()
    print(f"Diary entry for {timestamp}")
    print()
    entry = input("> ")
    db[timestamp] = entry

def view_entries():
    keys = db.prefix("2")
    for key in keys:
        time.sleep(1)
        os.system("clear")
        print(f"{key}\n{db[key]}")
        print()
        opt = input("Next or exit? > ")
        if opt.lower().startswith("e"):
            break

def initialize_user():
    username = input("Username > ")
    password = input("Password > ")
    salt = random.randint(0, 9999999)
    new_password = hash_password(f"{password}{salt}")
    db[username] = {"password": new_password, "salt": salt}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    keys = db.keys()

    if len(keys) < 1:
        print("First Run > Create account")
        initialize_user()
    else:
        print("Log in")
        username = input("Username > ")
        password = input("Password > ")

        if username not in keys or db[username]["password"] != hash_password(f"{password}{db[username]['salt']}"):
            print("Username or password incorrect")
            exit()

    while True:
        os.system("clear")
        menu = input("1: Add\n2: View\n> ")
        if menu == "1":
            add_entry()
        else:
            view_entries()

if __name__ == "__main__":
    main()

'''
'''
import os, time, random
from replit import db
import datetime

def add_entry(timestamp):
  entry = input("> ")
  db[timestamp] = entry

def view_entries(prefix):
  keys = db.keys()
  for key in keys:
    if key.startswith(prefix):
      print(f"{key}\n{db[key]}")

def main():
  if not db:
    initialize_user()

  while True:
    menu = input("1: Add\n2: View\n> ")
    if menu == "1":
      timestamp = datetime.datetime.now()
      add_entry(timestamp)
    elif menu == "2":
      prefix = input("Enter prefix: ")
      view_entries(prefix)
    else:
      print("Invalid option")

def initialize_user():
  username = input("Username > ")
  password = input("Password > ")
  salt = random.randint(0, 9999999)
  new_password = hash(f"{password}{salt}")
  db[username] = {"password": new_password, "salt": salt}

def hash(password):
  return hashlib.sha256(password.encode()).hexdigest() 

if __name__ == "__main__":
    main()

'''

#rembember the sha