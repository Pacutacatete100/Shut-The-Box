class Box:
    def __init__(self, pieces):
        self.pieces = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def print_remaining_pieces(self):
        for i in range(0, 9):
            print(self.pieces[i])

    def check_if_piece_exists(self, num):
        if num not in self.pieces:
            return False

        return True
