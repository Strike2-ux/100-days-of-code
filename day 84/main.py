from flask import Flask, request, redirect


app = Flask(__name__)


# key, keys & db are a personalized set of querys own by www.replit.com

@app.route('/signup', methods=["POST"])
def createUser():
  keys = db.keys()
  form = request.form
  if form["username"] not in key:
    db[form["username"]] = {"name": form["name"], "password": form["password"]}
    return redirect("/login")
  else:
    return("/signup") 
  

@app.route("/login", methods=["POST"])
def doLogin():
    keys = db.keys()
    form = request.form
    if form["username"] not in key:
      return redirect("/login")
    else:
      if form["password"]==db[form["username"]]["password"]:
         return f"""Hello {db[form["username"]]["name"]}"""
      else:
         return redirect("/login")
      

  
@app.route("/login")
def login():
    page = ""
    f = open("login.html", "r")
    page = f.read()
    f.close()
    return page

@app.route("/signup")
def signup():
  page = ""
  f = open("signup.html", "r")
  page = f.read()
  f.close()
  return page

@app.route('/')
def index():
   page = """<p><a href="/signup">Sign up</a></p><p><a href="/login">Log in</a></p>"""
   return page

app.run(host='0.0.0.0', port=81)