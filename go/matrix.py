from copy import copy

class MatrixError(Exception):
    pass

class Matrix(object):
    def __init__(self, width, height, empty=None):
        self._width = width
        self._height = height
        self._empty = empty
        self._fill()

    def _fill(self, value=None):
        value = value or self._empty
        self._array = [
            [value for i in range(self._width)]
            for j in range(self._height)
        ]

    def _is_possible_x(self, x):
        return (x < 1 or x > self._width)

    def _is_possible_y(self, y):
        return (y < 1 or y > self._height)

    def _is_possible(self, x, y):
        if (self._is_possible_x(x) or self._is_possible_y(y)):
            raise ArrayError("Out of range")

    def _index(cls, x, y):
        return x - 1, y - 1

    def __getitem__(self, coords):
        self._is_possible(*coords)
        x, y = self._index(*coords)
        return self._array[y][x]

    def __setitem__(self, coords, value):
        self._is_possible(*coords)
        x, y = self._index(*coords)
        self._array[y][x] = value

    def __eq__(self, other):
        return self._array == other._array

    def __str__(self):
        return "\n".join([[str(e) for e in row] for row in self._array])

    @property
    def copy(self):
        new = copy(self)
        new._array = [copy(row) for row in self._array]
        return new
