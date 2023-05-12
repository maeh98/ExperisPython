stringa = "banana"

dizionario = {}

for lettera in stringa:
    if lettera not in dizionario:
        dizionario[lettera] = 1
    else:
        dizionario[lettera] += 1

print(dizionario.items())