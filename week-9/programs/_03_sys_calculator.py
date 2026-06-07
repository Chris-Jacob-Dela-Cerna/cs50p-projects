

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--add", type=int, nargs=2, help="Add 2 integers")
parser.add_argument("--subtract", type=int, nargs=2, help="Subtract 2 integers")
parser.add_argument("--multiply", type=int, nargs=2, help="Multiply 2 integers")
parser.add_argument("--divide", type=int, nargs=2, help="Divide 2 integers")


def main():
    global args
    args = parser.parse_args()
    x = "Enter an operation."
    if args.add != None:
        x = addition()
    elif args.subtract != None:
        x = subtraction()
    elif args.multiply != None:
        x = multiplication()
    elif args.divide != None:
        x = division()
    print(x)


def addition():
    return args.add[0] + args.add[1]


def subtraction():
    return args.subtract[0] - args.subtract[1]


def multiplication():
    return args.multiply[0] * args.multiply[1]


def division():
    return args.divide[0] / args.divide[1]


if __name__ == "__main__":
    main()