

class Jar:
    def __init__(self, capacity):
        self.capacity = capacity

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if not self.capacity:
            raise ValueError
        if capacity < 1:
            raise ValueError
        self._capacity = capacity