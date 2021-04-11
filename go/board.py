from .matrix import Matrix
from .stone import Stone

class Board(Matrix):
    def __init__(self, dimension):
        self._TURNS = ("B", "W")
        self._EMPTY = Stone("E")
        super(Board, self).__init__(dimension, dimension, self._EMPTY)
        self._turn = 0
        self._stones = []

        self._score = {"black" : 0, "white" : 0}

    @property
    def turn(self):
        return self._TURNS[self._turn]

    @property
    def score(self):
        return self._score

    @property
    def _next_turn(self):
        return (self._turn + 1) % 2

    def _flip_turn(self):
        self._turn = self._next_turn
        return self._turn

    def move(self, x, y):
        if self[x, y] is not self._EMPTY:
            raise BoardError('Cannot move on top of another piece!')
        self._stones.append(Stone(self.turn, x, y))
        self[x, y] = Stone(self.turn, x, y)

    def remove(self, x, y):
        self[x, y] = self._EMPTY

    def _check_for_suicide(self, x, y):
        pass

    def _check_for_ko(self):
        pass
