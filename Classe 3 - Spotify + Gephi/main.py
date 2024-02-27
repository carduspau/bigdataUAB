import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

api_client_id = "503363c7cf514111ab42d2863c2cb540"
api_client_secret = "85a7230016664afe8aa862125669c4a0"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))
artist_id ="7ltDVBr6mKbRvohxheJ9h1"
llista_artistes = []

def get_artist(artist_id):
    resultat = spotify.artist_related_artists(artist_id)
    return resultat

resultat = get_artist(artist_id)

llista_de_relacionats = []

for artist in resultat["artists"]:
    artista = {}
    artista["origen"] = "segismundo toxicomano"
    artista["desti"] = artist["name"]
    artista["id"] = artist["id"]
    llista_de_relacionats.append(artista)

llista_provisional = llista_de_relacionats.copy()

for j in llista_provisional:
    print(j["desti"])
    print(j["id"])
    print("-------")
    resultat2 = get_artist(j["id"])
    for artist in resultat2["artists"]:
        artista = {}
        artista["origen"] = j["desti"]
        artista["desti"] = artist["name"]
        artista["id"] = artist["id"]
        llista_de_relacionats.append(artista)


llista_tuples = []

for i in llista_de_relacionats:
    source =  i["origen"]
    target = i["desti"]
    tupla = (source, target)
    llista_tuples.append(tupla)

df = pd.DataFrame(llista_tuples, columns=["source", "target"])
print(df)
df.to_csv("graf.csv", sep=",", index=False)
