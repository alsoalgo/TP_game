class StoneError(Exception):
    pass


class Stone(object):

    def __init__(self, type, x = 0, y = 0):
        self.TYPES = {
            'B': '*',
            'W': 'o',
            'E': '.',
        }
        if type not in self.TYPES:
            raise StoneError("There's no type")
        self._type = type
        self._x = x
        self._y = y

    def __eq__(self, other):
        return self._type == other._type

    def __hash__(self):
        return hash(self._type)

    def __str__(self):
        return self.TYPES[self._type]

    def __repr__(self):
        return self._type.title()

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
