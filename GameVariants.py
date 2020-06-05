from GameUtils import *
from Box import Box


def play_base_game():
    box = Box([1, 2, 3, 4, 5, 6, 7, 8, 9])
    playing = True

    while playing:
        box.print_remaining_pieces()
        roll = roll_die(box.find_max_piece())
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if sum(choices) == roll:
                box.remove_pieces(choices)
                if len(choices) == 0:
                    print('YOU WIN')
                    playing = False
            elif sum(choices) != roll:
                print('doesnt add up')
        elif box.combination_not_possible(roll):
            print('Sorry! you\'re all out of luck! Final score is: ' +
                  str(sum(box.pieces)))
            playing = False


def two_to_go():
    box = Box([1, 3, 4, 5, 6, 7, 8, 9])
    playing = True

    print('2 to go: the 2 is automatically removed, if you roll 4 on your first roll, you lose the game')

    roll = roll_die(box.find_max_piece())
    if roll == 4:
        print('Sorry! you\'re all out of luck! Final score is: ' +
              str(sum(box.pieces)))
        return

    while playing:
        box.print_remaining_pieces()
        roll = roll_die(box.find_max_piece())
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if sum(choices) == roll:
                box.remove_pieces(choices)
                if len(choices) == 0:
                    print('YOU WIN')
                    playing = False
            elif sum(choices) != roll:
                print('doesnt add up')
        elif box.combination_not_possible(roll):
            print('Sorry! you\'re all out of luck! Final score is: ' +
                  str(sum(box.pieces)))
            playing = False


def three_to_go():
    box = Box([1, 2, 4, 5, 6, 7, 8, 9])
    playing = True

    print('3 to go: the 3 is automatically removed, if you roll 4 on your first roll, you lose the game')

    roll = roll_die(box.find_max_piece())
    if roll == 4:
        print('Sorry! you\'re all out of luck! Final score is: ' +
              str(sum(box.pieces)))
        return

    while playing:
        box.print_remaining_pieces()
        roll = roll_die(box.find_max_piece())
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if sum(choices) == roll:
                box.remove_pieces(choices)
                if len(choices) == 0:
                    print('YOU WIN')
                    playing = False
            elif sum(choices) != roll:
                print('doesnt add up')
        elif box.combination_not_possible(roll):
            print('Sorry! you\'re all out of luck! Final score is: ' +
                  str(sum(box.pieces)))
            playing = False


def three_down_extreme():
    box = Box([4, 5, 6, 7, 8, 9])
    playing = True

    print('numbers 1, 2 and 3 are pre-dropped, leaving numbers 4 to 9 up')

    while playing:
        box.print_remaining_pieces()
        roll = roll_die(box.find_max_piece())
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if sum(choices) == roll:
                box.remove_pieces(choices)
                if len(choices) == 0:
                    print('YOU WIN')
                    playing = False
            elif sum(choices) != roll:
                print('doesnt add up')
        elif box.combination_not_possible(roll):
            print('Sorry! you\'re all out of luck! Final score is: ' +
                  str(sum(box.pieces)))
            playing = False


def against_all_odds():
    box = Box([1, 3, 5, 7, 9])
    playing = True

    print('only odd numbers are up')

    while playing:
        box.print_remaining_pieces()
        roll = roll_die(box.find_max_piece())
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if sum(choices) == roll:
                box.remove_pieces(choices)
                if len(choices) == 0:
                    print('YOU WIN')
                    playing = False
            elif sum(choices) != roll:
                print('doesnt add up')
        elif box.combination_not_possible(roll):
            print('Sorry! you\'re all out of luck! Final score is: ' +
                  str(sum(box.pieces)))
            playing = False


def even_stevens():
    box = Box([2, 4, 6, 8])
    playing = True

    print('only even numbers are up')

    while playing:
        box.print_remaining_pieces()
        roll = roll_die(box.find_max_piece())
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if sum(choices) == roll:
                box.remove_pieces(choices)
                if len(choices) == 0:
                    print('YOU WIN')
                    playing = False
            elif sum(choices) != roll:
                print('doesnt add up')
        elif box.combination_not_possible(roll):
            print('Sorry! you\'re all out of luck! Final score is: ' +
                  str(sum(box.pieces)))
            playing = False


def full_house():
    box = Box([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    playing = True

    print('12 numbers are up')

    while playing:
        box.print_remaining_pieces()
        roll = roll_die(box.find_max_piece())
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            if sum(choices) == roll:
                box.remove_pieces(choices)
                if len(choices) == 0:
                    print('YOU WIN')
                    playing = False
            elif sum(choices) != roll:
                print('doesnt add up')
        elif box.combination_not_possible(roll):
            print('Sorry! you\'re all out of luck! Final score is: ' +
                  str(sum(box.pieces)))
            playing = False
