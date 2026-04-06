
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
