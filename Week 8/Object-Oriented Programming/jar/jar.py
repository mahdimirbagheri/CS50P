class Jar:
    def __init__(self, capacity=12, size=0):
        # initialize a cookie jar with the given capacity
        self.capacity = capacity
        self.size = size

    def __str__(self):
        # return a str with 🍪, where is the number of cookies in the cookie jar
        return "🍪" * self.size

    def deposit(self, n):
        # add n cookies to the cookie ja
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies!")
        self.size = self.size + n

    def withdraw(self, n):
        # should remove n cookies from the cookie jar
        if n > self.size:
            raise ValueError("Too many cookies!")
        self.size = self.size - n

    @property
    def capacity(self):
        #  return the cookie jar’s capacity
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Not a non-negative integer.")
        self._capacity = capacity

    @property
    def size(self):
        # return the number of cookies actually in the cookie jar
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError
        self._size = size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()
