# Week 9 scratch file

def main():
    guys = [
        {"name": "Jacob", "strength": "high"},
        {"name": "Chris", "strength": "high"},
        {"name": "John", "strength": "medium"},
        {"name": "Doe", "strength": "low"},
        {"name": "Pratt", "strength": "low"},
    ]
    strongmen = filter(high, guys)
    for man in sorted(strongmen, key=lambda x: x["name"]):
        print(man)


def high(list_):
    return list_["strength"] == "high"


if __name__ == "__main__":
    main()