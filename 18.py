


person = {
    "Name": "name",
    "Age": "age",
    "Height": "height",
    "Birthday": "birthday"
}

indicator =f"""
    Name: {person.get("Name")}
    Age: {person.get("Age")}
    Height: {person.get("Height")}
    Birthday: {person.get("Birthday")}
"""

print(indicator)
