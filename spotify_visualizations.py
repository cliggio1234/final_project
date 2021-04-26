import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 
import sqlite3
import csv_to_sqlite
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np

"""
Getting Access to Spotify API
"""
client_id = 'c7c042c1a50a4202b30e64d401461e2b'
client_secret = '0585a3aaf38540d5b06743126f414cbd'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getTrackIDs5(user, playlist_id):
  """
  Extracting Track IDs of every track in Christina's top 100 playlist.
  """
  ids5 = []
  playlist = sp.user_playlist(user, playlist_id)
  for item in playlist['tracks']['items']:
      track = item['track']
      ids5.append(track['id'])
  return ids5
ids5 = getTrackIDs5('1292839507', '37i9dQZF1EM3lkVCiFpDCn')   

def getTrackFeatures5(id):
  """
  Converting Christina's track ids into categories/columns.

  """
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
"""
Create dataset with all of the wanted columns.
"""
df5 = pd.DataFrame(tracks5, columns = ['name', 'album', 'artist',  'popularity', 'danceability'])
df5.to_csv("my-top-100.csv", sep = ',')

"""
Getting the amount of times artists are feautred in Christina's top 100.
"""
count = df5['artist'].value_counts()

"""
Getting the mean danceability score for the songs grouped by the most frequent artists
"""
dance_data = df5.groupby(['artist'])['danceability'].mean()


def getTrackIDs6(user, playlist_id):
  """
  Extracting Track IDs of every track in Addies's top 100 playlist.
  """
  ids6 = []
  playlist = sp.user_playlist(user, playlist_id)
  for item in playlist['tracks']['items']:
      track = item['track']
      ids6.append(track['id'])
  return ids6
ids6 = getTrackIDs6('1292839507', '03DKLbZBo14ZllyuWl3USg')   

def getTrackFeatures6(id):
  """
  Converting Christina's track ids into categories/columns.
  """
  meta = sp.track(id)
  features = sp.audio_features(id)
  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  popularity = meta['popularity']
  danceability = features[0]['danceability']
  track = [name, album, artist, popularity, danceability]
  return track
  # loop over track ids 
tracks6 = []
for i in range(len(ids6)):
  time.sleep(.5)
  track6 = getTrackFeatures6(ids6[i])
  tracks6.append(track6)


"""
Create dataset with all of the wanted columns.
"""
df6 = pd.DataFrame(tracks6, columns = ['name', 'album', 'artist',  'popularity', 'danceability'])
df6.to_csv("addie-top-100.csv", sep = ',')

"""
Getting the amount of times artists are feautred in Addie's top 100.
"""
count2 = df6['artist'].value_counts().tolist()

"""
Getting the mean danceability score for the songs grouped by the most frequent artists for Addie.
"""
dance_data2 = df6.groupby(['artist'])['danceability'].mean()

"""
Converting data in lists so that it can be used with matplotlib"
"""
pop_for_visual1 = df5['popularity'].tolist()
dance_for_visual1 = df5['danceability'].tolist()
count_for_visual = count2[:5]

"""
Writing into file the top artists, how many times they are featured in the top 100, and the average danceability of their feautured songs.
"""
file = open("myavg_dance.txt", "a")

file.write("The average danceability of Bazzi's songs in my top 100 is " + str(dance_data[3]) + ". He appeared in my top 100 " + str(count[0]) + " times.\n"

"The average danceabililty of Quinn XCII's songs in my top 100 is " + str(dance_data[43]) + ". He appeared in my top 100 " + str(count[1]) + " times.\n"

"The average danceabililty of One Direction's songs in my top 100 is " + str(dance_data[41]) + ". They appeared in my top 100 " + str(count[2]) + " times.\n"

"The average danceabililty of Chelsea Cutler's songs in my top 100 is " + str(dance_data[9]) + ". She appeared in my top 100 " + str(count[3]) + " times.\n"
 
"The average danceabililty of Lost Kings's songs in my top 100 is " + str(dance_data[34]) + ". They appeared in my top 100 " + str(count[4]) + " times.\n"

 )
file.close()

"""
Writing into file the top artists, how many times they are featured in the top 100, and the average danceability of their feautured songs.
"""

file = open("myavg_dance.txt", "a")

file.write("The average dancebility of Ariana Grande's's songs in Addie's top 100 is " + str(dance_data[4]) + ". She appeared in it " + str(count2[0]) + " times.\n"

"The average dancebililty of Taylor Swift's songs in Addie's top 100 is " + str(dance_data2[54]) + ". She appeared in it " + str(count2[1]) + " times.\n"

"The average dancebililty of Justin Bieber's songs in Addie's top 100 is " + str(dance_data2[22]) + ". He appeared in it " + str(count2[2]) + " times.\n"

"The average dancebililty of Madison Beer's songs in Addie's top 100 is " + str(dance_data2[34]) + ". She appeared in it " + str(count2[3]) + " times.\n"
 
"The average dancebililty of Zara Larsson's songs in Addie's top 100 is " + str(dance_data2[-4]) + ". She appeared in it " + str(count2[4]) + " times."
)
file.close()


"""
Creating a bar chart that shows the frequency of the top 5 artists is Addie's Top 100 songs.
"""
labels = ['Ariana Grande', 'Taylor Swift', 'Justin Bieber', 'Madison Beer', 'Zara Larsson']
counts_per_artist = [count_for_visual[0], count_for_visual[1], count_for_visual[2], count_for_visual[3], count_for_visual[4]]
plt.bar(labels, counts_per_artist, align = "center", color = ["blue", "blue", "blue", "blue", "blue"])
plt.title("The Amount Top Artists Appeared in Addie's Top 100 Songs")
plt.xlabel("Top 5 Artist Names")
plt.ylabel("Frequency")
plt.savefig("Addie_countper_artist.png")
plt.show()

"""
Creating a Scatter Plot where the x-axis is the Dancebility of a song and the y-axis is the popularity for Christina's playlist.
"""

fig, ax = plt.subplots()
for color in['tab:green']:
    x= pop_for_visual1
    y= dance_for_visual1
    ax.scatter(x, y, c=color, label=color, 
               alpha=0.3, edgecolors='none')
plt.title("Christina's Top 100 Popularity Versus Danceability")
plt.xlabel("Popularity")
plt.ylabel("Danceability")
ax.legend()
ax.grid(True)
plt.savefig("Scatterplot_dancevspop.png")
plt.show()

