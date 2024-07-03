import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configura las credenciales de tu aplicación de Spotify
SPOTIPY_CLIENT_ID = 'tu_client_id'
SPOTIPY_CLIENT_SECRET = 'tu_client_secret'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'playlist-read-private'

# Autentica usando Spotipy
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SCOPE))

# Obtén las canciones de una playlist de Spotify
def obtener_canciones_de_spotify(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    canciones = []
    for item in results['items']:
        track = item['track']
        canciones.append(track['name'] + ' ' + track['artists'][0]['name'])
    return canciones

playlist_id = 'tu_playlist_id'  # ID de la playlist de Spotify
canciones_spotify = obtener_canciones_de_spotify(playlist_id)
print(canciones_spotify)
