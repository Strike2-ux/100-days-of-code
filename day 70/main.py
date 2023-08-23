import os

while True:
  username = input("Username: ")
  password = input("Password: ")
  if username == os.environ['adminUsername'] and password == os.environ['adminPassword']:
    print("Welcome Admin")
    break
  elif username ==  os.environ['username'] and password == os.environ['password']:
    print("Welcome Normy")
    break
  else:
    print("Try again")
    '''
    import os

def authenticate_user(username, password):
    if username == os.environ.get('adminUsername') and password == os.environ.get('adminPassword'):
        return "Welcome Admin"
    elif username == os.environ.get('username') and password == os.environ.get('password'):
        return "Welcome Normy"
    else:
        return "Try again"

while True:
    username = input("Username: ")
    password = input("Password: ")
    
    result = authenticate_user(username, password)
    print(result)
    
    if result.startswith("Welcome"):
        break
    '''