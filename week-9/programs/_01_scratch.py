


def main():
    global banana
    banana = 1
    while True:
        if banana == 1:
            print(f"Tommie has {banana} banana.")
        else:
            print(f"Tommie has {banana} bananas.")
        print("Do you want to give him 1 more banana? Enter y or n")
        resp = input(">>> ").strip()
        if resp == "y":
            add_banana()
        else:
            break


def add_banana():
    global banana
    banana += 1
    print("You gave him 1 banana.")


if __name__ == "__main__":
    main()