from flask import Flask, request, render_template

app = Flask(__name__)

# Define valid username-password pairs
valid_credentials = {
    "David": "123456",
    "Jean Luc Picard": "password",
    "Yul Brynner": "letmein"
}

@app.route("/robot", methods=["POST"])
def robot():
    form = request.form
    if form["metal"]=="Yes":
        return "You're a robot!"
    elif "error" in form["infinity"].lower():
        return "You're a robot!"
    elif form["food"] == "synthectic oil":
        return "You're a robot!"
    else:
        return "Hi there fellow human"


@app.route('/')
def index():
    page = ""
    f = open("form.html", "r")
    page = f.read()
    f.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)