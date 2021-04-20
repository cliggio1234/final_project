import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 

client_id = 'c7c042c1a50a4202b30e64d401461e2b'
client_secret = '0585a3aaf38540d5b06743126f414cbd'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
print('hi')
## TAYLOR SWIFT AND ALL HER SONGS SORTED INTO A CSV
def getTrackIDs6(user, playlist_id):
    ids6 = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids6.append(track['id'])
    return ids6
ids6 = getTrackIDs6('1292839507', '03DKLbZBo14ZllyuWl3USg')   

def getTrackFeatures6(id):
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
tracks6 = []
for i in range(len(ids6)):
  time.sleep(.5)
  track6 = getTrackFeatures6(ids6[i])
  tracks6.append(track6)
# create dataset with all the wanted columns
#df6 = pd.DataFrame(tracks6, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
#df6.to_csv("addie-top-100.csv", sep = ',')
#PRINTIMG THINGS
##print(ids6)
##print(len(ids6))\
#group_by_1 = df6.groupby(['artist']).count()
#print(group_by_1)






def getTrackIDs5(user, playlist_id):
    ids5 = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids5.append(track['id'])
    return ids5
ids5 = getTrackIDs5('1292839507', '37i9dQZF1EM3lkVCiFpDCn')   

def getTrackFeatures5(id):
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
tracks5 = []
for i in range(len(ids5)):
  time.sleep(.5)
  track5 = getTrackFeatures5(ids5[i])
  tracks5.append(track5)
# create dataset with all the wanted columns
df5 = pd.DataFrame(tracks5, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df5.to_csv("my-top-100.csv", sep = ',')