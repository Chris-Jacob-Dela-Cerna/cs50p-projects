# Document: This python is my 2nd application of CS50P Week 4.

import sys
import random


if len(sys.argv) != 2:
    sys.exit(f"System:   Invalid. Please enter either red or blue.\n          >>> python {sys.argv[0]} [input] <<<")

colors = ["red", "blue"]

print(f"System:   User entered '{sys.argv[1]}'.")
win = random.choice(colors)
if sys.argv[1].lower() == win:
    print("System:   You win!", end=" ")
else:
    print("System:   You lost!", end=" ")
print(f"The answer was {win}.")