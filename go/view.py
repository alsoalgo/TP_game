import math

from .matrix import Matrix
from .board import Board


class View(Matrix):
    CURSOR = 'X'
    def __init__(self, board):
        self._board = board
        self._cursor = (1, 1)
        super(View, self).__init__(board._width, board._height)

    def _reset(self):
        self._array = [
            [str(loc) for loc in row]
            for row in self._board._array
        ]

    def redraw(self):
        self._reset()

    def _in_width(self, v):
        return max(1, min(self._width, v))

    def _in_height(self, v):
        return max(1, min(self._height, v))

    def cursor_up(self):
        self._cursor = (
            self._in_width(self._cursor[0]),
            self._in_height(self._cursor[1] - 1),
        )

    def cursor_down(self):
        self._cursor = (
            self._in_width(self._cursor[0]),
            self._in_height(self._cursor[1] + 1),
        )

    def cursor_left(self):
        self._cursor = (
            self._in_width(self._cursor[0] - 1),
            self._in_height(self._cursor[1]),
        )

    def cursor_right(self):
        self._cursor = (
            self._in_width(self._cursor[0] + 1),
            self._in_height(self._cursor[1]),
        )

    @property
    def cursor(self):
        return self._cursor

    def __str__(self):
        arr = self.copy
        if self._cursor:
            arr[self._cursor] = self.CURSOR

        return '\n'.join([' '.join(row) for row in arr._array])
