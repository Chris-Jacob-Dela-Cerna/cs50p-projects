# Document: This python is my 1st application of CS50P Week 4.

import random


def main():
    print("\nSystem:   Would you like to guess a number or a fruit? Enter 1 or 2.\n          Enter 'ctrl-z' to leave.")
    while True:
        try:
            whichgame = input("User:     ").strip().lower()
        except EOFError:
            print("System:   Thank you for playing!")
            break
        else:
            if whichgame == "1":
                game = numbers
                userguess = get_number()
            elif whichgame == "2":
                game = fruits
                userguess = get_fruit()
            else:
                print("System:   Invalid. Please try again.")
                continue
            guess(game, userguess)
            break


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fruits = ["Apple", "Banana", "Orange", "Grapes", "Strawberry", "Pineapple", "Mango", "Watermelon", "Blueberry", "Peach"]


def get_number():
    print("\nSystem:   Guess a number from 1-10.")
    while True:
        try:
            userguess = int(input("User:     ").strip())
        except ValueError:
            print("System:   Invalid. Please enter a valid number.")
        else:
            if userguess in numbers:
                return userguess
            else:
                print("System:   Invalid. Please enter a number from 1-10.")


def get_fruit():
    print("\nSystem:   Guess a fruit from the following fruits below:")
    for eachfruit in fruits:
        print(f" | {eachfruit.title()}")
    while True:
        userguess = input("User:     ").strip().title()
        if userguess in fruits:
            return userguess
        else:
            print("System:   Invalid. Please enter a valid fruit.")


def guess(game, userguess):
    correct = random.choice(game)
    print(f"System:   The answer was {correct.lower()}.", end=" ")
    if userguess == correct:
        print("You won, congratulations!\n")
    else:
        print("You lost, better luck next time!\n")


main()