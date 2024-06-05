# CLASSE 5 - 13/03/2024

Profundització de la llibreria *Pandas* per completar dos exercicis.

[Documentació dels exercicis](https://adriapadilla.github.io/bigdata-uab/pandas/ejercicio_pandas_1.html)

## Primer exercici: Introducció a Pandas (exercici_1.py)

A partir de tres llistes: *notes*, *noms* i *cognoms*, 
```python
notes = [1,6,8,9,10,6,5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]
```
l'objectiu és generar un .CSV amb aquestes 5 columnes:

1. **Columna 1:** Nom i cognoms (en una única cadena de text) de cada alumne
2. **Columna 2:** Nota de cada alumne
3. **Columna 3:** Nota "en text" per a cada alumne:
   - Si la nota final és inferior a 5, afegir el text "suspès".
   - Si la nota es troba entre 5 i 6 (ambdós inclosos), afegir el text "aprovat".
   - Si la nota és superior a 6, i inferior a 7, afegir el text "bé".
   - Si la nota és igual o superior a 7, afegir el text "notable".
   - Si la nota supera el 9, afegir el text "excel·lent".
   - Si la nota equival a un 10, afegir el text "matrícula d'honor".
4. **Columna 4:** Diferència de nota respecte a la mediana del grup
5. **Columna 5:** Diferència de nota (expressada en percentatge) respecte a la mediana del grup

    **Extra:** Abans de fer els càlculs, has de sumar UN punt a cada alumne, però la nota màxima mai no pot superar el 10.


**➕Afegir 1 punt a cada alumne sense que la nota superi el 10***
```python
posicio = 0
suma_notes = 0

for nota in notes:
    if nota <10:
        nota += 1
        notes[posicio] = nota
    else:
        pass
    posicio += 1
    suma_notes = suma_notes + nota

mitjana = round(suma_notes/posicio, 2)
```


**🔧Modificació de les llistes amb *Pandas***

```python
insercions = []

for i in range(len(notes)):
    insercio = {}
    insercio["Nom i cognoms"] = alumnes[i] + ' ' + cognoms[i]
    insercio["Nota"] = notes[i]

    if notes[i] < 5:
        text_nota = 'Suspès'
    elif notes[i] <=6:
        text_nota = 'Aprovat'
    elif notes[i] < 7:
        text_nota = 'Bé'
    elif notes[i] >= 7 and notes[i] < 9:
        text_nota = 'Notable'
    elif notes[i] >= 9 and notes[i] < 10:
        text_nota = 'Excel·lent'
    elif notes[i] == 10:
        text_nota = 'Matrícula d\'honor'

    insercio["Nota en text"] = text_nota
    insercio["Diferència de mitjana"] = round(notes[i] - mitjana, 2)
    insercio["Diferència de mitjana en %"] = round(((notes[i]-mitjana)*100)/mitjana, 2)

    insercions.append(insercio)
```

**📖 Taula generada**

| Nom i cognoms       | Nota | Nota en text          | Diferència de mitjana | Diferència de mitjana en % |
|---------------------|------|-----------------------|-----------------------|----------------------------|
| Jaume Tort          | 2    | Suspès                | -5.29                 | -72.57                     |
| Carles Soldevila    | 7    | Notable               | -0.29                 | -3.98                      |
| Cristina Luna       | 9    | Excel·lent            | 1.71                  | 23.46                      |
| Josep Muñoz         | 10   | Matrícula d'honor     | 2.71                  | 37.17                      |
| Rafael Fernandez    | 10   | Matrícula d'honor     | 2.71                  | 37.17                      |
| Agnès Hernandez     | 7    | Notable               | -0.29                 | -3.98                      |
| Marta Llopart       | 6    | Aprovat               | -1.29                 | -17.70                     |

Consultar a [exercici_1.csv](https://github.com/carduspau/bigdataUAB/blob/main/Classe%205%20-%20Pandas/exercici_1.csv)

## Segon exercici: Anàlisi de dades de YouTube (exercici_2.py)

A partir d'un *dataset* en .XLSX proporcionat amb les dades del canal de YouTube "KEXP", volem saber:
1. Volum general: Quantes files i columnes té el dataset complet?
2. Composició del dataset: Quines columnes componen el dataset?
3. Calcula la desviació (absoluta i percentual) de cada vídeo sobre la mitjana d'espectadors/comentaris/m'agrada del canal.
4. Localitza el vídeo més vist.
5. Localitza el vídeo més comentat.
6. Crea una nova columna per a cada un dels valors calculats anteriorment, i crea un nou dataset final que incorpori tota la nova informació.
7. Calcula la durada en segons de cada vídeo, i indica la seva desviació percentual sobre la mitjana de durada dels vídeos del canal.
8. Visualitza totes les estadístiques calculades anteriorment en un gràfic de Tableau.

**📄 Processament i modificació de dades**
```python
average_views = df["viewCount"].mean()
average_comments = df["commentCount"].mean()
average_likes = df["likeCount"].mean()

df["desviacio_likes_total"] = df["likeCount"] - average_likes
df["desviacio_likes_percentual"] = (df["likeCount"] - average_likes) / average_likes * 100

df["desviacio_comments_total"] = df["commentCount"] - average_comments
df["desviacio_comments_percentual"] = (df["commentCount"] - average_comments) / average_comments * 100

df["desviacio_views_total"] = df["viewCount"] - average_views
df["desviacio_views_percentual"] = (df["viewCount"] - average_views) / average_views * 100

max_view = df[df["viewCount"] == df["viewCount"].max()]

max_comment = df[df["commentCount"] == df["commentCount"].max()]
```

Consultar a [exercici_2.csv](https://github.com/carduspau/bigdataUAB/blob/main/Classe%205%20-%20Pandas/exercici_2.csv)
