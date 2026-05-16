

import re


while True:
    user = input("Enter a 5-digit number: ").strip()

    if re.search(r"^[1234567890]{5}$", user):
        print("Valid")
        break
    else:
        print("Invalid")

while True:
    user = input("Enter a 3 or 4-digit number: ").strip()

    if re.search(r"^[1234567890]{3,4}$", user):
        print("Valid")
        break
    else:
        print("Invalid")

while True:
    number = input("Enter your phone number: ").strip()

    if re.search(r"^[0123456789]{4}-[0123456789]{3}-[0123456789]{4}$", number):
        print("Valid")
        break
    else:
        print("Invalid")

while True:
    email = input("Enter your email: ").strip()

    if re.search(r"^[^@]+@gmail\.com$", email):
        print("Valid")
    else:
        print("Invalid")