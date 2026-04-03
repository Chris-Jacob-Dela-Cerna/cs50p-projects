# Document: This python is my 5th application of CS50P Week 1.



def greet():
    print()
    print("System: I, the Great Question of Life, the Universe, and Everything")
    response = input("User: ").strip().lower()
    pass
    return response

def check_greet(response):
    if response.startswith("hello"):
        print("System: Welcome! Your cover fee is $0")
    elif response.startswith("h"):
        print("System: Welcome! Your cover fee is $20")
    elif response == "42" or response == "forty-two" or response == "forty two":
        print("System: Ah, the meaning of life. Welcome!")
    else:
        print("System: Welcome! Your cover fee is $100")
    pass

def menu():
    print("Resto Owner: Greetings user! Welcome to the Space Resto!\n             May I ask what time it currently is? ")
    user_time = input("User: ").replace(":", ".")
    time = float(user_time)

    if 7 <= time >= 8:
        print(f"Resto Owner: It's {time}? Well I suggest you order our special meal just for this morning!")
        print("             Our Space Omelet with a side of guacamole")
    else:
        print("BALLER ")









def main():
    response = greet()
    check_greet(response)
    menu()

main()