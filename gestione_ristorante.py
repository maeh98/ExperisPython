
# Inizializza il dizionario dove salvare le vendite

menu = {}

# Chiedi fino a che il cliente non ha inserito tutte le vendite
while True:
    print("\n----------------------------  MENU  ---------------------------------------")
    print("Per visualizzare il menu: visualizza (v)")
    print("Per aggiungere un piatto digita: aggiungi (a)")
    print("Per rimuovere un piatto digita: rimuovi (r)")
    print("Per uscire digita: esci (e)")
    operazione = input("Digita la tua scelta: ").lower().strip()

    # Esci
    if operazione in ["esci", "e", "esci (e)"]:
        print("Operazione completata, il suo ordine arriverà a breve.\n")
        break           # Interrompi ciclo

    # Visualizza
    elif operazione in ["visualizza", "v", "visualizza (v)"]:
        # Stampa
        print("Il menu comprende: ")
        for key, value in menu.items():
            print(f'{value[0]} volte {key} a un prezzo di {value[1]}€ per piatto')
    
    # Aggiungi piatto
    elif operazione in ["aggiungi", "a", "aggiungi (a)"]:
        print("Indicare piatto")
        prodotto = input().lower().strip()
        print("Indicare prezzo")
        prezzo = input().lower().strip()

        # Aggiungi piatto al menu se non è presente, altrimenti aumenta di uno il conteggio
        if prodotto not in menu:
            menu[prodotto] = [1, prezzo]
        else:
            if menu[prodotto][1] == prezzo:
                menu[prodotto][0] += 1
            else:
                print('inserimento prezzo incorretto')
                continue
    
    # Rimuovi piatto
    elif operazione in ["rimuovi", "r", "rimuovi (r)"]:
        print("Scegli quale piatto vuoi rimuovere")
        prodotto = input().lower().strip()
        if prodotto in menu:
            print(f"Rimuovi 1 {prodotto}")
            # Se c'è solo un piatto, rimuovi il piatto dal menu, altrimenti riduci la quantita di uno
            if menu[prodotto][0] == 1:
                del menu[prodotto]
            else:
                menu[prodotto][0] -= 1

        else:
            print("Il prodotto non è nel menu")

    # Saluti
    print("Operazione completata!")



