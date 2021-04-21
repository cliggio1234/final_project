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


def getTrackIDs6(user, playlist_id):
  #Extracting Track IDs from Addie's Top 100 Songs Playlist
    ids6 = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids6.append(track['id'])
    return ids6
ids6 = getTrackIDs6('1292839507', '03DKLbZBo14ZllyuWl3USg')   

def getTrackFeatures6(id):
  #Track Ids into categories/columns 
  meta = sp.track(id)
  features = sp.audio_features(id)
  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  #release_date = meta['album']['release_date']
  #length = meta['duration_ms']
  #lengths = length/60000
  popularity = meta['popularity']
  # declaring features
  #acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  #energy = features[0]['energy']
  #instrumentalness = features[0]['instrumentalness']
  #liveness = features[0]['liveness']
  #loudness = features[0]['loudness']
  #speechiness = features[0]['speechiness']
  #tempo = features[0]['tempo']
  #time_signature = features[0]['time_signature']
  track = [name, album, artist, popularity, danceability]
  return track
  # loop over track ids 
tracks6 = []
for i in range(len(ids6)):
  time.sleep(.5)
  track6 = getTrackFeatures6(ids6[i])
  tracks6.append(track6)
# create dataset with all the wanted columns
df6 = pd.DataFrame(tracks6, columns = ['name', 'album', 'artist',  'popularity', 'danceability'])
df6.to_csv("addie-top-100.csv", sep = ',')


#converting addie-top-100.csv to SQlite3

df6 = pd.read_csv('addie-top-100.csv', encoding = "UTF-8", index_col = [0])
df6.columns = df6.columns.str.strip()
df6.columns = df6.columns.str.replace("."," ")
df6.head()

conn = sqlite3.connect('addieTopDB.db')
c = conn.cursor
df6.to_sql("AddieTopSongs", conn)
c.execute('''SELECT * FROM AddieTopSongs;''')
data = pd.DataFrame(c.fetchall())
data.columns = [x[0] for x in c.description]
data




