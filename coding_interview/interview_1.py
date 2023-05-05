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
        del self.map[val]



    def random(self):
        index = random.randint(0, self.length-1)
        return self.storage[index]

    def __repr__(self):
        return str(self.storage) +"   "+str(self.map)


