# Week 9 scratch file

def main():
    x = int(input("x: ").strip())
    oss = add(x)
    for y in oss:
        print(y)


def add(x):
    for y in range(x):
        yield "0" * (y + 1)


if __name__ == "__main__":
    main()