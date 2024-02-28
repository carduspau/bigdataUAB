import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

api_client_id = ""
api_client_secret = ""

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))

playlist_id = "37i9dQZF1DWZYOM6QxgTaX"
llista_final = []

def get_playlist(playlist_id):
    resultat_playlist = spotify.playlist_items(playlist_id)
    return resultat_playlist

resultat_playlist = get_playlist(playlist_id)

with open('resposta.json', 'w', encoding='utf-8') as f:
    json.dump(resultat_playlist, f, ensure_ascii=False, indent=4)

llista_id_artistes = []

for artista_playlist in resultat_playlist["items"]:
    for j in artista_playlist["track"]["artists"]:
        id_artista = j["id"]
        llista_id_artistes.append(id_artista)


def get_artist(artist_id):
    resultat = spotify.artist_related_artists(artist_id)
    return resultat

print(llista_id_artistes)

for id in llista_id_artistes:
    try:
        print(id)
        resultat = get_artist(id)
        for artist in resultat["artists"]:
            for genere in artist["genres"]:
                source = artist["name"]
                target = genere
                tupla = (source, target)
                llista_final.append(tupla)
    except:
        print("ERROR PROBLEMA")
        pass

print(llista_final)

df = pd.DataFrame(llista_final, columns=["source", "target"])
print(df)
df.to_csv("graf_generesmusicals.csv", sep=",", index=False)

