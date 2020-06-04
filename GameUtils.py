import random
from Box import Box


def roll_die(max_piece):
    if max_piece <= 6:
        return random.randint(1, 6)
    if max_piece > 6:
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)

        return num1 + num2


def ask_numbers_to_remove():
    numbers_string = input(
        "input the numbers you would like to remove (separate by spaces)")
    numbers_s_list = numbers_string.split()
    numbers = []
    for n in numbers_s_list:
        numbers.append(int(n))

    numbers.sort()
    return numbers

