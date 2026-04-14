# Document: This python is my last application of CS50P Week 3.


def main():
    intro()
    cargo_inventory()
    canteen()
    # fuel_management()
    # shipment_audit()

def intro():
    print("\n | You are managing a shipping hub in Metro Manila that sends Balikbayan boxes to various provinces.\n | You must manage the inventory of items being packed, the fuel for the delivery trucks, and the schedule of shipments.")

onhand = []

def cargo_inventory():
    print("\n | You head to the packing station. You are tasked to pack items inside a Balikbayan Box.")
    print("\nSystem:   Enter the name of the items 1 by 1.\n          Enter 'ctrl-z' to finish packing items.")
    while True:
        try:    
            useritem = input("User:     ").strip().lower()
        except EOFError:
            pack_items()
            break
        else:
            onhand.append(useritem)

def pack_items():
    onhand.sort()
    box = {}
    for eachitem in onhand:
        if not eachitem in box:
            box.update({eachitem: 1})
        else:
            box[eachitem] +=1
    list(box.keys())
    total = 0
    print("\n <<< Balikbayan Box >>>")
    for eachitem in box.keys():
        print(f" | {box[eachitem]} - {eachitem.upper()}")
        total += box[eachitem]
    print(f" = {total} total items")

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
    print("\nVendor:   Hello user. Interested in some snacks?\n          Enter 'menu' to see the list of snacks.\n          Enter the name of the snack to add to your order.\n          Enter 'ctrl-z' to pay or leave.")
    while True:
        try:
            usersnack = input("User:     ").strip().lower()
        except EOFError:
            receipt()
        else:
            if usersnack == "menu":
                print("\n <<< List of Snacks >>>")
                for eachsnack in snacks:
                    print(f" | {eachsnack.title()} - {snacks[eachsnack].get("price")} pesos")
                print()
            else:
                check_snack(usersnack)

def receipt():
    pass

def check_snack(snack):
    if snack in snacks:
        if not snack in order:
            order.update({snack: {"quantity": 1}})
        else:
            order[snack]["quantity"] += 1
        order_price()
    else:
        print("Vendor:   Oops, we don't have that at the moment.")

def order_price():
    price = 0
    for eachsnack in order:
        price += order[eachsnack].get("quantity") * snacks[eachsnack].get("price") 
    print(f"Total:    {price} pesos")


def fuel_management():
    pass



def shipment_audit():
    pass



main()