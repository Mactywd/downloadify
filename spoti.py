from dotenv import load_dotenv
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET")
))