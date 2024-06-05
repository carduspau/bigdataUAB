# CLASSE 4 - 05/03/2024

Primer, hem extret un volum alt d'informació amb l'API d'Spotify. A continuació, hem manipulat la informació dels fitxers .JSON amb les llibreries *glob*, *json* i *pandas*.

## Primer codi: main.py

Aquest codi exporta un .JSON amb la informació de totes les playlists introduïdes. Seguidament, importa el fitxer, el manipula i l'exporta amb .CSV.


**📤Extracció d'informació i exportació amb JSON**

```python
playlist_list = ["37i9dQZF1DWZYOM6QxgTaX", "37i9dQZF1DXcF6B6QPhFDv", "37i9dQZF1DWWJOmJ7nRx0C", "37i9dQZF1DX82GYcclJ3Ug"]

def get_playlist(playlist, offset):
    resposta = spotify.playlist_items(playlist, offset=offset)

    with open(f'{playlist}-{offset}.json', 'w', encoding='utf-8') as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)
    
    if resposta["next"] == None:
        pass

    else:
        offset = offset + 100
        get_playlist(playlist, offset)

for playlist in playlist_list:
    offset = 0
    get_playlist(playlist, offset)
```

**📝Importació del JSON, manipulació d'aquest i exportació amb CSV**

```python
files = glob.glob("*.json")
list_tracks = []

for file in files:
    with open(file) as f:
        d = json.load(f)
        tracks = d["items"]
        for track in tracks:
            track_dict = {}
            track_dict["name"] = track["track"]["name"]
            track_dict["popularity"] = track["track"]["popularity"]
            track_dict["artist_name"] = track["track"]["artists"][0]["name"]
            track_dict["duration_ms"] = track["track"]["duration_ms"]
            track_dict["duration_sec"] = round(track["track"]["duration_ms"]/100/60, 2)
            list_tracks.append(track_dict)

df = pd.DataFrame.from_dict(list_tracks)
df.to_csv("output.csv", index=False, sep=";")
```
