import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import spotipy


CLIENT_ID = "YOUR CLIENT_ID"
CLIENT_SECRET = "YOUR CLIENT_SECRET"

URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
year = date.split("-")[0]

response = requests.get(url=f"{URL}{date}")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
sections = soup.find_all(name="div", class_="o-chart-results-list-row-container")
songs = [song.find(name="h3", id="title-of-a-story").text.strip() for song in sections]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR USERNAME",
    )
)

user_id = sp.current_user()["id"]
name_of_playlist = f"{date} Billboard 100"
description = f"The Top 100 Songs from Billboard on day {date}"
playlist = sp.user_playlist_create(user=user_id, name=name_of_playlist, public=False, description=description)
playlist_id = playlist["id"]

list_of_songs = []
for song in songs:
    query = f"track:{song} year:{year}"
    try:
        new_song = sp.search(q=query, limit=10, type=['track'], offset=0, market="US")
        song_id = new_song["tracks"]["items"][0]["id"]
    except IndexError:
        continue
    else:
        print(f"{song_id}: {song} ")
        list_of_songs.append(song_id)

sp.playlist_add_items(playlist_id=playlist_id, items=list_of_songs)

