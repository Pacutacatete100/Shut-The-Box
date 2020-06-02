import itertools


class Box:
    def __init__(self, pieces):
        self.pieces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def print_remaining_pieces(self):
        for i in self.pieces:
            print(i)

    def find_max_piece(self):
        return max(self.pieces)

    def piece_exists(self, num):
        return num in self.pieces

    def combination_exists(self, num, numbers_to_remove):
        combinations = []
        combos_tup = [seq for i in range(len(self.pieces), 0, -1)
                      for seq in itertools.combinations(self.pieces, i) if sum(seq) == num]
        for c in combos_tup:
            combinations.append(list(c))

        numbers_to_remove.sort()

        for comb in combinations:
            if numbers_to_remove == comb:
                return True

    def remove_pieces(self, nums_to_remove_sorted, num):
        for n in nums_to_remove_sorted:
            if self.piece_exists(n):
                self.pieces.remove(n)
            elif not self.piece_exists(n):
                print('you chose a number that is no longer available')
                return
