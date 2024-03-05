import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import glob

"""api_client_id = ""
api_client_secret = ""

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))

playlist_list = ["37i9dQZF1DWZYOM6QxgTaX", "37i9dQZF1DXcF6B6QPhFDv", "37i9dQZF1DWWJOmJ7nRx0C", "37i9dQZF1DX82GYcclJ3Ug"]

def get_playlist(playlist, offset):
    resposta = spotify.playlist_items(playlist, offset=offset)
    with open(f'{playlist}-{offset}.json', 'w', encoding='utf-8') as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)
    if resposta["next"] == None:
        print("Final")
        pass
    else:
        offset = offset + 100
        print("Nova petició")
        get_playlist(playlist, offset)

for playlist in playlist_list:
    offset = 0
    get_playlist(playlist, offset)"""



files = glob.glob("*.json")
for file in files:
    with open(file) as f:
        d = json.load(f)
        tracks = d["items"]
        for track in tracks:
            name = track["track"]["name"]
            print (name)
