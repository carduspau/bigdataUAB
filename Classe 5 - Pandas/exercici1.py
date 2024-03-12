import pandas as pd

notes = [1,6,8,9,10,6,5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]

# --- SUMAR 1 PUNT ---
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
print (mitjana)

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

df = pd.DataFrame.from_dict(insercions)
print(df)
df.to_csv("output.csv", index=False, sep=";")
