import random


def roll_2_dice():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)

    return num1 + num2


def roll_die():
    return random.randint(1, 6)
