# -*- coding: utf-8 -*-
color = {0: 'BLACK', 1: 'WHITE', None: 'None'}


class Piece(object):
    IMG = None

    def __init__(self, side, board):
        self.side = side
        self.board = board
        self.position = None

    def __str__(self):
        return self.IMG[self.side]

    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, color[self.side])

    # def make_move(self, pos_from, pos_to):
    #     piece_from = self.board[pos_from]
    #     piece_to = self.board[pos_to]

    # def can_move(self, pos_from, pos_to):
    #     raise Exception('Нельзя')
