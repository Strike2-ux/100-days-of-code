from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Hardcoded username and password for simplicity
USERNAME = "your_username"
PASSWORD = "your_password"

# Assume you have functions get_all_posts_from_db and add_post_to_db defined in database.py

def get_all_posts():
    posts = get_all_posts_from_db()
    return reversed(posts)

@app.route('/')
def index():
    logged_in = request.cookies.get('logged_in')
    return render_template('index.html', logged_in=logged_in, post_list=get_all_posts())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            response = redirect('/')
            response.set_cookie('logged_in', 'True')
            return response
        else:
            return "Invalid credentials. Try again."

    return render_template('login.html')

@app.route('/logout')
def logout():
    response = redirect('/')
    response.set_cookie('logged_in', 'False')
    return response

@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    add_post_to_db(title, content)
    return redirect('/')
