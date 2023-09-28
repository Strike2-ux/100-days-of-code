# Sample messages.py
messages = [
    {'id': 1, 'username': 'admin', 'text': 'Welcome to the chat room!', 'profile_pic': 'admin.jpg'},
    {'id': 2, 'username': 'user1', 'text': 'Hi there!', 'profile_pic': 'user1.jpg'},
    {'id': 3, 'username': 'user2', 'text': 'Hello!', 'profile_pic': 'user2.jpg'},
]

def get_last_five_messages():
    return messages[-5:]

def add_message(username, text):
    new_message = {
        'id': len(messages) + 1,
        'username': username,
        'text': text,
        'profile_pic': users[username]['profile_pic']
    }
    messages.append(new_message)

def delete_message(message_id):
    global messages
    messages = [message for message in messages if message['id'] != message_id]
