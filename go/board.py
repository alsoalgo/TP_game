from .stone import *
from .dsu import DSU

class Board(object):
    _score = [0, 0] # [B, W] BLM!!!
    _dimension = 0 # n by n
    _map = [] # game map
    _turn = "B"
    _board_history = []
    _dsu = DSU()
    _history = []
    _deleted = []

    def is_available(self, i, j) -> bool:
        return (0 <= i and i < self._dimension) and (0 <= j and j < self._dimension)

    def flip_turn(self):
        if self._turn == "B":
            self._turn = "W"
            return
        self._turn = "B"

    def __init__(self, n: int = 9):
        self._score = [0, 0]
        self._dimension = n
        self._map = []
        self._history = []
        self._board_history = []
        self._dsu = DSU(self._dimension ** 2)
        for i in range(n):
            self._map.append([])
            for j in range(n):
                self._map[i].append(Stone(n=n, i=i, j=j, c="E"))
    
    def __str__(self):
        representation = ""
        for i in range(self._dimension):
            for j in range(self._dimension):
                representation += str(self._map[i][j])
            representation += "\n"
        return representation + "\n"

    def __getitem__(self, coordinates):
        if isinstance(coordinates, int):
            coordinates = [coordinates // self._dimension, coordinates % self._dimension]
        if self.is_available(coordinates[0], coordinates[1]):
            return self._map[coordinates[0]][coordinates[1]]
        raise IndexError
    
    def __setitem__(self, coordinates, value):
        if isinstance(coordinates, int):
            coordinates = [coordinates // self._dimension, coordinates % self._dimension]
        if self.is_available(coordinates[0], coordinates[1]) and isinstance(value, Stone):
            self._map[coordinates[0]][coordinates[1]] = value
        else:
            raise IndexError

    @property
    def score(self):
        return self._score
    
    @property
    def turn(self):
        return self._turn
    
    @property
    def history(self):
        return self._board_history
    

    def check_ko(self, i: int, j: int):
        #check history
        #append (i, j) stone and then check representation
        self[i, j] = Stone(n=self._dimension, i=i, j=j, c=self._turn)
        #if len(self._history) >= 2:
            #print(self._history[-2])
            #print(str(self))
            #input()
        if len(self._history) >= 2 and self._history[-2] == str(self):
            self[i, j] = Stone(n=self._dimension, i=i, j=j, c="E")
            return True
        return False

    def get_breath_points(self, i, j) -> list:
        color = self[i, j].color
        used = [[False for i in range(self._dimension)]
                for j in range(self._dimension)]
        queue = [[i, j]]
        used[i][j] = True
        breath_points = set()
        shifts = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        while len(queue):
            cur = queue[0]
            queue.pop(0)
            for shift in shifts:
                ni = cur[0] + shift[0]
                nj = cur[1] + shift[1]
                if self.is_available(ni, nj):
                    if self[ni, nj].color == "E":
                        breath_points.add((ni, nj))
                    elif self[ni, nj].color == color and not used[ni][nj]:
                        used[ni][nj] = True
                        queue.append([ni, nj])
        breath_points = list(breath_points)
        return breath_points

    def remove_group(self, number: int):
        for i in range(self._dimension):
            for j in range(self._dimension):
                if self._dsu.find_group(int(self[i, j])) == number:
                    if self._turn == "B":
                        self._score[0] += 1
                    else:
                        self._score[1] += 1
                    self._map[i][j] = Stone(n=self._dimension, i=i, j=j, c="E")
                    self._dsu.make_group(int(self[i, j]))

    def move(self, i: int, j: int) -> str:
        i -= 1
        j -= 1
        #success - move is available and completed
        #ko - repeating of position
        #error - there's no such position or cell is occupied
        #... - I'm still thinking about others possible return variants

        #case №1 - is the cell occupied
        if self._map[i][j].color != "E":
            return "error"

        #case №2 - is ko situation
        if self.check_ko(i, j):
            return "ko"
        
        #case №3 - do adjacent groups have breathing points (dame points)
        opponent_color = "B" if self._turn == "W" else "W"

        self[i, j] = Stone(n=self._dimension, i=i, j=j, c=self._turn)

        shifts = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        adj_groups = set()
        group_to_cell = {}
        for shift in shifts:
            adj_i = i + shift[0]
            adj_j = j + shift[1]
            if self.is_available(adj_i, adj_j) and self[adj_i, adj_j].color == opponent_color:
                cell = int(self._map[adj_i][adj_j])
                group = self._dsu.find_group(cell)
                adj_groups.add(group)
                group_to_cell[group] = [adj_i, adj_j]
        adj_groups = list(adj_groups)
        possible_can_be_killed = []
        for group in adj_groups:
            current_stone = group_to_cell[group]
            breath_points = self.get_breath_points(*current_stone)
            if len(breath_points) == 0:
                possible_can_be_killed.append(group_to_cell[group])

        own_breath_points = len(self.get_breath_points(i, j))
        if len(possible_can_be_killed) > 0:
            for kill_stone in possible_can_be_killed:
                self.remove_group(self._dsu.find_group(int(self[kill_stone])))
            for shift in shifts:
                adj_i = i + shift[0]
                adj_j = j + shift[1]
                if self.is_available(adj_i, adj_j) and self[adj_i, adj_j].color == self._turn:
                    self._dsu.union_groups(int(self[adj_i, adj_j]), int(self[i, j]))
            self._history.append(str(self))
            self.flip_turn()
            return "success"
        if own_breath_points == 0:
            self[i, j] = Stone(n=self._dimension, i=i, j=j, c="E")
            return "error"
        
        for shift in shifts:
            adj_i = i + shift[0]
            adj_j = j + shift[1]
            if self.is_available(adj_i, adj_j) and self[adj_i, adj_j].color == self._turn:
                self._dsu.union_groups(int(self[adj_i, adj_j]), int(self[i, j]))
        self._history.append(str(self))
        self.flip_turn()
        return "success"
        """
        shifts = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        adj_groups = set()
        group_to_cell = {}
        for shift in shifts:
            adj_i = i + shift[0]
            adj_j = j + shift[1]
            if self.is_available(adj_i, adj_j) and self[adj_i, adj_j].color != "E":
                cell = int(self._map[adj_i][adj_j])
                group = self._dsu.find_group(cell)
                adj_groups.add(group)
                group_to_cell[group] = [adj_i, adj_j]

        adj_groups = list(adj_groups)
        print(group_to_cell)
        

        opponent_breath_points = -1
        own_breath_points = -1
        for group in adj_groups:
            current_stone = group_to_cell[group]
            if self[current_stone].color != opponent_color:
                own_breath_points = max(own_breath_points, 
                                        len(self.get_breath_points(*current_stone)))
            else:
                opponent_breath_points = max(opponent_breath_points, 
                                            len(self.get_breath_points(*current_stone)))
        if opponent_breath_points == 1: 
            #oppenent groups have only one breath point -> it's current (i, j)
            #that means that this move kills opponent groups
            #so current player is able to make move
            self[i, j] = Stone(n=self._dimension, i=i, j=j, c=self._turn)
            for group in adj_groups:
                current_stone = group_to_cell[group]
                if self[current_stone].color != opponent_color:
                    self._dsu.union_groups(int(self[current_stone]), int(self[i, j]))
                else:
                    self.remove_group(self._dsu.find_group(int(self[current_stone])))
            self._history.append(str(self))
            self.flip_turn()
            return "success"
        elif own_breath_points == 1:
            return "error" #suicide is forbidden for go
        
        #there's no killed group, so that's simple move
        self[i, j] = Stone(n=self._dimension, i=i, j=j, c=self._turn)
        for group in adj_groups:
            current_stone = group_to_cell[group]
            if self[current_stone].color != opponent_color:
                self._dsu.union_groups(int(self[current_stone]), int(self[i, j]))
        self._history.append(str(self))
        self.flip_turn()
        return "success"
        """
    

    




        