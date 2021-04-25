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

count = df5['artist'].value_counts()
#print(count)

dance_data = df5.groupby(['artist'])['danceability'].mean()
#print(dance_data)

print("The average dancebility of Bazzi's songs in my top 100 is " + str(dance_data[3]) + ". He appeared in my top 100 " + str(count[0]) + " times.")

print("The average dancebililty of Quinn XCII's songs in my top 100 is " + str(dance_data[43]) + ". He appeared in my top 100 " + str(count[1]) + " times.")

print("The average dancebililty of One Direction's songs in my top 100 is " + str(dance_data[41]) + ". They appeared in my top 100 " + str(count[2]) + " times.")

print("The average dancebililty of Chelsea Cutler's songs in my top 100 is " + str(dance_data[9]) + ". She appeared in my top 100 " + str(count[3]) + " times.")
 
print("The average dancebililty of Lost Kings's songs in my top 100 is " + str(dance_data[34]) + ". They appeared in my top 100 " + str(count[4]) + " times.")

