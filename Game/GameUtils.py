import random
# from Box import Box


def roll_die(num_sides, num_dice):
    while True:
        yield sum(random.randint(1, num_sides) for i in range(num_dice))


def at_least_one_exists(possibilities, pieces):
    return any(i in pieces for i in possibilities)


def ask_numbers_to_remove():
    numbers_string = input(
        "input the numbers you would like to remove (separate by spaces) or type \'end\' to end the game: ")
    if numbers_string.lower() == 'end':
        return 'end'
    numbers_s_list = numbers_string.split()
    numbers = []
    for n in numbers_s_list:
        numbers.append(int(n))

    numbers.sort()
    return numbers
