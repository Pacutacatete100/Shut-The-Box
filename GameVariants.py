from GameUtils import *
from Box import Box


def play():
    box = Box([])
    playing = True

    while playing:
        box.print_remaining_pieces()
        roll = roll_die(box.find_max_piece())
        print('\nYou rolled: ' + str(roll))
        if not box.combination_not_possible(roll):
            choices = ask_numbers_to_remove()
            box.remove_pieces(choices)
        elif box.combination_not_possible(roll):
            print('Sorry! you\'re all out of luck! Final score is: ' +
                  str(sum(box.pieces)))
            playing = False
