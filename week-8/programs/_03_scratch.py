# OOP scratch file 2 - practicing classes and objects

class Horse:
    health = 10
    attack = 3
    defence = 2
    min_movement = 1
    horse_types = {
        "Fast": {"max_movement": 3},
        "Slow": {"max_movement": 2},
    }

    def __init__(self, horse_type):
        self.horse_type = horse_type

    @property
    def horse_type(self):
        return self._horse_type

    @horse_type.setter
    def horse_type(self, horse_type):
        if horse_type not in Horse.horse_types:
            raise ValueError("Invalid type.")
        self._horse_type = horse_type
        self._max_movement = self.horse_types[horse_type]["max_movement"]

    @property
    def max_movement(self):
        return self._max_movement
    
    @classmethod
    def damage(cls, damage):
        cls.health -= damage

    @staticmethod
    def yell():
        print("Horse yelled.")


h1 = Horse("Slow")
print(h1.horse_type, "-", h1.max_movement)
h1.damage(3)
print(h1.horse_type, "-", h1.health)
h1.damage(3)
print(h1.horse_type, "-", h1.health)
h1.yell()