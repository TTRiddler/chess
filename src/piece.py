from abc import ABC, abstractmethod


BLACK = 0
WHITE = 1


COLORS = {
    BLACK: 'BLACK',
    WHITE: 'WHITE'
}


class Piece(ABC):
    """ Chess Piece """

    def __init__(self, side, board):
        self.side = side
        self.board = board
        self.position = None
        self.made_first_move = False

    @abstractmethod
    def make_move(self):
        pass

    @abstractmethod
    def can_move(self):
        pass
