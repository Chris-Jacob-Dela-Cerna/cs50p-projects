

class Warrior:
    traits = {
        "normal": {
            "health": 12,
            "defence": 2,
            "attack": 2,
        },
        "tanky": {
            "health": 16,
            "defence": 3,
            "attack": 1,
        },
        "agile": {
            "health": 10,
            "defence": 1,
            "attack": 4,
        },
    }

    def __init__(self, trait):
        if not trait:
            raise ValueError("No trait selected.")
        if trait not in Warrior.traits:
            raise ValueError("Invalid trait.")

        self._trait = trait
        self.trait = trait

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


def main():
    w1 = Warrior("normal")
    w2 = Warrior("tanky")
    w3 = Warrior("agile")
    print(w1.stats())


if __name__ == "__main__":
    main()