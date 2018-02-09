# Music Downloader
The point of this project was to be able to download albums of music off of the
internet, mainly through the use of turning the audio from youtube videos into 
mp3s. This allows for the use of this music on platfroms such as itunes. This
is my alternative tot paying for a music streaming service such as spotify. 
This program works by typing in a specific album name, and that is it. All of the
songs from the album will appear in the specified destination folder.

# Technical Explanation
When developing this program, I used a few different APIs and libraries included for python.
Once the album is typed in, it is first ran through Spotifys web API to find a list
of all of the tracks on the requested album. To easily use the Spotify API, I used an
avaliable phyton shell called spotipy. Then once I got the tracks, I used the search function
in googles youtube data api. This allowed for me to get youtube video ids for each of the songs.
After this was done I then used youtube-dl library to download the mp3 files off of each of the
videos. All of these downloads currently end up in a desination folder hierarchy of the artist,
and then the album, then all of the songs.

# Future Plans
Going on, the first thing I plan on implementing is to edit the metadata of the downloaded 
mp3s so that they are all the right name have the correct track number and artist. I also plan
on implementing something where it downloads a .jpg of the album artwork and puts it into the 
album folder as well. There is also a bug right now where the youtube data api does not return
a video id for some reason, so I want to implement something that fixes that. Also some of the videos
come back as not the music video. A way to maybe fix this issue is to use view count of youtube videos 
to get a better estimate on what is actually the music video, and what is other videos (ie. covers, instrumentals).
Finally, I want to add more search functions to download all of the songs from an artist and such.
