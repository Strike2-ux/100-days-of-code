from replit import db
import time, requests, schedule, os, smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def addToDB():
    link = input("Link: ")
    price = float((input("Price: ")))
    db[time.time()] = {"link": link, "price" : None, "level" : price}



def emailMe(text, price, link)
    password = os.environ['mailPassword']
    username = os.enviroment['mailUsername']
    host = "smtp.outlook.com"
    port = 587
    s = smtplib.SMTP(host=host, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg["To"] = username
    msg["From"] = username
    msg["Subject"] = "Product is Cheaper!"
    text = f"""<p><a href='{link}'>This item</a> is now {price} wich is below your purchase level of {level}</p>"""
    msg.attach(MIMEText(text, 'html'))
    s.send_message(msg)
    del msg

def update():
    keys = db.keys()
    for key in keys:
        url = db[key]["link"]
        price = db[key]["price"]
        level = db[key]["level"]
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

    myPrice = soup.find_all("span", { "class": "price"})

    thisPrice = float(myPrice[0].text[1:].replace(",",""))

    if thisPrice != price:
        db[key]["price"] = thisPrice
        if thisPrice <= level:
            print("Cheaper")
            emailMe(level, price, url)

schedule.every(1).day.do(update)

while True:
    schedule.run_pending()
    time.sleep(1)


'''

'''