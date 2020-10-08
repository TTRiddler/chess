from piece import Piece, COLORS, BLACK, WHITE


CONSOLE_IMAGE = {
    BLACK: '\33[94m♛',
    WHITE: '\33[93m♕'
}


class Queen(Piece):
    """ Queen """

    def make_move(self, piece_to):
        if not self.can_move(piece_to):
            raise Exception('Queen can\'t move there.')

        self.board[self.position], self.board[piece_to.position] = None, self.board[self.position]

        if not self.made_first_move:
            self.made_first_move = True
            
        if piece_to is not None:
            self.board.deleted_pieces.append(piece_to)
        
        self.board.history.append(f'{self}({self.position}) --> {piece_to}({piece_to.position})')

    def can_move(self, piece_to):
        if self.side == piece_to.side:
            return False

        pos_from = self.board.get_coords(self.position)
        pos_to = self.board.get_coords(piece_to.position)

        diff0 = pos_to[0] - pos_from[0]
        diff1 = pos_to[1] - pos_from[1]

        if abs(diff0) == abs(diff1):
            k0, k1 = 1 if diff0 > 0 else -1, 1 if diff1 > 0 else -1
            for i in range(1, abs(diff0)):
                if self.board[self.board.get_pos((pos_from[0] + i * k0, pos_from[1] + i * k1))] is not None:
                    return False
            return True
        elif pos_from[1] == pos_to[1]:
            space = range(pos_to[0] + 1, pos_from[0]) if pos_from[0] > pos_to[0] else range(pos_from[0] + 1, pos_to[0])
            for item in space:
                if self.board[self.board.get_pos((item, pos_to[1]))] is not None:
                    return False
            return True
        elif pos_from[0] == pos_to[0]:
            space = range(pos_to[1] + 1, pos_from[1]) if pos_from[1] > pos_to[1] else range(pos_from[1] + 1, pos_to[1])
            for item in space:
                if self.board[self.board.get_pos((pos_to[0], item))] is not None:
                    return False
            return True

    def __str__(self):
        return CONSOLE_IMAGE[self.side]

    def __repr__(self):
        return f'<Queen ({COLORS[self.side]})>'
