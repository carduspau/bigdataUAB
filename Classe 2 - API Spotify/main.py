# AQUEST CODI EXPORTA UN EXCEL AMB LA INFORMACIÓ DELS RELACIONATS DELS RELACIONATS

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

api_client_id = ""
api_client_secret = ""

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))

artist_id ="7ltDVBr6mKbRvohxheJ9h1"

resposta = spotify.artist_related_artists(artist_id)

with open('data_resposta.json', 'w', encoding='utf-8') as f:
    json.dump(resposta, f, ensure_ascii=False, indent=4)

artistes = resposta["artists"]

llista_artistes = []

for a in artistes:
    nom = a["name"]
    seguidors = a["followers"]["total"]
    link = a["external_urls"]["spotify"]

    frame = pd.DataFrame({
        "nom": nom,
        "seguidors": seguidors,
        "enllaç": link,
    }, index=[0])

    llista_artistes.append(frame)

for i in artistes:
    artist_id_related = i["id"]
    resposta_related = spotify.artist_related_artists(artist_id_related)
    artistes_related = resposta_related["artists"]
    for a in artistes_related:
        nom = a["name"]
        seguidors = a["followers"]["total"]
        link = a["external_urls"]["spotify"]

        frame = pd.DataFrame({
            "nom": nom,
            "seguidors": seguidors,
            "enllaç": link,
        }, index=[0])

        llista_artistes.append(frame)

final = pd.concat(llista_artistes)

print(final)

final.to_excel("dataset.xlsx")

