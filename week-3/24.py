# Document: This python is my last application of CS50P Week 3.


def main():
    # intro()
    cargo_inventory()
    # canteen()
    # fuel_management()
    # shipment_audit()

def intro():
    print("\nContext: You are managing a shipping hub in Metro Manila that sends Balikbayan boxes to various provinces.\nYou must manage the inventory of items being packed, the fuel for the delivery trucks, and the schedule of shipments.")



def cargo_inventory():
    print("\nYou head to the packing station. You are tasked to pack items inside a Balikbayan Box.")
    while True:
        try:    
            useritem = input("System:   Enter the name of the items 1 by 1.\n          Enter ctrl-z to finish packing items.").strip()
        except EOFError:
            inventory()
            break
        else:
            insert_item()

def inventory():
    pass

def insert_item():
    pass



def canteen():
    pass



def fuel_management():
    pass



def shipment_audit():
    pass



main()