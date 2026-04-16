# Document: This python is my 1st application of CS50P Week 4.

import random



def main():
    print("System:   Would you like to guess a number or a fruit? Enter 1 or 2.\n          Enter 'ctrl-z' to leave.")
    while True:
        try:
            whichgame = input("User:     ").strip().lower()
        except EOFError:
            print("System:   Thank you for playing!")
            break
        else:
            if whichgame == "1":
                game = "number"
            elif whichgame == "2":
                game = "fruit"

def guess(game, userguess):
    pass

main()