

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
                raise ValueError("A quantity must be a number.")
        if capacity < 1:
            raise ValueError("A cookie jar can't be negatively full.")
        self._capacity = capacity

    def deposit(self, cookies):
        if not cookies:
            raise ValueError("You can't deposit zero cookies.")
        if not isinstance(cookies, int):
            if not isinstance(cookies, float):
                raise TypeError("A quantity must be a number.")
        if cookies < 0:
            raise ValueError("Negative cookies isn't a thing.")
        if cookies > self._capacity:
            raise ValueError("Cookie overflow!")
        self._cookies = cookies

jar = Jar(3)
print(jar.capacity)
jar.deposit("l")