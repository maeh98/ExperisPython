"""calcolatrice: +, -, *
stampare, uscire, contare
"""
class Calcolatrice:
    operazioni = [[]]

    # Salva i risultati assieme all'operatore
    def carica_risultato(self, risultato, operatore):
        self.operazioni[-1] += [(risultato, operatore)]

    # Crea una nuova riga per i risultati
    def nuovo_ciclo(self):
        self.operazioni += [[]]

    def elimina_risultati(self):
        self.operazioni = [[]]
 
    def addizione(self, numero_1, numero_2):
        return numero_1 + numero_2
    
    def sottrazione(self, numero_1, numero_2):
        return numero_1 - numero_2
    
    def moltiplicazione(self, numero_1, numero_2):
        return numero_1 * numero_2

    # Somma dei tre risultati
    def calcolo_totale(self):
        totale = 0
        for i in range(len(self.operazioni[-1])):
            totale += self.operazioni[-1][i][0]
        
        return totale

# Istanzia oggetto calcolatrice
calcolo = Calcolatrice()
flag = False

while not flag:
    print("Benvenuto in calcolatrice: digita conta, end, stamp o elimina (storico)")
    comando = input()

    # Esci
    if comando == "end":
        print("Arrivederci!")
        flag = True

    # Stampa
    elif comando == "stamp":
        if calcolo.operazioni == [[]]:
            print("Lo storico È vuoto")
        else:
            print(calcolo.operazioni)
            for ciclo in calcolo.operazioni:
                print("---------------------------------------------")
                print(f"Le operazione sono {ciclo[0][1]}: {ciclo[0][0]}, {ciclo[1][1]}: {ciclo[1][0]}, {ciclo[2][1]}: {ciclo[2][0]}")

    # Elimina risultati
    elif comando == "elimina":
        print("Sei sicuro di voler eliminare tutti i risultati? \nY/n")
        sicuro = input().lower().strip()
        if sicuro == "y":
            calcolo.elimina_risultati()
            print("Hai eliminato tutto lo storico dei risultati")
        else:
            print("Commando abortito")

    # Operazioni
    elif comando == "conta":
        # Inizia una nuova riga
        if calcolo.operazioni != [[]]:
            calcolo.nuovo_ciclo()
        # Tre volte
        for i in range(3):
            # Chiedi due numeri
            print("Scegli due numeri")
            a = float(input("a: "))
            b = float(input("b: "))
            # Chiedi quale operazione svolgere
            print("Scegli un'operazione: ")
            print("addizione, sottrazione, moltiplicazione")
            operazione = input().lower()
            print(f"Hai scelto {operazione}")

            if operazione == "addizione":
                risultato = calcolo.addizione(a, b)
                calcolo.carica_risultato(risultato, operazione)

            elif operazione == "sottrazione":
                risultato = calcolo.sottrazione(a, b)
                calcolo.carica_risultato(risultato, operazione)

            elif operazione == "moltiplicazione":
                risultato = calcolo.moltiplicazione(a, b)
                calcolo.carica_risultato(risultato, operazione)
            
        print(f"L'addizione tra i risultati delle tre operazioni dá {calcolo.calcolo_totale()}")
    
    else:
        print("Comando errato")









