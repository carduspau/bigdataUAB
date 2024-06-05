# CLASSE 2 - 20/02/2024

Introducció a l'API d'Spotify fent servir la llibreria Spotipy.

## Primer codi: main.py

Aquest codi exporta un fitxer excel amb el *nom*, *seguidors* i *enllaç* dels artistes relacionats dels relacionats a partir de l'ID d'un artista.

**🎵Extracció d'informació d'un artista**

```python
artist_id ="7ltDVBr6mKbRvohxheJ9h1"
resposta = spotify.artist_related_artists(artist_id)
```
**👨🏼‍🎤Obtenció del nom, seguidors i enllaç dels artistes relacionats**
```python
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
```
*Aquest bucle s'executa dues vegades per a obtenir els relacionats dels relacionats.*

**⏏️Preparació i exportació de dades**
```python
final = pd.concat(llista_artistes)
final.to_excel("dataset.xlsx")
```

**📄 Exporta les dades al següent fitxer Excel:**- [dataset.xlsx](https://github.com/carduspau/bigdataUAB/blob/main/Classe%202%20-%20API%20Spotify/dataset.xlsx)

## Segon codi: deures.py
Hem d'exportar la màxima informació dels artistes, com el *nom*, *seguidors*, *enllaç*, *identificador*, *gèneres*, *href*, *id*, *imatge*, *popularitat*, *tipus* i *uri*.

La diferència amb el primer codi és l'extracció de variables:
```python
frame = pd.DataFrame({
        "nom": nom,
        "seguidors": seguidors,
        "enllaç": link,
        "identificador": id,
        "generes": genres,
        "href api": href_api,
        "id artista": id_artista,
        "imatge": imatge,
        "popularitat": popularity,
        "tipus": type,
        "uri": uri,
}, index=[0])
```
**📄 Exporta les dades al següent fitxer Excel:**- [dataset_deures.xlsx](https://github.com/carduspau/bigdataUAB/blob/main/Classe%202%20-%20API%20Spotify/dataset_deures.xlsx)
