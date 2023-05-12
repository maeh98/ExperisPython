"""
Realizzare un codice che prende una "frase" in input
e ne restiuisce un dizionario che conti quante volte ogni parola appare nella "frase" 
"""

# Ottieni una frase
frase = input("Scegli una frase: \n")

# Separa le parole della lista
frase_lista = frase.split(" ")

# Inizializza il dizionario
dizionario = {}

# Cicla sulle parole della frase
for parola in frase_lista:
    # Aggiungi lettera al dizionario se non è presente
    if parola not in dizionario:
        dizionario[parola] = 1
    else:
        # Se è già presente aumenta il conteggio
        dizionario[parola] += 1

# Printa
print(dizionario.items())
