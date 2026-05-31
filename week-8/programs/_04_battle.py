

class Unit:
    def __init__(self, trait):
        if not trait:
            raise ValueError("No trait selected.")
        cls_ = self.__class__
        if trait not in cls_.traits:
            raise ValueError("Invalid trait.")
        self._trait = trait
        self._max_health = cls_.traits[trait]["health"]
        self._health = self._max_health
        self._defence = cls_.traits[trait]["defence"]
        self._attack = cls_.traits[trait]["attack"]

    @property
    def trait(self):
        return self._trait

    @property
    def max_health(self):
        return self._max_health

    @property
    def health(self):
        return round(self._health, 2)

    @property
    def attack(self):
        return self._attack

    @property
    def defence(self):
        return self._defence

    def stats(self):
        return f"\nTrait: {self.trait.title()}" \
               f"\nHealth: {self.health}/{self.max_health}" \
               f"\nAttack: {self.attack}" \
               f"\nDefence: {self.defence}"
    
    def damage(self, attack):
        dmg = attack - self._defence
        if dmg <= 0:
            dmg = 1
        self._health -= dmg

    def heal(self):
        max_heal = self._max_health / 2
        min_heal = self._max_health / 100
        miss_health = 1 - (self._health / self._max_health)
        healed = min_heal + (max_heal - min_heal) * miss_health
        total = self._health + healed
        if total >= self._max_health:
            self._health = self._max_health
        else:
            self._health = total


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
    a1 = Archer("normal")
    a1.damage(32)
    print(a1.stats())
    a1.heal()
    print(a1.stats())
    a1.heal()
    print(a1.stats())
    a1.heal()
    print(a1.stats())
    a1.heal()
    print(a1.stats())
    a1.heal()
    print(a1.stats())


if __name__ == "__main__":
    main()