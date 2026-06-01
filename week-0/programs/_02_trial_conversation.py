# Document: This python is my 2nd application of CS50P Week 0

# Greets the user and asks their full name
print("Greetings! I am Cybercop 1101 and I am tasked to investigate you.")
name = input("First off, what's your full name? ").title().strip()
first, second, last, last2 = name.split(" ")

# Interrogates the user's last name
print(f"Okay {first}, from your name it indicates that you are part of the {last} {last2} clan."), print(f"The {last} {last2} clan has records of tyrannus behavior among QC citizens. Care to explain your relation to these recent occurences? ")