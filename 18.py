
fruits = {
    "apple": {"name": "apple", "color": "red"},
    "banana": {"name": "banana", "color": "yellow"}
}

if fruits["apple"]["name"].startswith(("a", "e", "i", "o", "u")):
    a_an = "An"
else:
    a_an = "A"

print(f"{a_an} {fruits["apple"]["name"]} has the color {fruits["apple"]["color"]}.")

newfruit = input("Enter a fruit: ").strip().lower()
newcolor = input("Enter the color of that fruit: ").strip().lower()

fruits.update({newfruit: {"name": newfruit, "color": newcolor}})

if fruits[newfruit]["name"].startswith(("a", "e", "i", "o", "u")):
    a_an = "An"
else:
    a_an = "A"

print(f"{a_an} {fruits[newfruit]["name"]} has the color {fruits[newfruit]["color"]}.")