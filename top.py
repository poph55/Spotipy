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


top_artists = sp.current_user_top_artists(20, offset = 0, time_range='medium_term')


print(top_artists)