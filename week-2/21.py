# Document: This python is my last application of CS50P Week 2.

def transit_id(id):
    if len(id) >= 2 and len(id) <= 6:
        print("Correct")
    else:
        if_s = ""
        if len(id) > 1:
            if_s = "s"
        print(f"Invalid. User entered {len(id)} character{if_s}.")
        return False


def registration():
    print("\nWelcome user.")
    while True:
        userid = input("\nEnter your 2-6 character Transit ID.\nUser: ")
        if transit_id(userid) == True:
            break


def main():
    registration()


main()