from flask import Flask, render_template, request, redirect, url_for
from typing import List

app = Flask(__name__)

# Set the offset for the next page of results
offset = 0

# Define a function to query the song database
def query_songs(year: int, offset: int) -> List[dict]:
    # TODO: Implement this function to query the song database and return a list of song objects
    songs = []
    return songs

# Define a function to render the embedded MP3 player
def render_mp3_player(url: str) -> str:
    return f'<audio controls><source src="{url}" type="audio/mpeg"></audio>'

# Define a route for the home page
@app.route("/")
def index():
    # Get the search year from the form
    year = request.args.get("year")

    # If the search year is empty, redirect to the home page
    if year is None:
        return redirect(url_for("index"))

    # Convert the search year to an integer
    try:
        year = int(year)
    except ValueError:
        return redirect(url_for("index"))

    # Query the song database
    songs = query_songs(year, offset)

    # Render the embedded MP3 players for each song
    embedded_mp3_players = [render_mp3_player(song["url"]) for song in songs]

    # Render the index page with the embedded MP3 players
    return render_template("index.html", songs=songs, embedded_mp3_players=embedded_mp3_players)

# Define a route for the next page of results
@app.route("/next")
def next():
    # Increment the offset
    offset += 10

    # Redirect to the home page with the updated offset
    return redirect(url_for("index", offset=offset))

if __name__ == "__main__":
    app.run(debug=True)
