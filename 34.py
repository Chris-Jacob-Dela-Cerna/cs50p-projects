
fruits = []
for number in range(3):
    user_fruit = input("\nFruit: ")
    user_color = input("Color: ")
    fruits.append({"fruit": user_fruit, "color": user_color})

for fruit in sorted(fruits, key=lambda item: item['fruit']):
    print(fruit["fruit"])