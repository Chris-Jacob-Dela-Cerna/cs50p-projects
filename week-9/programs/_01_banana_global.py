# Document: This python is my 1st application of CS50P Week 9.

def main():
    global banana
    banana = 1
    print(f"Tommie has {banana} banana.")
    while True:
        print("Do you want to give him 1 more banana? Enter y or n")
        resp: str = input(">>> ").strip()
        if resp != "y":
            break
        add_banana()
        print(f"Tommie now has {banana: int} bananas.")


def add_banana() -> None:
    global banana
    banana += 1
    print("You gave him 1 banana.\n")


if __name__ == "__main__":
    main()