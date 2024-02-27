import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

api_client_id = ""
api_client_secret = ""

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))

id_artista = "7ltDVBr6mKbRvohxheJ9h1"

llista_definitiva = []
def get_artist(artist_id):
    resultat = spotify.artist_related_artists(artist_id)
    return resultat

resultat = get_artist(id_artista)

for artist in resultat["artists"]:
    for genere in artist["genres"]:
        artista = {}
        artista["origen"] = artist["name"]
        artista["genere"] = genere

        llista_definitiva.append(artista)

print(llista_definitiva)

llista_final = []

for i in llista_definitiva:
    source =  i["origen"]
    target = i["genere"]
    tupla = (source, target)
    llista_final.append(tupla)

df = pd.DataFrame(llista_final, columns=["source", "target"])
print(df)
df.to_csv("graf_generesmusicals.csv", sep=",", index=False)













