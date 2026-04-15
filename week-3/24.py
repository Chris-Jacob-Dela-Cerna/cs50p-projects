# Document: This python is my last application of CS50P Week 3.


def main():
    # intro()
    # cargo_inventory()
    # canteen()
    # fuel_management()
    shipment_audit()

def intro():
    print("\nContext:\nYou are managing a shipping hub in Metro Manila that sends Balikbayan boxes to various provinces.\nYou must manage the inventory of items being packed, the fuel for the delivery trucks, and the schedule of shipments.")



onhand = []
box = {}

def cargo_inventory():
    print("\n | You head to the packing station. You are tasked to pack items inside a Balikbayan Box.")
    print("\nSystem:   Enter the name of the items 1 by 1.\n          Enter 'ctrl-z' to finish packing items.")
    while True:
        try:    
            useritem = input("User:     ").strip().lower()
        except EOFError:
            sort_items()
            pack_items()
            break
        else:
            onhand.append(useritem)

def sort_items():
    onhand.sort()
    for eachitem in onhand:
        if not eachitem in box:
            box.update({eachitem: 1})
        else:
            box[eachitem] +=1

def pack_items():
    list(box.keys())
    total = 0
    print("\n <<< Balikbayan Box >>>")
    for eachitem in box.keys():
        print(f" | {box[eachitem]} - {eachitem.upper()}")
        total += box[eachitem]
    if total == 1:
        if_s = ""
    else:
        if_s = "s"
    print(f" = {total} total item{if_s}")



snacks = {
    "turon": {"price": 10.00},
    "siomai": {"price": 7.50},
    "banana cue": {"price": 15.00},
    "kwek-kwek": {"price": 5.00},
    "fish ball": {"price": 2.00},
    "kikiam": {"price": 2.50},
    "lumpia": {"price": 10.00},
    "taho": {"price": 20.00},
    "cheese stick": {"price": 2.00},
    "maruya": {"price": 15.00},
    "halo-halo": {"price": 40.00}
}
order = {}

def canteen():
    print("\n | You hear your stomach growl, you're hungry.\n | Thankfully it's breaktime so you head to the canteen.")
    print("\nVendor:   Hello user. Interested in some snacks?\n          Enter 'menu' to see the list of snacks.\n          Enter the name of the snack to add to your order.\n          Enter 'ctrl-z' to finalize your order.")
    while True:
        try:
            usersnack = input("User:     ").strip().lower()
        except EOFError:
            receipt()
            pay = input("\nVendor:   Is that all? Or do you want to add more items?\n          To pay and exit, enter 'yes'. Otherwise enter 'no'.\nUser:     ").strip().lower()
            if pay == "yes":
                print("Vendor:   Lovely! Thank you and have a nice day.")
                break
            else:
                print("Vendor:   Take your time user.")
        else:
            if usersnack == "menu":
                print("\n <<< List of Snacks >>>")
                for eachsnack in snacks:
                    print(f" | {eachsnack.title()} - {snacks[eachsnack].get("price")} pesos")
                print()
            else:
                check_snack(usersnack)

def receipt():
    print("\n <<< Order >>>")
    for eachorder in order:
        print(f" | {order[eachorder].get("quantity")} {eachorder.title()} = {order[eachorder].get("quantity") * snacks[eachorder].get("price")}")
    total = order_price()
    print(f" = {total} pesos total")

def check_snack(snack):
    if snack in snacks:
        if not snack in order:
            order.update({snack: {"quantity": 1}})
        else:
            order[snack]["quantity"] += 1
        total = order_price()
        print(f"Total:    {total} pesos")
    else:
        print("Vendor:   Oops, we don't have that at the moment.")

def order_price():
    total = 0
    for eachsnack in order:
        total += order[eachsnack].get("quantity") * snacks[eachsnack].get("price") 
    return total



def fuel_management():
    print("\n | It's time to go back to work.\n | The trucks are loaded with Balikbayan Boxes but before they leave you must check their fuel level.")
    print("\nSystem:   Enter the fuel level in fraction form.\n          Use this format: [remaining/capacity].")
    while True:
        userfuel = input("User:     ").strip()
        try:   
            left, tank = userfuel.split("/")
            left = float(left)
            tank = float(tank)
        except ValueError:
            print("System:   Invalid. Enter the fuel level in the right format.")
            continue
        else:
            if fuel_check(left, tank):
                break

def fuel_check(left, tank):
    if left <= tank:
        if left >= 0 and tank >= 0:
            try:
                level = left / tank
            except ZeroDivisionError:
                print("System:   Invalid. The tank's capacity can't be 0.")
                return False
            else:
                fuel_convert(level)
                return True
        else:
            print("System:   Invalid. Fuel can't be lower than 0.")
            return False
    else:
        print("System:   Invalid. Remaining fuel must be lower than the tank's capacity.")
        return False

def fuel_convert(level):
    fuelpercent = level * 100
    if fuelpercent >= 99:
        print("Fuel:     Full")
    elif fuelpercent <= 1:
        print("Fuel:     Empty")
    else:
        print(f"Fuel:     {round(fuelpercent, 2)}% full")
    if fuelpercent <= 30:
        print("\n | You refill the truck and send it off for delivery.")
    else:
        print("\n | The truck's fuel is set. You send it off for delivery.")



date1 = {
    1: {"month": "january", "days": 31},
    2: {"month": "febraury", "days": 28},
    3: {"month": "march", "days": 31},
    4: {"month": "april", "days": 30},
    5: {"month": "may", "days": 31},
    6: {"month": "june", "days": 30},
    7: {"month": "july", "days": 31},
    8: {"month": "august", "days": 31},
    9: {"month": "september", "days": 30},
    10: {"month": "october", "days": 31},
    11: {"month": "november", "days": 30},
    12: {"month": "december", "days": 31}
}

date2 = {
    "january": {"days": 31},
    "febraury": {"days": 28},
    "march": {"days": 31},
    "april": {"days": 30},
    "may": {"days": 31},
    "june": {"days": 30},
    "july": {"days": 31},
    "august": {"days": 31},
    "september": {"days": 30},
    "october": {"days": 31},
    "november": {"days": 30},
    "december": {"days": 31}
}

def shipment_audit():
    print(" | Your last task is to document the shipment's date of origin.")
    print("\nSystem:   Enter the date of shipment in either format:\n          [MM/DD/YYYY] or [Month, DD, YYYY]")
    while True:
        userdate = input("User:     ").strip()
        if userdate[0].isdigit():
            check_date(userdate)
        elif userdate[0].isalpha():
            check_date2(userdate)
                
def check_date(userdate):
    try:
        mm, dd, yyyy = userdate.split("/")
        mm = int(mm)
        dd = int(dd)
        yyyy = int(yyyy)
    except ValueError:
        print("System:   Invalid. Enter the date in the right format.")
    else:
        pass

def check_date2():
    print("Digit")



main()