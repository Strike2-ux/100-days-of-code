import schedule, time, random, os, smtplib, 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

quotes = []
f = open("quotes.txt", "r")
quotes = eval(f.read())
f.close()



password = os.environ['mailPassword']
username = os.environ['mailUsername']

def sendMail():
    quote = random.choice(quotes)
    print(quote)
    server = "smtp.outlook.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg["To"] = username
    msg["From"] = username
    msg["Subject"] = "Daily Inspiration"
    msg.attach(MIMEText(quote, 'html'))

    s.send_message(msg)
    del msg



schedule.every{24}.hours.do(sendMail)

while True:
    schedule.run_pending()
    time.sleep(1)

'''
import schedule
import time
import random
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# File structure:
# - main.py
# - quotes.txt

quotes = []
with open("quotes.txt", "r") as f:
    quotes = eval(f.read())

password = os.environ["mailPassword"]
username = os.environ["mailUsername"]


def send_mail():
    quote = random.choice(quotes)
    print(quote)

    msg = MIMEMultipart()
    msg["To"] = username
    msg["From"] = username
    msg["Subject"] = "Daily Inspiration"
    msg.attach(MIMEText(quote, "html"))

    try:
        server = smtplib.SMTP("smtp.outlook.com", 587)
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")


schedule.every().day.at("00:00").do(send_mail)

while True:
    schedule.run_pending()
    time.sleep(1)

    


or


import schedule
import time
import random
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load quotes using with statement
with open("quotes.txt", "r") as f:
    quotes = eval(f.read())

# Use f-strings for string formatting
password = os.getenv('mailPassword')
username = os.getenv('mailUsername')

def send_mail():
    try:
        quote = random.choice(quotes)
        print(quote)

        server = "smtp.outlook.com"
        port = 587

        with smtplib.SMTP(host=server, port=port) as s:
            s.starttls()
            s.login(username, password)

            msg = MIMEMultipart()
            msg["To"] = username
            msg["From"] = username
            msg["Subject"] = "Daily Inspiration"
            msg.attach(MIMEText(quote, 'html'))

            s.send_message(msg)

    except Exception as e:
        print(f"An error occurred: {e}")

# Fix schedule statement
schedule.every(24).hours.do(send_mail)

while True:
    schedule.run_pending()
    time.sleep(1)


'''