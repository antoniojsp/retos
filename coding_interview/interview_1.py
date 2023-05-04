# https://www.youtube.com/watch?v=46dZH7LDbf8&ab_channel=NeetCode
#first question
import random
class Test:
    def __init__(self):
        # self.storage = [] time consuming
        self.storage = []
        self.map = {}
        self.length = 0

    def insert(self, val):
        if val in self.storage:
            print("Duplicate")
            return 0
        self.storage.append(val)
        self.map[val] = self.length
        self.length += 1


    def remove(self, val):
        temp = self.storage.pop()
        if temp == val:
            return

        old_index = self.map[val]
        self.storage[old_index] = temp
        self.map[temp] = old_index
        self.length -=1



    def random(self):
        index = random.randint(0, self.length-1)
        print("index",index)
        return self.storage[index]

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
#
a.remove(3)
print(a)
a.insert((7))
print(a)

print(a.random())