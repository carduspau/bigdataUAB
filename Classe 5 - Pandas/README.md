# CLASSE 5 - 13/03/2024

Profundització de la llibreria *Pandas* per completar dos exercicis.

[Documentació dels exercicis](https://adriapadilla.github.io/bigdata-uab/pandas/ejercicio_pandas_1.html)

## Primer exercici: exercici_1.py

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
