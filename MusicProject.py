import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from YoutubeSearch import youtube_search
#from oauth2client.tools import argparser
import argparse

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
    trackList.append(x['name'])

#Search the album dictionary for the artist uri
artistURI = results['albums']['items'][0]['artists'][0]['uri']
artist = results['albums']['items'][0]['artists'][0]['name']

#Get youtube ids for each song

for x in range(0,len(trackList)):
    search = (artist+" "+album+" "+trackList[x])
    #Searches for the videos and returns video id
    if __name__ == "__main__":
      parser = argparse.ArgumentParser()
      parser.add_argument("--q", help="Search term", default=search)
      parser.add_argument("--max-results", help="Max results", default=1)
      args = parser.parse_args()
    try:
        youtube_search(args)
    except (HttpError,e):
        print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))

#Take youtube ids and put them into a list. This will get the youtube urls for each video
