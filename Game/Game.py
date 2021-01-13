from Box import Box
from GameUtils import *


class Game:
    def __init__(self, pieces, num_sides):
        self.pieces = pieces
        self.num_sides = num_sides
        self.box = Box(self.pieces)
        self.change_roll = True


    def number_of_die(self):
        if 19 <= self.box.find_max_piece() <= 24 and self.change_roll:
            return 4
        if 13 <= self.box.find_max_piece() <= 18 and self.change_roll:
            return 3
        if 7 <= self.box.find_max_piece() <= 12 and self.change_roll:
            return 2
        if 1 <= self.box.find_max_piece() <= 6 and self.change_roll:
            return 1

    def roll_die(self, num_sides, num_dice):
        while True:
            yield sum(random.randint(1, num_sides) for i in range(num_dice))

    def get_next_roll(self):
        roll_generator = roll_die(self.num_sides, self.number_of_die())
        return next(roll_generator)


    def play_game(self):
        playing = True
        roll = 0

        while playing:
            self.box.print_remaining_pieces()
            roll = self.get_next_roll()

            if not self.box.combination_not_possible(roll):
                choices = ask_numbers_to_remove()  # TODO: make this take in input from GUI buttons
                if choices == 'end':
                    # print('You ended the game, final score is ' + self.box.final_score())
                    playing = False
                elif not choices:
                    self.change_roll = False
                    # print('Oops, Looks like you forgot to type a number')
                else:
                    if sum(choices) == roll and all(elem in self.box.pieces for elem in choices):
                        self.box.remove_pieces(choices)
                        self.change_roll = True
                        if len(self.box.pieces) == 0:
                            print('YOU WIN')
                            playing = False
                    elif sum(choices) != roll or any(elem not in self.box.pieces for elem in choices):
                        # print('doesnt add up')
                        self.change_roll = False
            elif self.box.combination_not_possible(roll):
                self.box.loss_message()
                playing = False

