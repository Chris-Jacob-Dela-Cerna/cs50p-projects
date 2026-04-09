# Document: This python is my last application of CS50P Week 2.

def transit_id(id):
    if len(id) >= 2 and len(id) <= 6:
        if id.isalnum():
            if check_id(id):
                print("Valid")
                return True
            
            else:
                return False
        else:
            print("Invalid. There must be no spaces or punctuation.")
            return False
    else:
        if_s = "s"
        if len(id) == 1:
            if_s = ""
        print(f"Invalid. User entered {len(id)} character{if_s}.")
        return False
    

def check_id(newid):
    if newid[:2].isalpha():
        return True
        
    else:
        print("Invalid. There must be atleast 2 letters.")
        return False

def registration():
    print("\nWelcome user.")
    while True:
        userid = input("\nEnter your 2-6 character Transit ID.\nUser: ")
        if transit_id(userid):
            break


def main():
    registration()


main()