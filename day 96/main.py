import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://news.ycombinator.com/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the headlines
headlines = soup.find_all("a", class_="storylink")

# Define the keywords
keywords = ["Python", "Replit"]

# Loop through the headlines and check for keywords
for headline in headlines:
    title = headline.text
    for keyword in keywords:
        if keyword.lower() in title.lower():  # Case insensitive search
            print(title)
            break
'''
import requests
from bs4 import BeautifulSoup

def get_hacker_news_headlines():
  """Scrapes the headlines from Hacker News and returns a list of strings."""

  response = requests.get("https://news.ycombinator.com/")
  soup = BeautifulSoup(response.content, "html.parser")

  headlines = []
  for headline in soup.find_all("a", class_="titlelink"):
    headlines.append(headline.text)

  return headlines

def filter_headlines_by_keywords(headlines, keywords):
  """Filters the headlines by keywords and returns a list of strings."""

  filtered_headlines = []
  for headline in headlines:
    for keyword in keywords:
      if keyword.lower() in headline.lower():
        filtered_headlines.append(headline)
        break

  return filtered_headlines

def main():
  """The main function of the program."""

  headlines = get_hacker_news_headlines()
  filtered_headlines = filter_headlines_by_keywords(headlines, ["Python", "Replit"])

  # Use a for loop to iterate over the filtered headlines and print them to the console.
  for headline in filtered_headlines:
    print(headline)

if __name__ == "__main__":
  main()

'''