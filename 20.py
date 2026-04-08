
fruits = []

print("\nWelcome user.")
while True:
    userfruit = input("\nEnter a fruit or enter 'next': ").strip().lower()
    if userfruit == "next":
        break
    else:
        fruits.append(userfruit)

print(f"\nFruits: {", ".join(fruits)}.")

print(f"\n{fruits[1][0:3]}")

print(f"{fruits[1][-2:]}")