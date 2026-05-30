

class Warrior:
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
        if not trait:
            raise ValueError("No trait selected.")
        if trait not in Warrior.traits:
            raise ValueError("Invalid trait.")
        self._trait = trait

        self._health = Warrior.traits[trait]["health"]
        self._defence = Warrior.traits[trait]["defence"]
        self._attack = Warrior.traits[trait]["attack"]

    # Runs once when setting the unit's trait
    @property
    def trait(self):
        return self._trait

    # Shows a unit's stats
    def stats(self):
        return f"\nTrait: {self._trait.title()}\nHealth: {self._health}\nDefence: {self._defence}\nAttack: {self._attack}"
    

class Archer:
    traits = {
        "normal": {
            "health": 120,
            "attack": 25,
            "defence": 15,
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
        if not trait:
            raise ValueError("No trait selected.")
        if trait not in Archer.traits:
            raise ValueError("Invalid trait.")
        self._trait = trait

        self._health = Archer.traits[trait]["health"]
        self._defence = Archer.traits[trait]["defence"]
        self._attack = Archer.traits[trait]["attack"]

    # Runs once when setting the unit's trait
    @property
    def trait(self):
        return self._trait

    # Shows a unit's stats
    def stats(self):
        return f"\nTrait: {self._trait.title()}\nHealth: {self._health}\nDefence: {self._defence}\nAttack: {self._attack}"
    

class Giant:
    traits = {
        "normal": {
            "health": 160,
            "attack": 28,
            "defence": 15,
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
        if not trait:
            raise ValueError("No trait selected.")
        if trait not in Giant.traits:
            raise ValueError("Invalid trait.")
        self._trait = trait

        self._health = Giant.traits[trait]["health"]
        self._defence = Giant.traits[trait]["defence"]
        self._attack = Giant.traits[trait]["attack"]

    # Runs once when setting the unit's trait
    @property
    def trait(self):
        return self._trait

    # Shows a unit's stats
    def stats(self):
        return f"\nTrait: {self._trait.title()}\nHealth: {self._health}\nDefence: {self._defence}\nAttack: {self._attack}"


def main():
    ...


if __name__ == "__main__":
    main()