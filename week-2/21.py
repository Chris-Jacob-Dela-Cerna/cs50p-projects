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
    if name.isalpha():
        newname = name.lower().replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace(".", "")
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
        username = input("\nSystem:   Enter your full name to receive a Commuter Tag.\nUser:     ").strip()
        print("System:   Processing username...")
        if commuter_tag(username):
            break



stations = [
    {"stationid": "recto", "name": "Recto"}, 
    {"stationid": "legarda", "name": "Legarda"}, 
    {"stationid": "pureza", "name": "Pureza"}, 
    {"stationid": "vmapa", "name": "V. Mapa"}, 
    {"stationid": "jruiz", "name": "Gilmore"},
    {"stationid": "bettygo", "name": "Betty Go-Belmonte"},
    {"stationid": "anonas", "name": "Anonas"},
    {"stationid": "katipunan", "name": "Katipunan"},
    {"stationid": "santolan", "name": "Santolan"},
    {"stationid": "marikina", "name": "Marikina-Pasig"},
    {"stationid": "antipolo", "name": "Antipolo"}
]

def station(station):
    print("System:   Processing text...")
    if station.endswith("Station"):
        print("System:   Processing Station IDs...")
        for eachstation in range(len(stations)):
            if station[:-7] == stations[eachstation]['stationid']:
                print(f"System:   {stations[eachstation]['name']} Station selected.")
                return True
        print("System:   Invalid. Choose a correct Station ID.")
        return False
    else:
        print("System:   Invalid. Must end with -Station.")
        return False



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
                print(f"{eachstation + 1}. {stations[eachstation]['stationid']} - {stations[eachstation]['name']} Station")



def main():
    # Temporarily remove registration()
    ticket_kiosk()

main()