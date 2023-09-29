import requests
import json

# Set the NewsAPI API key
NEWSAPI_API_KEY = "YOUR_NEWSAPI_API_KEY"

# Set the OpenAI API key
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

# Define a function to get the top news stories for the day
def get_top_news_stories():
    # Make a request to the NewsAPI to get the top news stories for the day
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey={}".format(NEWSAPI_API_KEY)
    response = requests.get(url)
    json_response = json.loads(response.content)

    # Return the top 5 news stories
    return json_response["articles"][:5]

# Define a function to summarize a news story
def summarize_news_story(url):
    # Make a request to the OpenAI API to summarize the news story
    headers = {
        "Authorization": "Bearer {}".format(OPENAI_API_KEY)
    }
    payload = {
        "prompt": "Summarize the following news story:\n{}".format(url)
    }
    response = requests.post("https://api.openai.com/v1/engines/davinci/completions", headers=headers, json=payload)
    json_response = json.loads(response.content)

    # Return the summary of the news story
    return json_response["choices"][0]["text"]

# Define a function to print the top news stories for the day
def print_top_news_stories():
    # Get the top news stories for the day
    top_news_stories = get_top_news_stories()

    # Print the top news stories
    for i in range(len(top_news_stories)):
        print("[{}] {}".format(i + 1, top_news_stories[i]["title"]))
        print("Summary: {}".format(summarize_news_story(top_news_stories[i]["url"])))
        print()

# If the program is being run as a script, print the top news stories for the day
if __name__ == "__main__":
    print_top_news_stories()
