# Document: This python is my 5th application of CS50P Week 1.

def greet():
    print()
    print("System: I, the Great Question of Life, the Universe, and Everything.")
    response = input("User: ").strip().lower()
    return response

def check_greet(response):
    if response.startswith("hello"):
        print("System: Welcome! Your entrance fee is $0.")
    elif response.startswith("h"):
        print("System: Welcome! Your entrance fee is $20.")
    elif response == "42" or response == "forty-two" or response == "forty two":
        print("System: Ah, the meaning of life. Welcome!")
    else:
        print("System: Welcome! Your entrance fee is $100.")

def convert_time():
    user_time = input("User: ").strip()
    hour, minute = user_time.split(":")
    fixed_time = (f"{int(hour)}.{round(int(minute) / 6)}")
    time = float(fixed_time)
    return user_time, time

def resto():
    print()
    print("Resto Owner: Greetings user! Welcome to the Space Resto!\n             May I ask what time it is? In military '##:##'.")
    user_time, time = convert_time()

    if 7.0 <= time <= 8.0:
        print(f"Resto Owner: Wait, it's {user_time}? Well I suggest you order our special meal just for this morning!")
        print("             Our Space Omelet with a side of guacamole.")
    elif 12.0 <= time <= 13.0:
        print(f"Resto Owner: Wait, it's {user_time}? Well I suggest you order our hottest meal just for this afternoon!")
        print("             Our Asteroid Burger with a cup of Juga Cola.")
    elif 18.0 <= time <= 19.0:
        print(f"Resto Owner: Wait, it's {user_time}? Well I suggest you order our scrumptious meal just for this evening!")
        print("             Our Quantum Steak with a bucket of gravy.")
    else:
        print(f"Resto Owner: {user_time}? Well that's off our kitchen hours. Even then, I suggest you order our coldest drink.")
        print("             Our Pan-Galactic Gargle Blaster!")

    print()
    response1 = input("Resto Owner: Are you interested? (y or n). ")
    if not response1 == "y":
        raise SystemExit







def main():
    response = greet()
    check_greet(response)
    resto()


main()