"""Scrivere un programma che prenda una lista di numeri come input e rimuove i duplicati dalla lista, lasciando solo i valori "unici".
 L'ordine degli elementi nella lista deve rimanere invariato"""

caratteri_ammessi = "0123456789"

numero = "034 p521-77"
# Inizializza una stringa dove contieni le cifre in ordine, senza altri caratteri
numero_ordinato = ""

# Cicla sui caratteri in numero, e aggiungili alla stringa numero_ordinato solo se
#   sono caratteri ammessi e la cifra non è già presente
for carattere in numero:
    if carattere in numero_ordinato or carattere not in caratteri_ammessi:
        pass
    else:
        numero_ordinato += carattere

print(numero_ordinato)
