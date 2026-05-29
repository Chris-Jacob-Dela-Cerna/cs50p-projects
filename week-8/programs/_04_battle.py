

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
        self.trait = trait

    @property
    def trait(self):
        return self._trait
    
    @trait.setter
    def trait(self, trait):
        if not trait:
            raise ValueError("No trait selected.")
        if trait not in Warrior.traits:
            raise ValueError("Invalid trait.")
        self._trait = trait


def main():
    ...


if __name__ == "__main__":
    main()