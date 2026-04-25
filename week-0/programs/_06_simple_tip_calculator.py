# Document: This python is my 6th application of CS50P Week 0.

# Calculates inc and total, returns the value
def calculate(cart, tip):
    inc = tip / 100 * cart
    total = cart + inc
    return inc, total

# Defines cart and tip
print ()
cart = float(input("How much are your items? "))
tip = float(input("How much are you willing to tip? "))

# Defines inc and total
inc, total = calculate(cart, tip)

# Sends results to user
print()
print("Total tip:", round(inc, 3))
print("Total amount due:", round(total, 3))

print()




# Versus




def calculate(cart, tip):
    inc = tip / 100 * cart
    total = cart + inc

print()
cart = float(input("How much are your items? "))
tip = float(input("How much are you willing to tip? "))
calculate(cart, tip)

print()
print("Total tip:", round(inc, 3))
print("Total amount due:", round(total, 3))

print()