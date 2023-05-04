# https://www.youtube.com/watch?v=46dZH7LDbf8&ab_channel=NeetCode
#first question
import random
class Test:
    def __init__(self):
        # self.storage = [] time consuming
        self.storage = {}
        self.map = {}

    def insert(self, val):
        if val in self.storage:
            print("Duplicate")
            return 0

        self.storage[val] = 0

    def remove(self, val):
        del self.storage[val]

    def random(self):
        return random.choice(list(self.storage.keys()))

    def __repr__(self):
        return str(self.storage)

a = Test()
a.insert(2)
a.insert(2)
a.insert(4)
a.insert(3)
a.insert(1)
print(a)
print(a.random())

a.remove(3)
print(a)
print(a.random())