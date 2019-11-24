# -*- coding: utf-8 -*-
from piece import Piece
from empty import Empty


class Bishop(Piece):
    IMG = ('♝', '♗')

    def make_move(self, piece_to):
        if self.can_move(piece_to):
            self.board[self.position], self.board[piece_to.position] = Empty(None, self.board), self.board[self.position]
            if not isinstance(piece_to, Empty):
                self.board.deleted_pieces.append(piece_to)
        else:
            raise Exception('Bishop can\'t move there')

    def can_move(self, piece_to):
        pos_from, pos_to = self.board.get_coords(self.position), self.board.get_coords(piece_to.position)

        if self.side != piece_to.side:
            if pos_from[1] == pos_to[1]:
                for item in range(pos_from[0] + 1, pos_to[0]):
                    if not isinstance(self.board[self.board.get_pos((item, pos_to[1]))], Empty):
                        return False
                return True
            elif pos_from[0] == pos_to[0]:
                for item in range(pos_from[1] + 1, pos_to[1]):
                    if not isinstance(self.board[self.board.get_pos((pos_to[0], item))], Empty):
                        return False
                return True
        return False
