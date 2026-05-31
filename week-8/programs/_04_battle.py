

class Unit:
    def __init__(self, trait):
        if not trait:
            raise ValueError("No trait selected.")
        cls = self.__class__
        if trait not in cls.traits:
            raise ValueError("Invalid trait.")
        self._trait = trait
        self._health = cls.traits[trait]["health"]
        self._defence = cls.traits[trait]["defence"]
        self._attack = cls.traits[trait]["attack"]

    @property
    def trait(self):
        return self._trait
    
    @property
    def health(self):
        return self._health
    
    @property
    def attack(self):
        return self._attack
    
    @property
    def defence(self):
        return self._defence

    def stats(self):
        return f"\nTrait: {self._trait.title()}" \
               f"\nHealth: {self._health}" \
               f"\nAttack: {self._attack}" \
               f"\nDefence: {self._defence}"


class Warrior(Unit):
    traits = {
        "normal": {
            "health": 120,
            "attack": 25,
            "defence": 15,
        },
        "agile": {
            "health": 100,
            "attack": 35,
            "defence": 10,
        },
        "tanky": {
            "health": 150,
            "attack": 18,
            "defence": 25,
        },
    }

    def __init__(self, trait):
        super().__init__(trait)
    

class Archer(Unit):
    traits = {
        "normal": {
            "health": 100,
            "attack": 22,
            "defence": 12,
        },
        "sniper": {
            "health": 80,
            "attack": 45,
            "defence": 5,
        },
        "evasive": {
            "health": 110,
            "attack": 20,
            "defence": 18,
        },
    }

    def __init__(self, trait):
        super().__init__(trait)
    

class Giant(Unit):
    traits = {
        "normal": {
            "health": 160,
            "attack": 28,
            "defence": 10,
        },
        "brawler": {
            "health": 140,
            "attack": 40,
            "defence": 8,
        },
        "colossus": {
            "health": 200,
            "attack": 15,
            "defence": 22,
        },
    }

    def __init__(self, trait):
        super().__init__(trait)


def main():
    w1 = Warrior("agile")
    a1 = Archer("sniper")
    g1 = Giant("brawler")
    print(w1.stats())
    print(a1.stats())
    print(g1.stats())


if __name__ == "__main__":
    main()