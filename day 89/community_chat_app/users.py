# Sample users.py
users = {'admin': {'password': 'password', 'profile_pic': 'admin.jpg'}}

def authenticate_user(username, password):
    if username in users and users[username]['password'] == password:
        return True
    return False

def is_admin(username):
    return username == 'admin'

def register_user(username, password):
    users[username] = {'password': password, 'profile_pic': f'{username}.jpg'}

def get_user_profile(username):
    return users[username]
