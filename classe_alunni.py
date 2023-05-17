
class Alunno:
    def __init__(self, Nome):              # costruttore
        self.Nome = Nome

    def MasterD(self):                          # Metodo della classe
        print(" ciao sono " + self.Nome)


class Scheda(Alunno):
    def __init__(self, Nome, grado):       # Stessa struttura per metodi piu convenzionali
        super().__init__(Nome)
        self.grado = grado

    def MasterD(self):                          # Metodo della classe
        super().MasterD()
        print(" ciao sono " + self.Nome + " " + self.grado)


class LISTAALUNNI():
    lista_schede_alunni = []
    def __init__(self, *alunni_schede):
        self.lista_schede_alunni = [*alunni_schede]

    def stampa_tutto(self):                          # Metodo della classe
        print(f"Ci sono {len(self.lista_schede_alunni)} alunni e sono: \n")
        for iter, alunno_scheda in enumerate(self.lista_schede_alunni):
            print(f"{iter}. {alunno_scheda.Nome} ha ottenuto un voto di {alunno_scheda.grado}")

    def aggiungi_schede(self, *alunni_schede):
        self.lista_schede_alunni += [*alunni_schede]

    def rimuovi_scheda_alunni(self, alunno_scheda):
        idx = self.lista_schede_alunni.index(alunno_scheda)
        del self.lista_schede_alunni[idx]

    def modifica_schea_alunni(self, alunno_scheda, nuovo_voto):
        idx = self.lista_schede_alunni.index(alunno_scheda)
        self.lista_schede_alunni[idx].grado = nuovo_voto




def switch_primo():
    print("\n---------------------------------------------------------5")
    print("Scegli l'opzione desiderata: ")
    print("1. Entra")
    print("2. Esci")

    variabile = input().strip()         

    if variabile == "1":
        esci = False
        while not esci:
            # Entra nel secondo menu
            esci = switch_secondo()

    elif variabile == "2":
        print("Hai scelto di uscire, arriverci!")
        return "esci"
    
    else:
        print("L'ordine non è stato eseguito correttamente")


def switch_secondo():
    print("\n---------------------------------------------------------5")
    print("Scegli l'opzione desiderata: ")
    print("1. Aggiungi scheda")
    print("2. Elimina scheda")
    print("3. Stampa tutte le schede")
    print("4. Modifica voto")
    print("5. Esci")

    variabile = input().strip()                         # Scelta

    if variabile == "1":                                # Aggiungi scheda
        print(f"Inserisci nome e voto")
        nome = input("Nome: ").strip()                  # Chiedi nome
        voto = int(input("Voto: ").strip())             # Chiedi voto
        lista.aggiungi_schede(Scheda(nome, voto))       # Crea oggetto scheda e aggiungi a lista

    elif variabile == "2":                              # Elimina scheda
        print("Scegli la scheda da eliminare")
        lista.stampa_tutto()
        n_elimina = int(input("alunno: ").strip())
        lista.rimuovi_scheda_alunni(lista.lista_schede_alunni[n_elimina])
        print("L'alunno è stato eliminato")
    
    elif variabile == "3":                              # Stampa tutte le schede
        lista.stampa_tutto()

    elif variabile == "4":                              # Modifica voto
        print("Scegli la scheda da modificare")
        lista.stampa_tutto()
        n_modifica = int(input("alunno: ").strip())
        nuovo_voto = int(input("Setta nuovo voto: ").strip())

        lista.modifica_schea_alunni(lista.lista_schede_alunni[n_modifica], nuovo_voto)

        print("La scheda è stata modificata")

    elif variabile == "5":                              # esci
        print("Hai scelto di uscire, arriverci!")
        return "esci"
    
    else:
        print("L'ordine non è stato eseguito correttamente")


# Istanzia l'oggetto che rappresenta la lista delle schede degli alunni
lista = LISTAALUNNI()
# Entra nel primo menu
switch_primo()
lista.stampa_tutto()

