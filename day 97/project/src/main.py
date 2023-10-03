import requests
from bs4 import BeautifulSoup
import openai
from flask import Flask, render_template

app = Flask(__name__)

# Set up OpenAI API
openai.api_key = 'YOUR_API_KEY'

@app.route('/')
def scrape_and_summarize():
    # Step 1: Scrape the article
    url = "https://en.wikipedia.org/wiki/Hair_loss"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the main content of the article
    article_content = soup.find("div", {"class": "mw-parser-output"})
    text = " ".join([p.text for p in article_content.find_all("p")])

    # Step 2: Send it to OpenAI for summarization
    response = openai.Summarizer.create(
        model="davinci",
        documents=[text],
        max_tokens=150
    )

    summary = response.choices[0].text.strip()

    # Render the summary with references template
    return render_template('summary.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)

'''
for this structure 
project_root/
├── main.py
└── README.md

you should use this code ==>

import requests
from bs4 import BeautifulSoup
import openai

# Set the OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Scrape the Wikipedia article
def scrape_wikipedia_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

# Summarize the article using the OpenAI summarizer
def summarize_article(article):
    prompt = "Summarize the following Wikipedia article in no more than 3 paragraphs:\n\n" + article
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
    )
    summary = response["choices"][0]["text"]
    return summary

# Output the summary with the Wikipedia references at the bottom
def output_summary(summary, references):
    print(summary)
    print("\nWikipedia references:")
    for reference in references:
        print(reference.text.strip())  # strip() to remove whitespace at the beginning and end of the text

# Get the Wikipedia URL as input
url = input("Paste Wikipedia URL > ")

# Scrape the Wikipedia article
soup = scrape_wikipedia_article(url)

# Summarize the article using the OpenAI summarizer
summary = summarize_article(soup.get_text())

# Output the summary with the Wikipedia references at the bottom
output_summary(summary, soup.find_all("ol", {"class": "references"}))


'''