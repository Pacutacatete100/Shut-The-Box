import itertools


class Box:
    def __init__(self, pieces):
        self.pieces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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

    def combination_not_possible(self, num):
        combinations = []
        combos_tup = [seq for i in range(len(self.pieces), 0, -1)
                      for seq in itertools.combinations(self.pieces, i) if sum(seq) == num]
        for c in combos_tup:
            combinations.append(list(c))

        return not combinations

    def remove_pieces(self, nums_to_remove):
        for n in nums_to_remove:
            if self.piece_exists(n):
                self.pieces.remove(n)
            else:
                print('number no longer available')
