import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 
import sqlite3
import csv_to_sqlite
#getting access from Spotipy
client_id = 'c7c042c1a50a4202b30e64d401461e2b'
client_secret = '0585a3aaf38540d5b06743126f414cbd'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


#creating a csv for My top 100 Spotify Songs 


def getTrackIDs5(user, playlist_id):
  #extracting the track IDS from My Top Songs playlist
    ids5 = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids5.append(track['id'])
    return ids5
ids5 = getTrackIDs5('1292839507', '37i9dQZF1EM3lkVCiFpDCn')   

def getTrackFeatures5(id):
  #converting the ids into categories/columns
  meta = sp.track(id)
  features = sp.audio_features(id)
  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  popularity = meta['popularity']
  # declaring features
  danceability = features[0]['danceability']
  track = [name, album, artist, popularity, danceability]
  return track
  # loop over track ids 
tracks5 = []
for i in range(len(ids5)):
  time.sleep(.5)
  track5 = getTrackFeatures5(ids5[i])
  tracks5.append(track5)
# create dataset with all the wanted columns
df5 = pd.DataFrame(tracks5, columns = ['name', 'album', 'artist',  'popularity', 'danceability'])


#converting my My-top-100.csv to SQlite3

df5 = pd.read_csv('my-top-100.csv', encoding = "UTF-8", index_col = [0])
df5.columns = df5.columns.str.strip()
df5.columns = df5.columns.str.replace("."," ")
df5.head()

conn = sqlite3.connect('myTopDB.db')
c = conn.cursor
df5.to_sql("MyTopSongss", conn)
c.execute('''SELECT * FROM MyTopSongs;''')
data = pd.DataFrame(c.fetchall())
data.columns = [x[0] for x in c.description]
data

c.execute('''SELECT artist , COUNT(*)
              FROM MyTopSongs
              GROUP BY artist
              ORDER BY COUNT(*) DESC;''')
data = pd.DataFrame(c.fetchall())
data.columns = [x[0] for x in c.description]
data