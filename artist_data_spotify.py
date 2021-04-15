import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 

client_id = 'c7c042c1a50a4202b30e64d401461e2b'
client_secret = '0585a3aaf38540d5b06743126f414cbd'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

name = "Justin Bieber" #chosen artist
result = sp.search(name) #search query
result['tracks']['items'][0]['artists']

