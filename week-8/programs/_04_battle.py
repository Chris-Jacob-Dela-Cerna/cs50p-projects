

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


def main():
    w1 = Warrior("normal")
    w2 = Warrior("tanky")
    w3 = Warrior("agile")


if __name__ == "__main__":
    main()