

import argparse

parser = argparse.ArgumentParser()


def main():
    global args
    parser.add_argument("--add", type=int, nargs=2, help="Add 2 integers")
    parser.add_argument("--subtract", type=int, nargs=2, help="Subtract 2 integers")
    parser.add_argument("--multiply", type=int, nargs=2, help="Multiply 2 integers")
    parser.add_argument("--divide", type=int, nargs=2, help="Divide 2 integers")
    args = parser.parse_args()


def addition():
    print("add")


def subtraction():
    print("subtract")


def multiply():
    print("multiply")


def divide():
    print("divide")


if __name__ == "__main__":
    main()