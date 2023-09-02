from flask import Flask, request, render_template

app = Flask(__name__)

# Define valid username-password pairs
valid_credentials = {
    "David": "123456",
    "Jean Luc Picard": "password",
    "Yul Brynner": "letmein"
}

@app.route("/process", methods=["POST"])
def process():
    page = ""
    form = request.form

    username = form.get("username")
    password = form.get("password")

    if username in valid_credentials and password == valid_credentials[username]:
        page += f"You're alright, {username}!"
    else:
        page += f"Invalid credentials for {username}. You've picked wrong!"

    return page

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
