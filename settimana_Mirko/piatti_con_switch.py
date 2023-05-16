
class ORDINE:
    lista_ordinazioni = []
    nome = ""
    conto_totale = 0
    MENU = [("antipasto", 5), ("primo piatto", 10), ("secondo piatto", 15), ("dolce", 3)]

    # Settare nome
    def chiedi_nome(self):
        self.nome = input("Come ti chiami?\n")
    
    def esci(self):
        print("Hai scelto di uscire, arriverci!")
        return None

    def aggiungi_piatto(self):
        print("I piatti disponibili sono: ")
        for contatore in range(4):
            print(f"{contatore}. {self.MENU[contatore][0]} costa {self.MENU[contatore][1]}€")
        
        piatto_scelto = int(input().strip())

        self.lista_ordinazioni += [ordinazione.MENU[piatto_scelto]]

    def modifica_piatto(self):
        print("I piatti nell'ordinazione sono: ")
        for contatore in range(len(self.lista_ordinazioni)):
            print(f"{contatore}. {self.lista_ordinazioni[contatore][0]} costa {self.lista_ordinazioni[contatore][1]}€")

        print ("Quale desideri rimuovere?\n")
        piatto_da_rimuovere = int(input().strip())
        print("Con quale piatto lo vuoi rimpiazzare? \nI piatti disponibili sono: ")
        for contatore in range(4):
            print(f"{contatore}. {self.MENU[contatore][0]} costa {self.MENU[contatore][1]}€")
        
        piatto_da_aggiungere = int(input().strip())
        self.lista_ordinazioni[piatto_da_rimuovere] = self.MENU[piatto_da_aggiungere]


    def ordinare_conto(self):
        # Resetta conto
        self.conto_totale = 0
        print("I piatti ordinati sono: ")
        for contatore in range(len(self.lista_ordinazioni)):
            print(f"{contatore}. {self.lista_ordinazioni[contatore][0]} costa {self.lista_ordinazioni[contatore][1]}€")
            self.conto_totale += self.lista_ordinazioni[contatore][1]
        
        print(f"Il conto totale di {self.nome} è {self.conto_totale}")


    def switch_primo(self):
        print("Scegli l'opzione desiderata: ")
        print("1. Ordina un piatto")
        print("2. Modificare un piatto")
        print("3. Ordinare il conto")
        print("4. Esci")

        variabile = input().strip()         

        if variabile == "1":
            self.aggiungi_piatto()

        elif variabile == "2":
            self.modifica_piatto()

        elif variabile == "3":
            self.ordinare_conto()
        
        elif variabile == "4":
            self.esci()
            return "esci"
        
        else:
            print("L'ordine non è stato eseguito correttamente")


ordinazione = ORDINE()
ordinazione.chiedi_nome()

esci = False
while not esci:
    esci = ordinazione.switch_primo()



