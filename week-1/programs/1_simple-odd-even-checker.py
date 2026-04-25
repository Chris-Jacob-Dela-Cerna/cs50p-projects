# Document: This python is my 1st application of CS50P Week 1.

# Grabs "n" from main()
def even(n):
# Checks if n is divisible by 2 then returns the result to main ()
    return n % 2 == 0

def main():
# Prompts user for an integer then stores in "n"
    n = int(input("What's x? "))
# Runs even()
    if even(n) == True:
        print("Even")
    else:
        print("Odd")

main()