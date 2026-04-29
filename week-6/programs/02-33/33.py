# Document: This python is my 2nd application of CS50P Week 6.

while True:
    try:
        with open("subject_data.txt") as data:
            print(data.readlines()[0])
        break
    except FileNotFoundError:
        with open("subject_data.txt", "w") as data:
            data.write("yes file")