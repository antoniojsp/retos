# https://www.youtube.com/watch?v=46dZH7LDbf8&ab_channel=NeetCode
#timers question
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
        if val not in self.map:
            return
        #timers remove last element from storage array
        last_value_from_storage = self.storage.pop()
        #second look up the value to remove in the map, remove from the dict and save the index
        index_to_be_removed = self.map.pop(val)
        #third, set in the index of the value to be removed from storage as the value that was pop uo from the end of the list
        self.storage[index_to_be_removed] = last_value_from_storage
        #update map to show that the last element poo up is now in the place of the element deleted
        self.map[last_value_from_storage] = index_to_be_removed
        #update the length of the storage array
        self.length -=1

    def random(self):
        index = random.randint(0, self.length-1)
        return self.storage[index]

    def __repr__(self):
        return str(self.storage) +"   "+str(self.map)


a = Test()
a.insert(2)#0
a.insert(2)#1
a.insert(4)#2
a.insert(1)#3
a.insert(3)#4
a.insert(10)#5
a.insert(2)#6


print(a)
#
a.remove(3)
#
print(a)
#
# a.insert(4)
# print(a)
# a.remove(3)
# a.insert(10)
# print(a)
# a.remove(10)
# print(a)
# a.remove(1)
# print(a)
print(a.random())