# CLASSE 3 - 27/02/2024

Hem combinat l'extracció d'artistes des de l'API d'Spotify per a representar-los amb Gephi.

## Primer codi: main.py

Aquest codi exporta un csv amb la informació d'origen i destí entre els artistes relacionats.

**🎵Extracció d'informació d'un artista**

```python
artist_id ="7ltDVBr6mKbRvohxheJ9h1"
resposta = spotify.artist_related_artists(artist_id)
```
**↔️Relació entre artistes**
```python
for artist in resultat["artists"]:
    artista = {}
    artista["origen"] = "segismundo toxicomano"
    artista["desti"] = artist["name"]
    artista["id"] = artist["id"]
    llista_de_relacionats.append(artista)
```
**📄 Exporta les dades al següent fitxer CSV:** [graf.csv](https://github.com/carduspau/bigdataUAB/blob/main/Classe%203%20-%20Spotify%20+%20Gephi/graf.csv)

**GRAF de la representació de les dades:** 
![Primer graf](https://i.ibb.co/McKtZdm/Captura-de-pantalla-2024-06-05-163030.png)

## Segon codi: generes_a_partir_de_playlist.py
Aquest codi exporta un csv amb la informació d'origen i destí entre els artistes i els gèneres musicals a partir de l'ID d'una playlist.

**⏯️Petició a l'API per obtenir les cançons d'una playlist**
```python
def get_playlist(playlist_id):
    resultat_playlist = spotify.playlist_items(playlist_id)
    return resultat_playlist
```

**🎸Combinació de resultats entre artistes i gèneres**
```python
for id in llista_id_artistes:
    resultat = get_artist(id)
    for artist in resultat["artists"]:
        for genere in artist["genres"]:
            source = artist["name"]
            target = genere
            tupla = (source, target)
            llista_final.append(tupla)
```

**📄 Exporta les dades al següent fitxer CSV:** [graf_generesmusicals.csv](https://github.com/carduspau/bigdataUAB/blob/main/Classe%203%20-%20Spotify%20+%20Gephi/graf_generesmusicals.csv)

**GRAF de la representació de les dades:** 
![Primer graf](https://i.ibb.co/ZXsYLpC/Captura-de-pantalla-2024-06-05-163528.png)

## Tercer codi: obtencio_generes_dels_relacionats.py
Aquest codi exporta un .CSV amb la informació d'origen i destí entre els artistes i gèneres musicals dels artistes relacionats a partir de l'ID d'un artista.

**🗂️Extracció, processament i exportació dels resultats**
```python
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

llista_final = []

for i in llista_definitiva:
    source =  i["origen"]
    target = i["genere"]
    tupla = (source, target)
    llista_final.append(tupla)

df = pd.DataFrame(llista_final, columns=["source", "target"])
df.to_csv("graf_generesmusicals.csv", sep=",", index=False)
```
**📄 Exporta les dades al següent fitxer CSV:** [generes_dels_relacionats.csv](https://github.com/carduspau/bigdataUAB/blob/main/Classe%203%20-%20Spotify%20%2B%20Gephi/generes_dels_relacionats.csv)


**GRAF de la representació de les dades:** 
![Primer graf](https://i.ibb.co/4J7SBxV/Captura-de-pantalla-2024-06-05-163724.png)
