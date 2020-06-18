import itertools


class Box:
    def __init__(self, pieces):
        self.pieces = pieces

    def print_remaining_pieces(self):
        for i in self.pieces:
            print(str(i) + " ", end='')

    def find_max_piece(self):
        if len(self.pieces) >= 2:
            return max(self.pieces)
        if len(self.pieces) == 1:
            return self.pieces[0]

    def piece_exists(self, num):
        return num in self.pieces

    def combinations(self, numbers, target, partial=[], partial_sum=0):
        if partial_sum == target:
            yield partial
        if partial_sum >= target:
            return
        for i, n in enumerate(numbers):
            remaining = numbers[i + 1:]
            yield from self.combinations(remaining, target, partial + [n], partial_sum + n)

    def combination_not_possible(self, roll):
        combo_list = list(self.combinations(self.pieces, roll))

        return not combo_list

    def remove_pieces(self, nums_to_remove):
        for n in nums_to_remove:
            if self.piece_exists(n):
                self.pieces.remove(n)
            else:
                print('number no longer available')

    def loss_message(self):
        print('Sorry! you\'re all out of luck! Final score is: ' +
              str(sum(self.pieces)))

    def final_score(self):
        return str(sum(self.pieces))
