# Document: This python is my 5th application of CS50P Week 0.

# Store user's name
print()
name = input("Enter your name: ").strip().title()

# Greets user
def greet(name):
    print()
    print(f"Greetings {name}.")
    insert()

# Let user insert data
def insert():
    print("Please provide the following information: ")
    subj = input("Subject: ").strip().title()
    thour = float(input("Hours needed: "))
    ddue = float(input("Days until due: "))
    hrperday = round(thour / ddue, 2)
    minperday = round(hrperday * 60, 2)
    summary(subj, thour, ddue, hrperday, minperday)

# Provide a summary
def summary(name, subj, thour, ddue, hrperday, minperday):
    print()
    print(f"Name: {name} ")
    print(f"Subject: {subj}")
    print(f"Total hours needed: {thour} ")
    print(f"Days left: {ddue}")
    print()
    print(f"You must study {hrperday} hours or {minperday} minutes per day. ")
    print()

# Starts program
def main():
    greet(name)

main()