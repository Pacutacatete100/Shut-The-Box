from Game.Box import *
from Game.GameUtils import *


def play_base_game():
    box = Box([1, 2, 3, 4, 5, 6, 7, 8, 9])
    playing = True
    roll = 0
    change_roll = True

    while playing:
        box.print_remaining_pieces()
        if box.find_max_piece() > 6 and change_roll:
            roll_generator = roll_die(6, 2)
            roll = next(roll_generator)
            change_roll = True
        elif box.find_max_piece() <= 6 and change_roll:
            roll_generator = roll_die(6, 1)
            roll = next(roll_generator)
            change_roll = True
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if choices == 'end':
                print('You ended the game, final score is ' + box.final_score())
                playing = False
            elif not choices:
                change_roll = False
                print('Oops, Looks like you forgot to type a number')
            else:
                if sum(choices) == roll and all(elem in box.pieces for elem in choices):
                    box.remove_pieces(choices)
                    change_roll = True
                    if len(box.pieces) == 0:
                        print('YOU WIN')
                        playing = False
                elif sum(choices) != roll or any(elem not in box.pieces for elem in choices):
                    print('doesnt add up')
                    change_roll = False
        elif box.combination_not_possible(roll):
            box.loss_message()
            playing = False


def two_to_go():
    box = Box([1, 3, 4, 5, 6, 7, 8, 9])
    playing = True
    roll = 0
    change_roll = True

    print('2 to go: the 2 is automatically removed, if you roll 4 on your first roll, you lose the game')

    roll_generator = roll_die(6, 2)
    roll = next(roll_generator)
    if roll == 4:
        print('Sorry! you\'re all out of luck! Final score is: ' +
              box.final_score())
        return

    while playing:
        box.print_remaining_pieces()
        if box.find_max_piece() > 6 and change_roll:
            roll_generator = roll_die(6, 2)
            roll = next(roll_generator)
            change_roll = True
        elif box.find_max_piece() <= 6 and change_roll:
            roll_generator = roll_die(6, 1)
            roll = next(roll_generator)
            change_roll = True
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if choices == 'end':
                print('You ended the game, final score is ' + box.final_score())
                playing = False
            elif not choices:
                change_roll = False
                print('Oops, Looks like you forgot to type a number')
            else:
                if sum(choices) == roll and all(elem in box.pieces for elem in choices):
                    box.remove_pieces(choices)
                    change_roll = True
                    if len(box.pieces) == 0:
                        print('YOU WIN')
                        playing = False
                elif sum(choices) != roll or any(elem not in box.pieces for elem in choices):
                    print('doesnt add up')
                    change_roll = False
        elif box.combination_not_possible(roll):
            box.loss_message()
            playing = False


def three_to_go():
    box = Box([1, 2, 4, 5, 6, 7, 8, 9])
    playing = True
    roll = 0
    change_roll = True

    print('3 to go: the 3 is automatically removed, if you roll 4 on your first roll, you lose the game')

    roll_generator = roll_die(6, 2)
    roll = next(roll_generator)
    if roll == 4:
        print('Sorry! you\'re all out of luck! Final score is: ' +
              box.final_score())
        return

    while playing:
        box.print_remaining_pieces()
        if box.find_max_piece() > 6 and change_roll:
            roll_generator = roll_die(6, 2)
            roll = next(roll_generator)
            change_roll = True
        elif box.find_max_piece() <= 6 and change_roll:
            roll_generator = roll_die(6, 1)
            roll = next(roll_generator)
            change_roll = True
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if choices == 'end':
                print('You ended the game, final score is ' + box.final_score())
                playing = False
            elif not choices:
                change_roll = False
                print('Oops, Looks like you forgot to type a number')
            else:
                if sum(choices) == roll and all(elem in box.pieces for elem in choices):
                    box.remove_pieces(choices)
                    change_roll = True
                    if len(box.pieces) == 0:
                        print('YOU WIN')
                        playing = False
                elif sum(choices) != roll or any(elem not in box.pieces for elem in choices):
                    print('doesnt add up')
                    change_roll = False
        elif box.combination_not_possible(roll):
            box.loss_message()
            playing = False


def three_down_extreme():
    box = Box([4, 5, 6, 7, 8, 9])
    playing = True
    roll = 0
    change_roll = True

    print('numbers 1, 2 and 3 are pre-dropped, leaving numbers 4 to 9 up')

    while playing:
        box.print_remaining_pieces()
        if box.find_max_piece() > 6 and change_roll:
            roll_generator = roll_die(6, 2)
            roll = next(roll_generator)
            change_roll = True
        elif box.find_max_piece() <= 6 and change_roll:
            roll_generator = roll_die(6, 1)
            roll = next(roll_generator)
            change_roll = True
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if choices == 'end':
                print('You ended the game, final score is ' + box.final_score())
                playing = False
            elif not choices:
                change_roll = False
                print('Oops, Looks like you forgot to type a number')
            else:
                if sum(choices) == roll and all(elem in box.pieces for elem in choices):
                    box.remove_pieces(choices)
                    change_roll = True
                    if len(box.pieces) == 0:
                        print('YOU WIN')
                        playing = False
                elif sum(choices) != roll or any(elem not in box.pieces for elem in choices):
                    print('doesnt add up')
                    change_roll = False
        elif box.combination_not_possible(roll):
            box.loss_message()
            playing = False


def against_all_odds():
    box = Box([1, 3, 5, 7, 9])
    playing = True
    roll = 0
    change_roll = True

    print('only odd numbers are up')

    while playing:
        box.print_remaining_pieces()
        if box.find_max_piece() > 6 and change_roll:
            roll_generator = roll_die(6, 2)
            roll = next(roll_generator)
            change_roll = True
        elif box.find_max_piece() <= 6 and change_roll:
            roll_generator = roll_die(6, 1)
            roll = next(roll_generator)
            change_roll = True
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if choices == 'end':
                print('You ended the game, final score is ' + box.final_score())
                playing = False
            elif not choices:
                change_roll = False
                print('Oops, Looks like you forgot to type a number')
            else:
                if sum(choices) == roll and all(elem in box.pieces for elem in choices):
                    box.remove_pieces(choices)
                    change_roll = True
                    if len(box.pieces) == 0:
                        print('YOU WIN')
                        playing = False
                elif sum(choices) != roll or any(elem not in box.pieces for elem in choices):
                    print('doesnt add up')
                    change_roll = False
        elif box.combination_not_possible(roll):
            box.loss_message()
            playing = False


def even_stevens():
    box = Box([2, 4, 6, 8])
    playing = True
    roll = 0
    change_roll = True

    print('only even numbers are up')

    while playing:
        box.print_remaining_pieces()
        if box.find_max_piece() > 6 and change_roll:
            roll_generator = roll_die(6, 2)
            roll = next(roll_generator)
            change_roll = True
        elif box.find_max_piece() <= 6 and change_roll:
            roll_generator = roll_die(6, 1)
            roll = next(roll_generator)
            change_roll = True
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if choices == 'end':
                print('You ended the game, final score is ' + box.final_score())
                playing = False
            elif not choices:
                change_roll = False
                print('Oops, Looks like you forgot to type a number')
            else:
                if sum(choices) == roll and all(elem in box.pieces for elem in choices):
                    box.remove_pieces(choices)
                    change_roll = True
                    if len(box.pieces) == 0:
                        print('YOU WIN')
                        playing = False
                elif sum(choices) != roll or any(elem not in box.pieces for elem in choices):
                    print('doesnt add up')
                    change_roll = False
        elif box.combination_not_possible(roll):
            box.loss_message()
            playing = False


def full_house():
    box = Box([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    playing = True
    roll = 0
    change_roll = True

    print('12 numbers are up')

    while playing:
        box.print_remaining_pieces()
        if box.find_max_piece() > 6 and change_roll:
            roll_generator = roll_die(6, 2)
            roll = next(roll_generator)
            change_roll = True
        elif box.find_max_piece() <= 6 and change_roll:
            roll_generator = roll_die(6, 1)
            roll = next(roll_generator)
            change_roll = True
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if choices == 'end':
                print('You ended the game, final score is ' + box.final_score())
                playing = False
            elif not choices:
                change_roll = False
                print('Oops, Looks like you forgot to type a number')
            else:
                if sum(choices) == roll and all(elem in box.pieces for elem in choices):
                    box.remove_pieces(choices)
                    change_roll = True
                    if len(box.pieces) == 0:
                        print('YOU WIN')
                        playing = False
                elif sum(choices) != roll or any(elem not in box.pieces for elem in choices):
                    print('doesnt add up')
                    change_roll = False
        elif box.combination_not_possible(roll):
            box.loss_message()
            playing = False


def digital():
    box = Box([1, 2, 3, 4, 5, 6, 7, 8, 9])
    playing = True
    score = ''
    roll = 0
    change_roll = True

    while playing:
        box.print_remaining_pieces()
        if box.find_max_piece() > 6 and change_roll:
            roll_generator = roll_die(6, 2)
            roll = next(roll_generator)
            change_roll = True
        elif box.find_max_piece() <= 6 and change_roll:
            roll_generator = roll_die(6, 1)
            roll = next(roll_generator)
            change_roll = True
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if choices == 'end':
                for p in box.pieces:
                    score += str(p)
                print('You ended the game, final score is ' +
                      score)  # !!!!
                playing = False
            elif not choices:
                change_roll = False
                print('Oops, Looks like you forgot to type a number')
            else:
                if sum(choices) == roll and all(elem in box.pieces for elem in choices):
                    box.remove_pieces(choices)
                    change_roll = True
                    if len(box.pieces) == 0:
                        print('YOU WIN')
                        playing = False
                elif sum(choices) != roll or any(elem not in box.pieces for elem in choices):
                    print('doesnt add up')
                    change_roll = False
        elif box.combination_not_possible(roll):
            for p in box.pieces:
                score += str(p)
            print('Sorry! you\'re all out of luck! Final score is: ' + score)
            playing = False


def thai_style():
    box = Box([1, 2, 3, 4, 5, 6, 7, 8, 9])
    playing = True
    roll = 0
    change_roll = True

    print('you can only chose one of the numbers you rolled or their sum')

    while playing:

        if change_roll:
            box.print_remaining_pieces()
            roll_generator = roll_die(6, 1)
            roll1 = next(roll_generator)
            roll_generator = roll_die(6, 1)
            roll2 = next(roll_generator)

            total = roll1 + roll2

            possibilities = []

            possibilities.append(roll1)
            possibilities.append(roll2)
            possibilities.append(total)
            change_roll = True

        print('\nYou rolled a ' + str(roll1) + ' and a ' +
              str(roll2) + '. Total = ' + str(total))

        if at_least_one_exists(possibilities, box.pieces):
            choices = ask_numbers_to_remove()
            if choices == 'end':
                print('You ended the game, final score is ' + box.final_score())
                playing = False
            else:
                if sum(choices) == roll and all(elem in box.pieces for elem in choices):
                    box.remove_pieces(choices)
                    change_roll = True
                    if len(box.pieces) == 0:
                        print('YOU WIN')
                        playing = False
                elif sum(choices) != roll or any(elem not in box.pieces for elem in choices):
                    print('you cant chose that number')
                    change_roll = False
        elif not at_least_one_exists(possibilities, box.pieces):
            box.loss_message()
            playing = False


def the_300():
    box = Box([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
               14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
    playing = True
    roll = 0
    change_roll = True

    print('24 numbers to play with, 4 die (initially)')

    while playing:
        box.print_remaining_pieces()
        if 19 <= box.find_max_piece() <= 24 and change_roll:
            roll_generator = roll_die(6, 4)
            roll = next(roll_generator)
            change_roll = True
        if 13 <= box.find_max_piece() <= 18 and change_roll:
            roll_generator = roll_die(6, 3)
            roll = next(roll_generator)
            change_roll = True
        if 7 <= box.find_max_piece() <= 12 and change_roll:
            roll_generator = roll_die(6, 2)
            roll = next(roll_generator)
            change_roll = True
        if 1 <= box.find_max_piece() <= 6 and change_roll:
            roll_generator = roll_die(6, 1)
            roll = next(roll_generator)
            change_roll = True
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if choices == 'end':
                print('You ended the game, final score is ' + box.final_score())
                playing = False
            elif not choices:
                change_roll = False
                print('Oops, Looks like you forgot to type a number')
            else:
                if sum(choices) == roll and all(elem in box.pieces for elem in choices):
                    box.remove_pieces(choices)
                    change_roll = True
                    if len(box.pieces) == 0:
                        print('YOU WIN')
                        playing = False
                elif sum(choices) != roll or any(elem not in box.pieces for elem in choices):
                    print('doesnt add up')
                    change_roll = False
        elif box.combination_not_possible(roll):
            box.loss_message()
            playing = False


def twenty_twelve():
    box = Box([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    playing = True
    roll = 0
    change_roll = True

    print('20-sided die playing 12 numbers')

    while playing:
        box.print_remaining_pieces()
        if change_roll:
            roll_generator = roll_die(20, 1)
            roll = next(roll_generator)
            change_roll = True
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if choices == 'end':
                print('You ended the game, final score is ' + box.final_score())
                playing = False
            elif not choices:
                change_roll = False
                print('Oops, Looks like you forgot to type a number')
            else:
                if sum(choices) == roll and all(elem in box.pieces for elem in choices):
                    box.remove_pieces(choices)
                    change_roll = True
                    if len(box.pieces) == 0:
                        print('YOU WIN')
                        playing = False
                elif sum(choices) != roll or any(elem not in box.pieces for elem in choices):
                    print('doesnt add up')
                    change_roll = False
        elif box.combination_not_possible(roll):
            box.loss_message()
            playing = False
