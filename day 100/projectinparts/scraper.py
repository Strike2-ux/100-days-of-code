from bs4 import BeautifulSoup
import requests

def scrape_price(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    myPrice = soup.find_all("span", {"class": "price"})
    thisPrice = float(myPrice[0].text[1:].replace(",", ""))
    
    return thisPrice
