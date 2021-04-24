class DSU:
    _size = 0
    _parents = []
    _ranks = []

    def is_available(self, number) -> bool:
        return (0 <= number and number < self._size)

    def __init__(self, size: int = 0):
        self._parents = [i for i in range(size)]
        self._ranks = [0 for i in range(size)]
        self._size = size
    
    def make_group(self, element: int):
        if not self.is_available(element):
            raise IndexError
        self._parents[element] = element
        self._ranks[element] = 0

    def find_group(self, element: int):
        if not self.is_available(element):
            raise IndexError
        if element == self._parents[element]:
            return element
        self._parents[element] = self.find_group(self._parents[element])
        return self._parents[element]
    
    def union_groups(self, first_group, second_group):
        first = self.find_group(first_group)
        second = self.find_group(second_group)
        if first != second:
            if self._ranks[first] < self._ranks[second]: 
                first, second = second, first
            self._parents[second] = first
            if self._ranks[first] == self._ranks[second]:
                self._ranks[first] += 1