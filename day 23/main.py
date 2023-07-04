def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password? ")
    if username == "Paul" and password == "Replitxs13mpr":
      print("Welcome David!")
      break
    else:
      print("That is not the correct username or password. Try again!")
      continue
    
print("REPLIT Sistema de LOGIN")
login()