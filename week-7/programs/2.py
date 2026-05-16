

import re


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