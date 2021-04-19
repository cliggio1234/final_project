#from bs4 import BeautifulSoup
#import requests
#import re
#import os
#import csv
#import unittest
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 

client_id = 'c7c042c1a50a4202b30e64d401461e2b'
client_secret = '0585a3aaf38540d5b06743126f414cbd'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

## JUSTIN BIEBER PLAYLIST OF ALL SONGS SORTED INTO A CSV 
def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids
ids = getTrackIDs('1292839507', '3M4ZBeI0K4RTd8uFdR5Oy7')   

def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)
  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  lengths = length/60000
  popularity = meta['popularity']
  # declaring features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']
  time_signature = features[0]['time_signature']
  track = [name, album, artist, release_date, lengths, popularity, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track
  # loop over track ids 
tracks = []
for i in range(len(ids)):
  time.sleep(.5)
  track = getTrackFeatures(ids[i])
  tracks.append(track)
# create dataset with all the wanted columns
df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df.to_csv("justin-bieber.csv", sep = ',')
#PRINTIMG THINGS
##print(ids)
##print(len(ids))


## TAYLOR SWIFT AND ALL HER SONGS SORTED INTO A CSV
def getTrackIDs2(user, playlist_id):
    ids2 = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids2.append(track['id'])
    return ids2
ids2 = getTrackIDs2('1292839507', '1uwZEapkVmeIgXUmdjY6XW')   

def getTrackFeatures2(id):
  meta = sp.track(id)
  features = sp.audio_features(id)
  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  lengths = length/60000
  popularity = meta['popularity']
  # declaring features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']
  time_signature = features[0]['time_signature']
  track = [name, album, artist, release_date, lengths, popularity, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track
  # loop over track ids 
tracks2 = []
for i in range(len(ids2)):
  time.sleep(.5)
  track2 = getTrackFeatures2(ids2[i])
  tracks2.append(track2)
# create dataset with all the wanted columns
df2 = pd.DataFrame(tracks2, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df2.to_csv("taylor-swift.csv", sep = ',')
#PRINTIMG THINGS
##print(ids2)
##print(len(ids2))

#DUA LIPA AND ALL HER MUSIC IN A PLAYLIST

def getTrackIDs3(user, playlist_id):
    ids3 = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids3.append(track['id'])
    return ids3
ids3= getTrackIDs3('1292839507', '32fxdKFuOwfbL4XqS0NckK')   

def getTrackFeatures3(id):
  meta = sp.track(id)
  features = sp.audio_features(id)
  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  lengths = length/60000
  popularity = meta['popularity']
  # declaring features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']
  time_signature = features[0]['time_signature']
  track = [name, album, artist, release_date, lengths, popularity, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track
  # loop over track ids 
tracks3 = []
for i in range(len(ids3)):
  time.sleep(.5)
  track3 = getTrackFeatures3(ids3[i])
  tracks3.append(track3)
# create dataset with all the wanted columns
df3 = pd.DataFrame(tracks3, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df3.to_csv("dua-lipa.csv", sep = ',')
#PRINTIMG THINGS
##print(ids3)
##print(len(ids3))


## FRANK OCEAN AND ALL HIS SONGS IN PLAYLIST CSV.
def getTrackIDs4(user, playlist_id):
    ids4 = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids4.append(track['id'])
    return ids4
ids4= getTrackIDs4('1292839507', '3EBRl55ls0udYcDIQAW0OW')   

def getTrackFeatures4(id):
  meta = sp.track(id)
  features = sp.audio_features(id)
  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  lengths = length/60000
  popularity = meta['popularity']
  # declaring features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']
  time_signature = features[0]['time_signature']
  track = [name, album, artist, release_date, lengths, popularity, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track
  # loop over track ids 
tracks4 = []
for i in range(len(ids4)):
  time.sleep(.5)
  track4 = getTrackFeatures4(ids4[i])
  tracks4.append(track4)
# create dataset with all the wanted columns
df4 = pd.DataFrame(tracks4, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df4.to_csv("frank-ocean.csv", sep = ',')
#PRINTIMG THINGS
##print(ids4)
##print(len(ids4))
 

### STATS OF THE CSVS 
#mean danceability score of JUSTIN BIEBER
mean1 = df['danceability'].mean()
print('Mean danceability score of Justin Bieber is ' +str(mean1))
#mean danceability song of TAYLOR SWIFT
mean2 = df2['danceability'].mean()
print(mean2)
#mean danceability score of DUA LIPA
mean3 = df3['danceability'].mean()
print(mean3)
#mean danceability score of FRANK OCEAN
mean4 = df4['danceability'].mean()
print(mean4)