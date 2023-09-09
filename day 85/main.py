from flask import Flask, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to your own secret key

# db is a personalized set of queries owned by www.replit.com
db = {}

@app.route('/signup', methods=["POST"])
def createUser():
    if 'username' not in session:  # Check if user is logged in
        return redirect('/login')

    form = request.form
    if form["username"] not in db:
        db[form["username"]] = {"name": form["name"], "password": form["password"]}
        return redirect("/login")
    else:
        return redirect("/signup")

@app.route("/login", methods=["POST"])
def doLogin():
    form = request.form
    if form["username"] in db and form["password"] == db[form["username"]]["password"]:
        session['username'] = form["username"]  # Set session data
        return f"""Hello {db[form["username"]]["name"]} <a href='/logout'>Logout</a>"""
    else:
        return redirect("/login")

@app.route("/login")
def login():
    if 'username' in session:  # Check if user is logged in
        return f"""You are already logged in as {session['username']} <a href='/logout'>Logout</a>"""
    page = ""
    with open("login.html", "r") as f:
        page = f.read()
    return page

@app.route("/signup")
def signup():
    if 'username' in session:  # Check if user is logged in
        return f"""You are already logged in as {session['username']} <a href='/logout'>Logout</a>"""
    page = ""
    with open("signup.html", "r") as f:
        page = f.read()
    return page

@app.route('/')
def index():
    if 'username' in session:  # Check if user is logged in
        return f"""You are already logged in as {session['username']} <a href='/logout'>Logout</a>"""
    page = """<p><a href="/signup">Sign up</a></p><p><a href="/login">Log in</a></p>"""
    return page

@app.route('/logout')
def logout():
    session.pop('username', None)  # Clear session data
    return redirect('/login')

app.run(host='0.0.0.0', port=81)
