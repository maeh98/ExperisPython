# Parola
stringa = "banana"

# Inizializza
dizionario = {}

# Cicla sulle lettere della parola
for lettera in stringa:
    # Aggiungi lettera al dizionario se non è presente
    if lettera not in dizionario:
        dizionario[lettera] = 1
    else:
        # Se è già presente aumenta il conteggio
        dizionario[lettera] += 1

# Printa
print(dizionario.items())