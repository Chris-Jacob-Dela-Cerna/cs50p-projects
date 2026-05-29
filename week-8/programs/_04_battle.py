

class Warrior:
    traits = {
        "normal": {
            "health": 10,
            "defence": 2,
            "attack": 2,
        },
        "tanky": {
            "health": 15,
            "defence": 3,
            "attack": 1,
        },
        "agile": {
            "health": 10,
            "defence": 1,
            "attack": 3,
        },
    }

    def __init__(self, trait):
        self.traits = Warrior.traits
        self.trait = trait
        self._health = self.traits[trait]["health"]
        self._defence = self.traits[trait]["defence"]
        self._attack = self.traits[trait]["attack"]
        self._initialized = True

    @property
    def trait(self):
        return self._trait
    
    @trait.setter
    def trait(self, trait):
        if hasattr(self, "_initialized") and self._initialized:
            raise AttributeError("Trait cannot be changed.")
        if not trait:
            raise ValueError("No trait selected.")
        if trait not in Warrior.traits:
            raise ValueError("Invalid trait.")
        self._trait = trait

    def stats(self):
        return f"\nTrait: {self._trait.title()}\nHealth: {self._health}\nDefence: {self._defence}\nAttack: {self._attack}"


def main():
    w1 = Warrior("normal")
    print(w1.stats())
    w2 = Warrior("tanky")
    print(w2.stats())
    w3 = Warrior("agile")
    print(w3.stats())


if __name__ == "__main__":
    main()