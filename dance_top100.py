import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 
import sqlite3
import csv_to_sqlite
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np



#getting access from Spotipy
client_id = 'c7c042c1a50a4202b30e64d401461e2b'
client_secret = '0585a3aaf38540d5b06743126f414cbd'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


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

#getting the amount of times that an artist appears in top100.
count = df5['artist'].value_counts()
#print(count)

#writing out the top artists who appeared in the top 100 and the average danceability 
dance_data = df5.groupby(['artist'])['danceability'].mean()
#print(dance_data)

#writing out the top artists who appeared in the top 100 and the average danceability 
print("The average dancebility of Bazzi's songs in my top 100 is " + str(dance_data[3]) + ". He appeared in my top 100 " + str(count[0]) + " times.")

print("The average dancebililty of Quinn XCII's songs in my top 100 is " + str(dance_data[43]) + ". He appeared in my top 100 " + str(count[1]) + " times.")

print("The average dancebililty of One Direction's songs in my top 100 is " + str(dance_data[41]) + ". They appeared in my top 100 " + str(count[2]) + " times.")

print("The average dancebililty of Chelsea Cutler's songs in my top 100 is " + str(dance_data[9]) + ". She appeared in my top 100 " + str(count[3]) + " times.")
 
print("The average dancebililty of Lost Kings's songs in my top 100 is " + str(dance_data[34]) + ". They appeared in my top 100 " + str(count[4]) + " times.")


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

#getting the amount of times that an artist appears in top100.
count2 = df6['artist'].value_counts().tolist()
#print(count2)

print(type(count2))

count_for_visual = count2[:5]
print(count_for_visual)



"""
#getting the average dancebility of the songs that appear on top 100 for each artist
dance_data2 = df6.groupby(['artist'])['danceability'].mean()
#print(dance_data2[:60])
 

#writing out the top artists who appeared in the top 100 and the average danceability 
print("The average danceability of Ariana Grande's's songs in Addie's top 100 is " + str(dance_data2[4]) + ". She appeared in it " + str(count2[0]) + " times.")

print("The average danceabililty of Taylor Swift's songs in Addie's top 100 is " + str(dance_data2[54]) + ". She appeared in it " + str(count2[1]) + " times.")

print("The average danceabililty of Justin Bieber's songs in Addie's top 100 is " + str(dance_data2[22]) + ". He appeared in it " + str(count2[2]) + " times.")

print("The average danceabililty of Madison Beer's songs in Addie's top 100 is " + str(dance_data2[34]) + ". She appeared in it " + str(count2[3]) + " times.")
 
print("The average danceabililty of Zara Larsson's songs in Addie's top 100 is " + str(dance_data2[-4]) + ". She appeared in it " + str(count2[4]) + " times.")

"""


labels = ['Ariana Grande', 'Taylor Swift', 'Justin Bieber', 'Madison Beer', 'Zara Larsson']
counts_per_artist = [count_for_visual[0], count_for_visual[1], count_for_visual[2], count_for_visual[3], count_for_visual[4]]
plt.bar(labels, counts_per_artist, align = "center", color = ["blue", "blue", "blue", "blue", "blue"])
plt.title("The Amount Top Artists Appeared in Addie's Top 100 Songs")
plt.xlabel("Top 5 Artist Names")
plt.ylabel("Frequency")
plt.savefig("Addie_countper_artist.png")
plt.show()
