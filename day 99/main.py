import requests, schedule, time, os, smtplib
from bs4 import BeautifulSoup
from replit import db
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

interests = ["teams", "education"]

keys = db.keys()
for key in keys:
    del db[key]

def email(text, link):
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
    msg["Subject"] = "New Community Event"
    text = f"""< a href="{link}">{text}</a>"""
        
    msg.attach(MIMEText(text, 'html'))
    s.send_message(msg)
    del msg
    
def getHub():

    url = "https://replit.com/community-hub"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    #div
    #css-36v8q4

    myLinks = soup.find_all("div", {"class": "css-36v8q4"})


    counter = 0
    keys = db.keys()
    for link in myLinks:
        if "Community Spaces" in link.text:
            break
        if counter !=0:
            print(link.text)
            thisLink = link.find("a")["href"]
            print(thisLink)
            words = link.text.split()
            amInterested = False
            for word in words:
                if word.lower() in interests:
                 amInterested = True
            if amInterested and link.text not in keys:
                db[link.text] = thisLink
                # todo add the email bit
                email(link.text, thisLink)

        counter += 1

getHub()

schedule.every(3).hours.do(getHub)

while True:
    schedule.run_pending()
    time.sleep(1)
'''
import os
import requests
import schedule
import time
import smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuration
interests = ["teams", "education"]

def send_email(text, link):
    try:
        password = os.environ['mailPassword']
        username = os.environ['mailUsername']
        host = "smtp.outlook.com"
        port = 587
        with smtplib.SMTP(host=host, port=port) as s:
            s.starttls()
            s.login(username, password)

            msg = MIMEMultipart()
            msg["To"] = username
            msg["From"] = username
            msg["Subject"] = "New Community Event"

            text = f'<a href="{link}">{text}</a>'

            msg.attach(MIMEText(text, 'html'))
            s.send_message(msg)

        print(f"Email sent: {text}")
    except Exception as e:
        print(f"Error sending email: {e}")

def get_hub():
    try:
        url = "https://replit.com/community-hub"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors (4xx and 5xx)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        my_links = soup.find_all("div", {"class": "css-36v8q4"})

        for counter, link in enumerate(my_links):
            if "Community Spaces" in link.text:
                break

            if counter != 0:
                print(link.text)
                this_link = link.find("a")["href"]
                print(this_link)
                words = link.text.split()
                am_interested = any(word.lower() in interests for word in words)
                if am_interested and link.text not in db.keys():
                    db[link.text] = this_link
                    send_email(link.text, this_link)
    except Exception as e:
        print(f"Error getting community hub: {e}")

# Schedule to run get_hub every 3 hours
schedule.every(3).hours.do(get_hub)

while True:
    schedule.run_pending()
    time.sleep(1)

'''