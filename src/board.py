from .king import King
from .queen import Queen
from .rook import Rook
from .knight import Knight
from .bishop import Bishop
from .pawn import Pawn


BLACK = 0
WHITE = 1


class Board(object):
    def __init__(self):
        self.pieces = []

    def __str__(self):
        """
        Показ шахматной доски
        :return: str
        """
        string_rep = ''
        for y in range(8):
            for x in range(8):
                piece = None
                for p in self.pieces:
                    if p.position == (x, y):
                        piece = p
                        break
                piece_rep = '\033[97m ⭗ '
                if piece:
                    side = piece.side
                    color = '\033[31m {0} ' if side == WHITE else '\033[30m {0} '
                    piece_rep = color.format(piece)
                string_rep += piece_rep
            string_rep += '\n'
        return string_rep

    # def move(self, xy_from, xy_to, color=None):
    #     """
    #     Перемещение фигуры по доске
    #     :param xy_from: tuple(x,y)
    #     :param xy_to: tuple(x,y)
    #     :param color: bool
    #     :return: None
    #     """
    #     x_from, y_from = xy_from
    #     x_to, y_to = xy_to
    #     self.board[x_from][y_from], self.board[x_to][y_to] = self.board[x_to][y_to], self.board[x_from][y_from]

    def clear(self):
        """
        Очистка шахматной доски
        :return: None
        """
        self.pieces = []

    def new(self):
        """
        Новая шахматная доска
        :return: None
        """
        for i in range(8):
            self.pieces.extend([
                Pawn(BLACK, (i, 6)),
                Pawn(WHITE, (i, 1))
            ])

        self.pieces.extend([
            Rook(BLACK, (0, 7)),
            Knight(BLACK, (1, 7)),
            Bishop(BLACK, (2, 7)),
            Queen(BLACK, (3, 7)),
            King(BLACK, (4, 7)),
            Bishop(BLACK, (5, 7)),
            Knight(BLACK, (6, 7)),
            Rook(BLACK, (7, 7)),

            Rook(WHITE, (0, 0)),
            Knight(WHITE, (1, 0)),
            Bishop(WHITE, (2, 0)),
            Queen(WHITE, (3, 0)),
            King(WHITE, (4, 0)),
            Bishop(WHITE, (5, 0)),
            Knight(WHITE, (6, 0)),
            Rook(WHITE, (7, 0))
        ])


if __name__ == '__main__':
    b = Board()
    b.new()
    # b.move((0, 1), (3, 3))
    print(b)
    # print(b)
