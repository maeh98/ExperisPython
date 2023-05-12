"""Scrivere un programma python per la gestione di un registro vendite.
Il programma deve permettere di aggiungere le vendite di diversi prodotti e calcolare il totale delle vendite (per ogni prodotto).
1) Aggiungi una vendita di un prodotto (si richiede all'utente il nome del prodotto, la quantità ed il prezzo per unità)
2) Visualizzare il totale delle vendite per ogni prodotto per ogni prodotto presente nel registro 
Suggerimento: utilizzare un dizionario per memorizzare le vendite dei prodotti
 (le chiavi sono i nomi dei prodotti e i valori sono liste che contengono quantità e prezzo unitario) 
"""
# Inizializza il dizionario dove salvare le vendite
dizionario = {}

# Chiedi fino a che il cliente non ha inserito tutte le vendite
while True:
    print("Indicare prodotto venduto")
    print("Per uscire digitare: esci")
    prodotto = input().lower().strip()

    if prodotto == "esci":
        break

    print("Indicare quantità di prodotto venduto")
    quantita = int(input().strip())
    print("Indicare prezzo prodotto")
    prezzo = float(input().strip())



    if prodotto not in dizionario:
        dizionario[prodotto] = [quantita, prezzo]
    else:
        if dizionario[prodotto][1] == prezzo:
            dizionario[prodotto][0] += quantita
        else:
            print('inserimento prezzo incorretto')
            continue

# Stampa
for key, value in dizionario.items():
    print(f'{key} è stato venduto {value[0]} volte a un prezzo di {value[1]}€')

    
