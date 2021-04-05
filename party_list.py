import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from datetime import date
import random

#           $env:SPOTIPY_CLIENT_ID="aa6aa76d6e284f06bde2d13631af4983"
#
#           $env:SPOTIPY_CLIENT_SECRET="42ebc2d3b5984092af23676d4204d80c"    
#
#           $env:SPOTIPY_REDIRECT_URI="http://localhost:8888/callback"

date = date.today()

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


playlist_name = str(date) + " playlist"
description = "Collection of songs from top charts and playlists. Made using spotipy 2.17.1"

my_playlist = sp.user_playlist_create('poph55', playlist_name, public = True, collaborative = False, description = description)

print(playlist_name)
username = 'spotify'

rap_caviar = "spotify:playlist:37i9dQZF1DX0XUsuxWHRQd"
top_hits = "spotify:playlist:37i9dQZF1DXcBWIGoYBM5M"
get_turnt = "spotify:playlist:37i9dQZF1DWY4xHQp97fN6"
alt_hh = "spotify:playlist:37i9dQZF1DWTggY0yqBxES"

young_thug = "spotify:playlist:37i9dQZF1DXe5osTANjnfx"
lil_uzi = "spotify:playlist:37i9dQZF1DX4sqNyKH13qY"
future = "spotify:playlist:37i9dQZF1DWVstK6FYh8Nw"
kendrick = "spotify:playlist:37i9dQZF1DX5EkyRFIV92g"

playlists = [rap_caviar, top_hits, get_turnt, alt_hh, young_thug, lil_uzi, future, kendrick]
songs_list = []

for string in playlists:
    print(string)
    
    results = sp.user_playlist_tracks('spotify', string)



    for i, item in enumerate(results['items']):
        track = item['track']

        songs_list.append(track['uri'])

songs_list = list(set(songs_list))

for string in songs_list:
    track_id = [string]
    randval = random.random()  

    if (randval < 100/len(songs_list)):
        sp.user_playlist_add_tracks('poph55', my_playlist.get('id'), track_id)
