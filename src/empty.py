from piece import Piece


class Empty:
    """Empty Piece"""

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.image = '🙿'

    def __str__(self):
        return self.image

    def __repr__(self):
        return f'{self.__class__.__name__}(NO COLOR)'

    def make_move(self, pos_to):
        raise Exception('No piece selected')
