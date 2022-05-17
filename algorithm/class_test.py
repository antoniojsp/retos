class Test:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __str__(self):
        return f"{self.a}, {self.b}"

a = Test(1,2)
print(a)
a._a = 3
print(a)


