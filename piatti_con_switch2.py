

class ORDINE:
    lista_ordinazioni = []
    conto_totale = 0
    nome = ""
    MENU = [("antipasto", 5), ("primo piatto", 10), ("secondo piatto", 15), ("dolce", 3)]

    # Settare nome
    #def chiedi_nome(self):
    #    self.nome = input("Come ti chiami?\n")

    def aggiungi_piatto(self):
        # Elenca piatti
        print("I piatti disponibili sono: ")
        for contatore in range(4):
            print(f"{contatore}. {self.MENU[contatore][0]} costa {self.MENU[contatore][1]}€")

        # Chiedi quale piatto aggiungere e aggiungilo alla lista
        piatto_scelto = int(input().strip())
        self.lista_ordinazioni += [ordinazione.MENU[piatto_scelto]]
        # Aggiorna conto
        self.conto_totale += ordinazione.MENU[piatto_scelto][1]

    def modifica_piatto(self):
        # Elenco piatti ordinazione
        print("I piatti nell'ordinazione sono: ")
        for contatore in range(len(self.lista_ordinazioni)):
            print(f"{contatore}. {self.lista_ordinazioni[contatore][0]} costa {self.lista_ordinazioni[contatore][1]}€")
    
        # Chiedi quale rimuovere e agisci
        print ("Quale desideri rimuovere?\n")
        piatto_da_rimuovere = int(input().strip())
        # Elenco piatti MENU
        print("Con quale piatto lo vuoi rimpiazzare? \nI piatti disponibili sono: ")
        for contatore in range(4):
            print(f"{contatore}. {self.MENU[contatore][0]} costa {self.MENU[contatore][1]}€")
        
        # Chiedi quale aggiungere e agisci
        piatto_da_aggiungere = int(input().strip())
        # Aggiorna conto
        self.conto_totale += self.MENU[piatto_da_aggiungere][1] - self.lista_ordinazioni[piatto_da_rimuovere][1]
        # Aggiorna ordine
        self.lista_ordinazioni[piatto_da_rimuovere] = self.MENU[piatto_da_aggiungere]

    def elimina_piatto(self):
        print("I piatti nell'ordinazione sono: ")
        for contatore in range(len(self.lista_ordinazioni)):
            print(f"{contatore}. {self.lista_ordinazioni[contatore][0]} costa {self.lista_ordinazioni[contatore][1]}€")

        print ("Quale desideri rimuovere?\n")
        piatto_da_rimuovere = int(input().strip())
        # Aggiorna conto
        self.conto_totale -= self.lista_ordinazioni[piatto_da_rimuovere][1]
        # Elimina ordine
        del self.lista_ordinazioni

    def ordinare_conto(self):
        # Elenco piatti MENU  
        print("I piatti ordinati sono: ")
        for contatore in range(len(self.lista_ordinazioni)):
            print(f"{self.lista_ordinazioni[contatore][0]} costa {self.lista_ordinazioni[contatore][1]}€")
        
        print(f"Il conto totale è {self.conto_totale}€")


    def switch_primo(self):
        print("\n---------------------------------------------------------5")
        print("Scegli l'opzione desiderata: ")
        print("1. Ordina un piatto")
        print("2. Modificare un piatto")
        print("3. Elimina un piatto")
        print("4. Ordinare il conto")
        print("5. Esci")

        variabile = input().strip()         

        if variabile == "1":
            self.aggiungi_piatto()

        elif variabile == "2":
            self.modifica_piatto()
        
        elif variabile == "3":
            self.elimina_piatto()

        elif variabile == "4":
            self.ordinare_conto()
        
        elif variabile == "5":
            print("Hai scelto di uscire, arriverci!")
            return "esci"
        
        else:
            print("L'ordine non è stato eseguito correttamente")


class UTENTE():
    nome = ""
    budget = 0

    def __str__(self):
        return self.nome

    # Settare nome
    def chiedi_nome(self):
        self.nome = input("Come ti chiami?\n")
    
    # Setti budget
    def chiedi_budget(self):
        self.budget = int(input("Qual'è il tuo budget?" ))

# Istanzia
utente = UTENTE()
ordinazione = ORDINE()
utente.chiedi_nome()
utente.chiedi_budget()

print(f"L'utente è {str(utente)}")
esci = False        # flag
while not esci:
    esci = ordinazione.switch_primo()
    if ordinazione.conto_totale > utente.budget:
        print("Stai andando sopra il budget, riduci o modifica il tuo ordine")
        esci = False



