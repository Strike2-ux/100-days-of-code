import os, time, random
from replit import db #db from the replit platform hashing excercise

def createUser():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username in keys:
    print("ERROR: Username exists")
    return

  salt = random.randint(1000, 9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  
  db[username] = {"password": newPassword, "salt": salt}

  print("User added")

def login():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username not in keys:
    print("ERROR: Username does not exists")
    return

  salt = db[username]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)

  if db[username]["password"]==newPassword:
    print("Logged in")
  else:
    print("Username or password incorrect")


while True:
  menu = input("1: New User\n2: Login\n> ")
  if menu == "1":
    createUser()
  elif menu == "2":
    login()
  else:
    keys = db.keys()
    for key in keys:
      print(db[key])

'''
import os
import time
import random
import hashlib
from replit import db

def create_user():
    time.sleep(1)
    os.system("clear")
    username = input("Username: ")
    password = input("Password: ")
    keys = db.keys()
    if username in keys:
        print("ERROR: Username already exists")
        return

    salt = random.randint(1000, 9999)
    hashed_password = hash_password(password, salt)

    db[username] = {"password": hashed_password, "salt": salt}

    print("User added")

def login():
    time.sleep(1)
    os.system("clear")
    username = input("Username: ")
    password = input("Password: ")
    keys = db.keys()
    if username not in keys:
        print("ERROR: Username does not exist")
        return

    stored_salt = db[username]["salt"]
    stored_password = db[username]["password"]

    if validate_password(password, stored_password, stored_salt):
        print("Logged in")
    else:
        print("Username or password incorrect")

def hash_password(password, salt):
    # Hash the password using a secure hash function (SHA-256)
    hashed_password = hashlib.sha256(f"{password}{salt}".encode()).hexdigest()
    return hashed_password

def validate_password(input_password, stored_password, salt):
    # Validate the password by hashing the input password and comparing it with the stored password
    hashed_input_password = hash_password(input_password, salt)
    return hashed_input_password == stored_password

while True:
    menu = input("1: New User\n2: Login\n> ")
    if menu == "1":
        create_user()
    elif menu == "2":
        login()
    else:
        keys = db.keys()
        for key in keys:
            print(db[key])
'''

'''
import os, time, random
from replit import db

def createUser():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username in keys:
    print("ERROR: Username exists")
    return

  salt = random.randint(1000, 9999)
  hashed_password = hash(f"{password}{salt}")

  db[username] = {"password": hashed_password, "salt": salt}

  print("User added")

def login():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username not in keys:
    print("ERROR: Username does not exists")
    return

  salt = db[username]["salt"]
  hashed_password = hash(f"{password}{salt}")

  if db[username]["password"] == hashed_password:
    print("Logged in")
  else:
    print("Username or password incorrect")


while True:
  menu = input("1: New User\n2: Login\n3: Show Users\n> ")
  if menu == "1":
    createUser()
  elif menu == "2":
    login()
  elif menu == "3":
    keys = db.keys()
    for key in keys:
      print(key, db[key])
  else:
    print("Invalid option")

'''