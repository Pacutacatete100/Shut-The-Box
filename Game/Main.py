from GameVariants import *


if __name__ == "__main__":

    print('1. Normal Game')
    print('2. 2 To Go: the 2 is automatically removed, if you roll 4 on your first roll, you lose the game')
    print('3. 3 To To: the 3 is automatically removed, if you roll 4 on your first roll, you lose the game')
    print('4. 3 Down Extreme: numbers 1, 2 and 3 are pre-dropped, leaving numbers 4 to 9 up')
    print('5. Against All Odds: only the odd numbers are up')
    print('6. Even-Stevens: only the even numbers are up')
    print('7. Full House: numbers 1 - 12 are up')
    print('8. Digital: final score is the combination of the peices left, i.e. 1, 2, 5 = 125')
    print('9. Thai Style: you can only chose one of the numbers you rolled or their sum')
    print('10. The 300: 24 numbers to play with, 4 die (initially)')
    print('11. 2012: 20-sided die playing 12 numbers')

    variant = input('chose what version of the game you want to play: ')

    if int(variant) == 1:
        play_base_game()
    elif int(variant) == 2:
        two_to_go()
    elif int(variant) == 3:
        three_to_go()
    elif int(variant) == 4:
        three_down_extreme()
    elif int(variant) == 5:
        against_all_odds()
    elif int(variant) == 6:
        even_stevens()
    elif int(variant) == 7:
        full_house()
    elif int(variant) == 8:
        digital()
    elif int(variant) == 9:
        thai_style()
    elif int(variant) == 10:
        the_300()
    elif int(variant) == 11:
        twenty_twelve()
