# Document: This python is my last application of CS50P Week 2.

def transit_id(id):
    if len(id) >= 2 and len(id) <= 6:
        if id.isalnum():
            if check_id(id):
                return True
            else:
                return False
        else:
            print("System:   Invalid. There must be no spaces or punctuation.")
            return False
    else:
        if_s = "s"
        if len(id) == 1:
            if_s = ""
        print(f"System:   Invalid. User entered {len(id)} character{if_s}.")
        return False
    

def check_id(newid):
    if newid[:2].isalpha():
        alpha = 0
        for character in newid:
            if character.isalpha():
                alpha += 1
            elif character.isdigit():
                break
        for number in newid[alpha:]:
            if number.isalpha():
                print("System:   Invalid. After the last letter entered, there must only be succeeding numbers.")
                return False
        if alpha < 6 and alpha != len(newid):
            if newid[alpha] == "0":
                print("System:   Invalid. The first number must not be 0.")
                return False
        return True
    else:
        print("System:   Invalid. There must first be atleast 2 letters.")
        return False
    

def commuter_tag(name):
    if name.replace(" ", "A").isalpha():
        newname = name.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace(".", "").replace("A", "")
        print(f"System:   Commuter Tag [{newname.title()}] saved successfully.")
        return True
    else:
        print("System:   Invalid. There must only be letters.")
        return False


def registration():
    print("\nWelcome to LRT-2 Areneta Station.\nHead to the reception desk to register your ID.")
    while True:
        userid = input("\nSystem:   Enter your 2-6 character Transit ID.\nUser:     ")
        print("System:   Processing ID...")
        if transit_id(userid):
            print(f"System:   Transit ID [{userid}] saved successfully.")
            break
    while True:
        username = input("\nSystem:   Enter your full name to receive a Commuter Tag.\nUser:     ").strip().lower()
        print("System:   Processing username...")
        if commuter_tag(username):
            break

stations = [
    {"stationid": "recto_station", "name": "Recto", "price": 25}, 
    {"stationid": "legarda_station", "name": "Legarda", "price": 20}, 
    {"stationid": "pureza_station", "name": "Pureza", "price": 20}, 
    {"stationid": "vmapa_station", "name": "V. Mapa", "price": 20}, 
    {"stationid": "jruiz_station", "name": "J. Ruiz", "price": 15},
    {"stationid": "gilmore_station", "name": "Gilmore", "price": 15},
    {"stationid": "bettygo_station", "name": "Betty Go-Belmonte", "price": 15},
    {"stationid": "anonas_station", "name": "Anonas", "price": 15},
    {"stationid": "katipunan_station", "name": "Katipunan", "price": 15},
    {"stationid": "santolan_station", "name": "Santolan", "price": 15},
    {"stationid": "marikina_station", "name": "Marikina-Pasig", "price": 20},
    {"stationid": "antipolo_station", "name": "Antipolo", "price": 25}
]

def station(station):
    print("System:   Processing text...")
    if station.endswith("Station"):
        print("System:   Processing Station ID...")
        selected = [station[:-7], station[-7:].lower()]
        for eachstation in range(len(stations)):
            if ("_").join(selected) == stations[eachstation]["stationid"]:
                print(f"System:   {stations[eachstation]['name']} Station selected.")
                payment(eachstation)
                return True
        print("System:   Invalid. Choose a correct Station ID.")
        return False
    else:
        print("System:   Invalid. Must end with -Station.")
        return False
    
validcoins = [1, 5, 10, 20]

def payment(selected):
    price = stations[selected]["price"]
    print(f"\nSystem:   Your ticket fee is {price} pesos.\nSystem:   For payment, please insert inside the coin deposit the following coins: \n          1, 5, 10, 20")
    while True:
        coin = input("Deposit:  ").strip()
        if coin.isdigit():
            if int(coin) in validcoins:
                price -= int(coin)
                if not price > 0:
                    price *= -1
                    print(f"Status:   Paid\nChange:   {price} pesos")
                    return True
                else:
                    print(f"Status:   {price} pesos left")
            else:
                print("System:   Invalid. The coin deposit only accepts 1, 5, 10, 20 peso coins.")
        else:
            print("System:   Invalid. Enter numbers only.")
        

def ticket_kiosk():
    print("\nHead to a nearby ticket kiosk to select your destination.")
    while True:
        userstation = input("\nSystem:   Enter a station using this format: [stationidStation].\n          Enter 'stations' to see the list of available stations.\nUser:     ").strip()
        if userstation != "stations":  
            if station(userstation):
                break
        else:
            print("\nList of Stations IDs:")
            for eachstation in range(len(stations)):
                print(f"{eachstation + 1}. {stations[eachstation]['stationid'][:-8]} - {stations[eachstation]['name']} Station")

fruits = [
    {"fruit": "mango", "calories": 150},
    {"fruit": "banana", "calories": 105},
    {"fruit": "pineapple", "calories": 50},
    {"fruit": "papaya", "calories": 60},
    {"fruit": "guyabano", "calories": 66}
]

def check_fruit():
    print("\nVendor:   Good day! We have a few sorts of fruits.\n          This includes mangoes, bananas, pineapples, papayas, and guyabanos.\n          Any of them of interest to you?\n          If yes, enter the fruit in singular form. Otherwise, enter 'no'.")
    while True:
        user = input("User:     ").strip().lower()
        if user == "no":
            print("Vendor:   Thank you and have a safe trip!")
            break
        else:
            for eachfruit in range(len(fruits)):
                if user == fruits[eachfruit]['fruit']:
                    print(fruits[eachfruit])
                    match = True
                    break
            if match == True:
                break
            else:
                print("Vendor:   Looks like we don't have that at the moment.")


def fruit_stand():
    print("\nWhile waiting for the train you spot a fruit stand.")
    user = input("\nSystem:   Would you like to check their fruits? Enter yes or no.\nUser:     ").strip().lower()
    if user == "yes":
        check_fruit()

    print("\nYou wait for the train to arrive and then board safely.\n")


def main():
    # Tempremove registration()
    # Tempremove ticket_kiosk()
    fruit_stand()

main()