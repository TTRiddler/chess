from piece import Piece, COLORS, BLACK, WHITE
from empty import Empty


CONSOLE_IMAGE = {
    BLACK: '\33[94m♟',
    WHITE: '\33[93m♙'
}


class Pawn(Piece):
    """ Pawn """

    def make_move(self, piece_to):
        if self.can_move(piece_to):
            self.board.history.append('{0}({1}) --> {2}({3})'.format(self, self.position, piece_to, piece_to.position))
            self.board[self.position], self.board[piece_to.position] = Empty(None, self.board), self.board[self.position]
            if self.first_move:
                self.first_move = False
            if not isinstance(piece_to, Empty):
                self.board.deleted_pieces.append(piece_to)
        else:
            raise Exception('Pawn can\'t move there')

    def can_move(self, piece_to):
        pos_from, pos_to = self.board.get_coords(self.position), self.board.get_coords(piece_to.position)

        if isinstance(piece_to, Empty):
            k = (pos_from[1] - pos_to[1]) * ((-1) ** self.side)
            if pos_from[0] == pos_to[0]:
                if k == 1:
                    return True
                elif k == 2 and self.first_move:
                    inter_pos = self.position[0] + str(int(self.position[1]) + (-1) ** (self.side + 1))
                    if isinstance(self.board[inter_pos], Empty):
                        return True
            return False
        else:
            if self.side != piece_to.side:
                k = (-1) ** (self.side + 1)
                if pos_to[1] == pos_from[1] + k and pos_to[0] in (pos_from[0] - 1, pos_from[0] + 1):
                    return True
            return False

    def __str__(self):
        return CONSOLE_IMAGE[self.side]

    def __repr__(self):
        return f'<Pawn ({COLORS[self.side]})>'
