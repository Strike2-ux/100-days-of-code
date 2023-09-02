from flask import Flask

app = Flask(__name__)



myReflections = {}

myReflections["78"] = {"link" : "25th of October", "Reflection" : "Was a bit of a head scratcher, but I got there in the end. Even if I was a bit lazy with the css :D"}

myReflections["79"] = {"link" : "26th October", "Reflection" : "Oh. Easy. Done. Boom"}

print(myReflections["79"]["link"])



@app.route('/<pageNumber>')
def index(pageNumber):
    global myReflections
    page=""
    f = open("template/relection.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{day}", pageNumber)
    page = page.replace("{date}", myReflections[pageNumber]["link"])
    page = page.replace("{reflection}", myReflections[pageNumber]["Reflection"])
    return page

app.run(host='0.0.0.0', port=81)
