# OOP scratch file 2 - practicing classes and objects

class Horse:
    health = 10
    attack = 3
    defence = 2
    min_movement = 1
    horse_types = {
        "fast": {"max_movement": 3},
        "slow": {"max_movement": 2},
    }

    def __init__(self, horse_type):
        self.type = horse_type

    @property
    def horse_type(self):
        return self._horse_type

    @horse_type.setter
    def horse_type(self, horse_type):
        if horse_type not in Horse.horse_types:
            raise ValueError("Invalid type.")
        self._horse_type = horse_type


horse1 = Horse("fast")