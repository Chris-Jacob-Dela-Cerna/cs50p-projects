

class Bank:
    def __init__(self, pesos=0, dollars=0, gold=0):
        self.pesos = pesos
        self.dollars = dollars
        self.gold = gold

    def __str__(self):
        return f"Pesos: {self.pesos}" \
               f"\nDollars: {self.dollars}" \
               f"\nGold: {self.gold}"


hex = Bank()
print(hex)