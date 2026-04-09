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
        for number in newid[alpha: ]:
            if number.isalpha():
                print("System:   Invalid. After the last letter entered, there must only be succeeding numbers.")
                return False
        if alpha < 6:
            if newid[alpha] == "0":
                print("System:   Invalid. The first number must not be 0.")
                return False
        return True
    else:
        print("System:   Invalid. There must first be atleast 2 letters.")
        return False


def registration():
    print("\nWelcome user.")
    while True:
        userid = input("\nSystem:   Enter your 2-6 character Transit ID.\nUser:   ")
        print("System:   Processing ID...")
        if transit_id(userid):
            print(f"System:   Transit ID saved successfully.")
            break


def main():
    registration()


main()