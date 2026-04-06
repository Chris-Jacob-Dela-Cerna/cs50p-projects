
name = input("Enter name: ")
age = input("Enter age: ")
height = input("Enter height: ")
birthday = input("Enter birthday: ")

person = {
    "Name": name,
    "Age": age,
    "Height": height,
    "Birthday": birthday
}

indicator =f"""
    Name: {person.get("Name")}
    Age: {person.get("Age")}
    Height: {person.get("Height")}
    Birthday: {person.get("Birthday")}
"""

print(indicator)




def main():
    a, b, c, d = input("Enter a 4 numbers with a space in between: ").split(" ")
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    print(calculate(a, b, c, d))

def calculate(w, x, y, z):
    return (w + x) - (y + z)