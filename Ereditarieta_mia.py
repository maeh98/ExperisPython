class Uno:
    
    uno = "uno"                              # attributi

    # Metodi

    def __init__(self, Nome):              # costruttore
        self.Nome = Nome
        

    def MasterD(self):                          # Metodo della classe
        print(" i numeri sono " + self.uno)


X = Uno("Mirko")
X.MasterD()

class Due(Uno):

    def __init__(self, Nome, Eta):
        super().__init__(Nome)
        self.Eta = Eta

    due = "due"

    def MasterD(self):                          # Metodo della classe
        print(" i numeri sono " + self.uno + ", " + self.due)


Y = Due("Marius", 23)
Y.MasterD()

class Tre(Due):

    tre = "tre"

    def __init__(self, Nome, Eta, grado):
        super().__init__(Nome, Eta)
        self.grado = grado

    def MasterD(self):                          # Metodo della classe
        print(" i numeri sono " + self.uno + ", " + self.due + ", " + self.tre)

Z = Tre("Marius", 23, "TERZO DAN")
Z.MasterD()