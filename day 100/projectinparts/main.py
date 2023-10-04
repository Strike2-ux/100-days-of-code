from replit import db
import time
import schedule
from scraper import scrape_price
from email_sender import email_me

def add_to_db():
    link = input("Link: ")
    price = float(input("Price: "))
    db[time.time()] = {"link": link, "price": None, "level": price}

def update():
    keys = db.keys()
    for key in keys:
        url = db[key]["link"]
        price = db[key]["price"]
        level = db[key]["level"]
        this_price = scrape_price(url)

        if this_price != price:
            db[key]["price"] = this_price
            if this_price <= level:
                print("Cheaper")
                email_me(level, this_price, url, level)

if __name__ == "__main__":
    schedule.every(1).day.do(update)

    while True:
        schedule.run_pending()
        time.sleep(1)
