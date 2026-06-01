

from units import Warrior
from units import Archer
from units import Giant


def main():
    input("[Message - System] Press enter between pauses. ")
    show_greet()
    show_instructions()


def show_greet():
    input(
        "================="
        "\n Greetings, User "
        "\n================="
        "\n"
    )
    input(
        "=========================="
        "\n   Welcome to Battlopia!  "
        "\n A Text-based Battle Game "
        "\n=========================="
        "\n"
    )


def show_instructions():
    input(
        "Note: This game requires 2 players."
        "\n      Each player must select 3 units for their deck."
        "\n      The player with the last remaining units wins."
        "\n"
    )


if __name__ == "__main__":
    main()