import random
import itertools
from Box import Box
from GameUtils import *
from GameVariants import *

if __name__ == "__main__":
    # print('1. Normal Game')
    # print('2. 2 To Go: the 2 is automatically removed, if you roll 4 on your first roll, you lose the game')
    # print('3. 3 To To: the 3 is automatically removed, if you roll 4 on your first roll, you lose the game')
    # print('4. 3 Down Extreme: numbers 1, 2 and 3 are pre-dropped, leaving numbers 4 to 9 up')
    # print('5. Against All Odds: only the odd numbers are up')
    # print('6. Even-Stevens: only the even numbers are up')
    # print('7. Full House: numbers 1 - 12 are up')

    # variant = input('chose what version of the game you want to play: ')

    # if int(variant) == 1:
    #     play_base_game()
    # elif int(variant) == 2:
    #     two_to_go()
    # elif int(variant) == 3:
    #     three_to_go()
    # elif int(variant) == 4:
    #     three_down_extreme()
    # elif int(variant) == 5:
    #     against_all_odds()
    # elif int(variant) == 6:
    #     even_stevens()
    # elif int(variant) == 7:
    #     full_house()
    play_base_game()
