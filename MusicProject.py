import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

trackList = []

#User inputs for album and artists
album = input("Album: ")

#token authorization
client_id = "56fd49ba85c441919d120bae8c1cb7c5"
client_secret = "78cf8ba2a5e545a3b4a8ff1c0a89f3da"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Album search to get the tracks on the albums
results = sp.search(q = "album:" + album, type = "album")
album_id = results['albums']['items'][0]['uri']
tracks = sp.album_tracks(album_id)
for x in tracks['items']:
    print(x['name'])

#Search the album dictionary for the artist uri
artistURI = results['albums']['items'][0]['artists'][0]['uri']
artist = results['albums']['items'][0]['artists'][0]['name']


#Get youtube links for each song
