

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
    def capacity(self, capacity):
        if not capacity.isdigit():
            raise ValueError("A quantity must be a positive number.")
        capacity_ = int(capacity)
        if not capacity_:
            raise ValueError("A cookie jar can accept more cookies than that.")
        self._capacity = capacity_

    def deposit(self, cookies):
        if not cookies.isdigit():
            raise ValueError("A quantity must be a positive number.")
        cookies_ = int(cookies)
        if not cookies_:
            raise ValueError("You can't deposit zero cookies.")
        if cookies_ > self._capacity:
            raise ValueError("Cookie overflow!")
        self._cookies = cookies_