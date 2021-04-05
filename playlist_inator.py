
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

#           $env:SPOTIPY_CLIENT_ID="aa6aa76d6e284f06bde2d13631af4983"
#
#           $env:SPOTIPY_CLIENT_SECRET="42ebc2d3b5984092af23676d4204d80c"
#
#           $env:SPOTIPY_REDIRECT_URI="http://localhost:8888/callback"

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


artist_name = str(input())
playlist_name = artist_name + "inator 9000"
description = "A collection of 10 songs by " + artist_name + " alongside 3 songs from each of their 20 related artists. Made using spotipy 2.17.1"

playlist = sp.user_playlist_create('poph55', playlist_name, public = True, collaborative = False, description = description)

artist_finder = sp.search(q='artist:' + artist_name, type='artist')
uri = artist_finder['artists']['items'][0]['uri']
print(uri)

results = sp.artist_top_tracks(uri)



for track in results['tracks'][:10]:


    track_id =[track['uri']]
    sp.user_playlist_add_tracks('poph55', playlist.get('id'), track_id)


related = sp.artist_related_artists(uri)
related_uri_list = []

for artist in related['artists']:
    related_uri_list.append(artist['uri'])
print(related_uri_list)

for string in related_uri_list:
    results = sp.artist_top_tracks(string)
    for track in results['tracks'][:3]:
        track_id =[track['uri']]
        sp.user_playlist_add_tracks('poph55',playlist.get('id'),track_id)