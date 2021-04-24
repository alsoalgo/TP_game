class Stone(object):
    _position = (0, 0)
    _board_dimension = (0, 0)
    _color = "E"
    """
    B == BLACK
    E == EMPTY
    W == WHITE
    """

    @staticmethod
    def is_available(arguments, variable):
        if variable in arguments:
            return arguments[variable]
        return -1

    def __init__(self, **kwargs):
        arguments = dict(kwargs)
        self._board_dimension = int(Stone.is_available(arguments, "n"))
        self._position = (int(Stone.is_available(arguments, "i")), 
                            int(Stone.is_available(arguments, "j")))
        self._color = Stone.is_available(arguments, "c")

    def __str__(self):
        return self._color

    def __int__(self):
        return self._board_dimension * self._position[0] + self._position[1]

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        if isinstance(value, list):
            value = tuple(value)
        self._position = value
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value: str):
        self._color = value

    @property
    def group(self):
        return self._dsu_group
    
    @group.setter
    def group(self, value: int):
        self._dsu_group = value
    
