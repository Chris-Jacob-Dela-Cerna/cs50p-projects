# Document: This python is my last application of CS50P Week 3.


def main():
    # intro()
    cargo_inventory()
    # canteen()
    # fuel_management()
    # shipment_audit()

def intro():
    print("\nContext: You are managing a shipping hub in Metro Manila that sends Balikbayan boxes to various provinces.\nYou must manage the inventory of items being packed, the fuel for the delivery trucks, and the schedule of shipments.")

onhand = []

def cargo_inventory():
    print("\nYou head to the packing station. You are tasked to pack items inside a Balikbayan Box.")
    print("\nSystem:   Enter the name of the items 1 by 1.\n          Enter ctrl-z to finish packing items.")
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
    print("\n ==================")
    list(box.keys())
    total = 0
    for eachitem in box.keys():
        print(f" | {box[eachitem]} - {eachitem.upper()}")
        total += box[eachitem]
    print(f" = {total} total items\n")



def canteen():
    pass



def fuel_management():
    pass



def shipment_audit():
    pass



main()