# OOP scratch file 2 - practicing classes and objects


class Horse:
    health = 5
    attack = 2
    defence = 2
    min_movement = 1
    max_movement = 2

    @classmethod
    def move(cls, movement):
        if movement < cls.min_movement:
            raise ValueError("Too small.")
        if movement > cls.max_movement:
            raise ValueError("Too big.")
        print(f"Horse has moved {movement} tiles.")

try:
    Horse.move(1)
except ValueError as ve:
    print(ve)

horse = Horse
try:
    horse.move(2)
except ValueError as ve:
    print(ve)