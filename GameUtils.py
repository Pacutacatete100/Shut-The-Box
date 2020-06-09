import random
from Box import Box


def roll_die(num_sides, num_dice):
    roll_total = 0

    for _ in range(num_dice):
        roll_total += random.randint(1, num_sides)

    return roll_total


def ask_numbers_to_remove():
    numbers_string = input(
        "input the numbers you would like to remove (separate by spaces)")
    numbers_s_list = numbers_string.split()
    numbers = []
    for n in numbers_s_list:
        numbers.append(int(n))

    numbers.sort()
    return numbers
