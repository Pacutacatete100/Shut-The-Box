import itertools


class Box:
    def __init__(self, pieces):
        self.pieces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def print_remaining_pieces(self):
        for i in self.pieces:
            print(i)

    def find_max_piece(self):
        return max(self.pieces)

    def piece_does_not_exists(self, num):
        if num not in self.pieces:
            print('you chose a number that has already been put down')
            return False

        return True

    def addition_is_not_possible(self, num):
        result = [seq for i in range(len(self.pieces), 0, -1)
                  for seq in itertools.combinations(self.pieces, i) if sum(seq) == num]
        if not result:  # if list of combinations is null
            return False

    def remove_pieces(self, nums_to_remove, num):
        die_sum = sum(nums_to_remove)

        for n in nums_to_remove:
            if not self.piece_does_not_exists(n):
                return
            else:
                if die_sum == num:
                    for i in nums_to_remove:
                        self.pieces.remove(i)
