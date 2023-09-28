from flask import Flask, render_template, redirect, url_for, request, session
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.secret_key = 'your_secret_key'
socketio = SocketIO(app)

from users import authenticate_user, is_admin, register_user, get_user_profile
from messages import get_last_five_messages, add_message, delete_message

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if authenticate_user(username, password):
        session['username'] = username
        return redirect(url_for('chatroom'))
    else:
        return "Invalid credentials. Please try again."

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def do_register():
    username = request.form['username']
    password = request.form['password']
    register_user(username, password)
    session['username'] = username
    return redirect(url_for('chatroom'))

@app.route('/chatroom')
def chatroom():
    if 'username' not in session:
        return redirect(url_for('login'))

    messages = get_last_five_messages()
    return render_template('chatroom.html', messages=messages, current_user=session['username'], is_admin=is_admin(session['username']), user_profile=get_user_profile(session['username']))

@socketio.on('message')
def handle_message(data):
    message = data['message']
    username = session['username']
    add_message(username, message)
    emit('message', {'username': username, 'message': message, 'profile_pic': get_user_profile(username)['profile_pic']}, broadcast=True)

@app.route('/delete_message/<int:message_id>')
def delete(message_id):
    if not is_admin(session['username']):
        return "Access denied."
    delete_message(message_id)
    return redirect(url_for('chatroom'))

if __name__ == '__main__':
    socketio.run(app, debug=True)
