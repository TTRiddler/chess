from piece import Piece, COLORS, BLACK, WHITE
from empty import Empty


CONSOLE_IMAGE = {
    BLACK: '\33[94m♞',
    WHITE: '\33[93m♘'
}


class Knight(Piece):
    """ Knight """

    def make_move(self, piece_to):
        if self.can_move(piece_to):
            self.board.history.append('{0}({1}) --> {2}({3})'.format(self, self.position, piece_to, piece_to.position))
            self.board[self.position], self.board[piece_to.position] = Empty(None, self.board), self.board[self.position]
            if self.first_move:
                self.first_move = False
            if not isinstance(piece_to, Empty):
                self.board.deleted_pieces.append(piece_to)
        else:
            raise Exception('Knight can\'t move there')

    def can_move(self, piece_to):
        pos_from, pos_to = self.board.get_coords(self.position), self.board.get_coords(piece_to.position)

        if self.side != piece_to.side:
            if (pos_to[0] in (pos_from[0] - 1, pos_from[0] + 1) and pos_to[1] in (pos_from[1] + 2, pos_from[1] - 2) or
                    pos_to[0] in (pos_from[0] - 2, pos_from[0] + 2) and pos_to[1] in (pos_from[1] + 1, pos_from[1] - 1)):
                return True
        return False

    def __str__(self):
        return CONSOLE_IMAGE[self.side]

    def __repr__(self):
        return f'<Knight ({COLORS[self.side]})>'
