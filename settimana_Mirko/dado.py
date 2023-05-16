# import
import random

class DADO:
    def __init__(self, n=20):
        self.n = n

    def lancia(self):
        return random.randint(1, self.n)

# Istanzia
dado = DADO(20)
print(f"Hai lanciato {dado.lancia()}")