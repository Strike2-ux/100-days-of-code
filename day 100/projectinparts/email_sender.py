import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

def email_me(text, price, link, level):
    password = config.mailPassword
    username = config.mailUsername
    host = "smtp.outlook.com"
    port = 587
    s = smtplib.SMTP(host=host, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg["To"] = username
    msg["From"] = username
    msg["Subject"] = "Product is Cheaper!"
    text = f"""<p><a href='{link}'>This item</a> is now {price} which is below your purchase level of {level}</p>"""
    msg.attach(MIMEText(text, 'html'))
    s.send_message(msg)
    del msg
