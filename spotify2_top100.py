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


count = df6['artist'].value_counts()
#print(count)

dance_data = df6.groupby(['artist'])['danceability'].mean()
#print(dance_data[:60])

print("The average dancebility of Ariana Grande's's songs in Addie's top 100 is " + str(dance_data[4]) + ". She appeared in it " + str(count[0]) + " times.")

print("The average dancebililty of Taylor Swift's songs in Addie's top 100 is " + str(dance_data[54]) + ". She appeared in it " + str(count[1]) + " times.")

print("The average dancebililty of Justin Bieber's songs in Addie's top 100 is " + str(dance_data[22]) + ". He appeared in it " + str(count[2]) + " times.")

print("The average dancebililty of Madison Beer's songs in Addie's top 100 is " + str(dance_data[34]) + ". She appeared in it " + str(count[3]) + " times.")
 
print("The average dancebililty of Zara Larsson's songs in Addie's top 100 is " + str(dance_data[-4]) + ". She appeared in it " + str(count[4]) + " times.")



