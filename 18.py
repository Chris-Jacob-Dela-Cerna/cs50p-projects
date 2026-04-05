

def user_input():
    while True:
        number = int(input("Give me a number: "))
        if number > 0:
            break
        print("Please enter a natural number.")
    return number

def output(n):
    for _ in range(n):
        print(f"This is said {n} amount of times.")
    

def number_breaker():
    number = user_input()
    output(number) 