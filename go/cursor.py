class Cursor:
    def __init__(self, n):
        self._n = n
        self._position = [0, 0]

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, list):
            raise TypeError
        self._position = value
    
    def update(self, code):
        if code == 119:
            self._position[0] -= 1
        elif code == 97:
            self._position[1] -= 1
        elif code == 115:
            self._position[0] += 1
        elif code == 100:
            self._position[1] += 1
        self._position[0] %= self._n
        self._position[1] %= self._n

    