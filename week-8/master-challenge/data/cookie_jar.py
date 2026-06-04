

class Jar:
    cookies = 0
    def __init__(self, capacity):
        self.capacity = capacity
        self._cookies = Jar.cookies

    def __str__(self):
        cookies = ""
        for _ in range(self._cookies):
            cookies += "🍪"
        return f"Cookies: {cookies}"

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity_):
        if not capacity_.isdigit():
            raise ValueError("A quantity must be a positive number.")
        capacity = int(capacity_)
        if not capacity:
            raise ValueError("A cookie jar can accept more cookies than that.")
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