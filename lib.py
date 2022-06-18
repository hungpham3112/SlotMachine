import random
from typing import Tuple
import os


##############################
######### Save game ##########
##############################
def save_money(money):
    with open("saved_money.txt", "w") as f:
        f.write(money)


def read_money(file):
    with open(file, "r") as f:
        return f.read() if not isempty(file) else "10"


##############################
########## Engine ############
##############################
def random_digit() -> int:
    return random.randint(1, 9)


def three_number() -> Tuple[int, int, int]:
    return (random_digit(), random_digit(), random_digit())


def two_similar_digits_money(_three_number: Tuple[int, int, int]) -> bool:
    return len(set(_three_number)) == 2


def three_similar_digits_money(_three_number: Tuple[int, int, int]) -> bool:
    return len(set(_three_number)) == 1


def calc_money(_three_number, current_money):
    if two_similar_digits_money(_three_number):
        print("You won 50 cents.")
        return current_money + 0.25
    if three_similar_digits_money(_three_number):
        print("Bingo!!! You earned $10.00 dollars.")
        return current_money + 9.75
    if current_money == 0:
        print("you run out of money!!! game over :(")
    else:
        print("sorry you didn't earn anything :(")
        return current_money - 0.25


def engine(current_money=10.0):
    # Instruction
    while current_money != 0:
        user_input = input(
            """
Choose one of the following menu options:
1) Play the slot machine.
2) Save game.
3) Cash out.
"""
        ).strip()
        magic_number = three_number()

        if user_input == "3":
            save_money(str(current_money))
            print(f"Thank you for playing! You end with ${current_money}")
            break
        if user_input == "2":
            save_money(str(current_money))
            clear()
            print("Your money had saved!")
        if user_input == "1":
            clear()
            print(f"Your magic number is {''.join(map(str, magic_number))}")
            current_money = calc_money(magic_number, current_money=current_money)
            print(f"current_money is {current_money}")
            continue
        else:
            continue


##############################
########### Utils ############
##############################
def clear():
    return os.system("cls")


def isempty(file):
    return os.stat(file).st_size == 0


def instruction(current_money=10.0):
    return f"""
---------------------------------------------------------------------------
| You start with ${current_money:<19}                                     |
| Each play costs 25 cents.                                               |
| For each play, the slot machine will output a random three-digit number.|
| If have two similar numbers, you will earn 50 cents.                    |
| If have three similar numbers, you will earn $10.                       |
---------------------------------------------------------------------------
"""
