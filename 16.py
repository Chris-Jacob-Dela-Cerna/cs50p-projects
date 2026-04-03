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

def resto_owner():
    user_time, time = convert_time()

    if 7.0 <= time <= 8.0:
        print(f"Resto Owner: Wait, it's {user_time}? Well I suggest you order our special meal just for this morning!")
        print("             Our Space Omelet with a side of guacamole.")
        return ("Space Omelet")
    elif 12.0 <= time <= 13.0:
        print(f"Resto Owner: Wait, it's {user_time}? Well I suggest you order our hottest meal just for this afternoon!")
        print("             Our Asteroid Burger with a cup of Juga Cola.")
        return ("Asteroid Burger")
    elif 18.0 <= time <= 19.0:
        print(f"Resto Owner: Wait, it's {user_time}? Well I suggest you order our scrumptious meal just for this evening!")
        print("             Our Quantum Steak with a bucket of gravy.")
        return ("Quantum Steak")
    else:
        print(f"Resto Owner: {user_time}? Well that's off our kitchen hours. Even then, I suggest you order our coldest drink.")
        print("             Our Pan-Galactic Gargle Blaster!")
        return ("Pan-Galactic Gargle Blaster")

def resto():
    print()
    print("Resto Owner: Greetings user! Welcome to the Space Resto!\n             May I ask what time it is? In military '##:##'.")
    x = resto_owner()

    response1 = input("Resto Owner: Are you interested? (yes or no). ").strip().lower()
    if not response1 == "yes":
        raise SystemExit
    
    print("System: Sounds great! You may proceed to the cashier to finalize your order.")
    process_order(x)

def process_order(x):
    print()
    order = x

    match order:
        case "Space Omelet":
            print(f"Resto Cashier: Good morning, user! The {order} promo is only $14.")
        case "Asteroid Burger":
            print(f"Resto Cashier: Good afternoon, user! The {order} meal is only $19.")
        case "Quantum Steak":
            print(f"Resto Cashier: Good evening, user! The {order} dine is only $29.")
        case "Pan-Galactic Gargle Blaster":
            print(f"Resto Cashier: Good day, user! The {order} summer refresher is only $9.")





def main():
    response = greet()
    check_greet(response)
    resto()


main()