# -*- coding: utf-8 -*-
import traceback
import re
from piece import Piece
from king import King
from queen import Queen
from rook import Rook
from knight import Knight
from bishop import Bishop
from pawn import Pawn
from empty import Empty


BLACK = 0
WHITE = 1


class Board(object):
    def __init__(self):
        self.__key_regexp = re.compile('^[A-H][1-8]$')
        self.__letter_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        self.__int_mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
        self.board = [[None] * 8 for _ in range(8)]
        self.deleted_pieces = []
        self.__empty_board()
        self.history = []

    def __str__(self):
        string_rep = '\33[90m   A  B  C  D  E  F G  H'
        k = 0
        for i, item in enumerate(self):
            if i % 8 == 0:
                k += 1
                string_rep += '\n ' + '\33[90m' + str(k) + ' '
            if isinstance(item, Empty):
                string_rep += '\33[97m🙿 '
            else:
                if item.side == WHITE:
                    string_rep += '\33[93m' + item.IMG[item.side] + ' '
                else:
                    string_rep += '\33[94m' + item.IMG[item.side] + ' '
        return string_rep

    def clear(self):
        self.__empty_board()

    def new(self):
        for key in self.__letter_mapping:
            self[key+'7'] = Pawn(BLACK, self)
            self[key+'2'] = Pawn(WHITE, self)

        self['A1'] = Rook(WHITE, self)
        self['H1'] = Rook(WHITE, self)
        self['A8'] = Rook(BLACK, self)
        self['H8'] = Rook(BLACK, self)

        self['B1'] = Knight(WHITE, self)
        self['G1'] = Knight(WHITE, self)
        self['B8'] = Knight(BLACK, self)
        self['G8'] = Knight(BLACK, self)

        self['C1'] = Bishop(WHITE, self)
        self['F1'] = Bishop(WHITE, self)
        self['C8'] = Bishop(BLACK, self)
        self['F8'] = Bishop(BLACK, self)

        self['D1'] = Queen(WHITE, self)
        self['D8'] = Queen(BLACK, self)

        self['E1'] = King(WHITE, self)
        self['E8'] = King(BLACK, self)

    def move(self, pos_from, pos_to):
        piece_from = self[pos_from]
        piece_to = self[pos_to]

        piece_from.make_move(piece_to)

    def __setitem__(self, key, value):
        key = key.upper()

        if not isinstance(value, Piece):
            raise ValueError('Value must be None or Piece')

        if self.__key_regexp.search(key):
            x, y = key
            value.position = key
            self.board[int(y)-1][self.__letter_mapping[x]] = value
        else:
            raise KeyError('The key should be like: A1')

    def __getitem__(self, key):
        key = key.upper()

        if self.__key_regexp.search(key):
            x, y = key
            return self.board[int(y)-1][self.__letter_mapping[x]]
        else:
            raise KeyError('The key should be like: A1')

    def __iter__(self):
        for row in self.board:
            for item in row:
                yield item

    def get_coords(self, position):
        return self.__letter_mapping[position[0].upper()], int(position[1]) - 1

    def get_pos(self, coords):
        return self.__int_mapping[coords[0]] + str(coords[1] + 1)

    def __empty_board(self):
        for col in self.__letter_mapping:
            for row in range(1, 9):
                self[col+str(row)] = Empty(None, self)


if __name__ == '__main__':
    b = Board()
    # print(b)
    b.new()
    while True:
        print(b)
        turn = input('\33[91mYour turn: ')
        try:
            b.move(*turn.split())
            for i in b.history:
                print('\33[91m' + i)
        except Exception as e:
            print(e)
            # print(traceback.print_exc())
