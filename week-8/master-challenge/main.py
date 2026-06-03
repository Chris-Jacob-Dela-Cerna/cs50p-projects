

import re


class Jar:
    def __init__(self, capacity):
        self.capacity = capacity

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if not capacity:
            raise ValueError("A cookie jar can accept more cookies than that.")
        if not isinstance(capacity, int):
            if not isinstance(capacity, float):
                raise TypeError("A quantity must be a number.")
        if capacity < 1:
            raise ValueError("A cookie jar can't be negatively full.")
        self._capacity = capacity

print(Jar(1.5).capacity)