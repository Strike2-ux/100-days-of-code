import requests
from bs4 import BeautifulSoup
import openai

# Step 1: Scrape the article from Wikipedia
url = "https://en.wikipedia.org/wiki/Hair_loss"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
article_content = soup.find("div", {"class": "mw-parser-output"}).text

# Step 2: Send the article to OpenAI for summarization
openai.api_key = 'YOUR_API_KEY'  # Replace with your actual OpenAI API key

# Define the function to summarize text
def summarize_text(text):
    prompt = f"Summarize the following text:\n{text}\n\nSummary:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150,
        temperature=0.5,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    summary = response.choices[0].text.strip()
    return summary

# Step 3: Generate the summary
summary = summarize_text(article_content)

# Step 4: Output the summary with Wikipedia references
print(summary)

# Step 5: Extract and print Wikipedia references
references = soup.find_all("ol", {"class": "references"})
if references:
    print("\nWikipedia References:")
    for ref in references:
        print(ref.text)
'''
import requests
from bs4 import BeautifulSoup

# Define a function to summarize a Wikipedia article.
def summarize_wikipedia_article(url, openai_api_key):
    """Summarizes a Wikipedia article in no more than 3 paragraphs with the Wikipedia references at the bottom.

    Args:
        url: The URL of the Wikipedia article.
        openai_api_key: Your OpenAI API key.

    Returns:
        A string containing the summary of the Wikipedia article.
    """

    # Scrape the Wikipedia article.
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    text_content = soup.get_text()

    # Send the text content to OpenAI for summarization.
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci/completions",
        headers={"Authorization": "Bearer " + openai_api_key},
        json={"prompt": "Summarize the following text in no more than 3 paragraphs:\n" + text_content},
    )

    # Get the summary from OpenAI.
    summary = response.json()["choices"][0]["text"]

    # Limit the summary to 3 paragraphs.
    summary = summary[: summary.find("\n\n\n") + 3]

    # Add the Wikipedia references to the summary.
    references = soup.find_all("ol", {"class": "references"})[0].prettify()
    summary += "\n\n" + references

    return summary


# Get the Wikipedia URL from the user.
url = input("Paste wiki URL > ")

# Get the OpenAI API key from the user.
openai_api_key = input("Enter your OpenAI API key > ")

# Summarize the Wikipedia article.
summary = summarize_wikipedia_article(url, openai_api_key)

# Print the summary.
print(summary)

'''