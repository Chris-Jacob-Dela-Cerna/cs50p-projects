# Document: This python is my 5th application of CS50P Week 8.

class Bank:
    def __init__(self, pesos=0, dollars=0, gold=0):
        self.pesos = pesos
        self.dollars = dollars
        self.gold = gold

    def __str__(self):
        return f"Pesos: {self.pesos}" \
               f"\nDollars: {self.dollars}" \
               f"\nGold: {self.gold}"

    def __add__(self, other):
        pesos = self.pesos + other.pesos
        dollars = self.dollars + other.dollars
        gold = self.gold + other.gold
        return Bank(pesos, dollars, gold)