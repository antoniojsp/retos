#extend first question to allow duplicates
import random
class TestRepeat:

    def __init__(self):
        self.storage = []
        self.map = {}
        self.length = 0

    def insert(self, val):
        self.storage.append(val)
        if val not in self.map:
            self.map[val] = []
        self.map[val].append(self.length)
        self.length += 1


    def remove(self, val):

        if val not in self.map:
            return

        #remove last element from storage and map
        last_element = self.storage.pop()
        last_element_index = self.map[last_element].pop()
        self.length -=1

        if val == last_element:
            if not self.map[val]:
                del self.map[val]
            return

        #get the index of the element_deleted and remove it from map
        old_index = self.map[val].pop()
        #change the storage at index from the elemented deleted to the previos last element
        self.storage[old_index] = last_element
        #modify the map to show the change of position in the map
        self.map[last_element].append(old_index)
        if not self.map[val]:
            del self.map[val]

    def random(self):
        index = random.randint(0, self.length-1)
        return self.storage[index]

    def __repr__(self):
        return f"Storage{str(self.storage)}, map{str(self.map)} length {self.length}"

a = TestRepeat()
a.insert(2)#0
a.insert(2)#1
a.insert(4)#2
a.insert(1)#3
a.insert(3)#4
a.insert(10)#5
a.insert(2)#6


print(a)

a.remove(3)

print(a)

a.insert(4)
print(a)
a.remove(3)
a.insert(10)
print(a)
a.remove(10)
print(a)
a.remove(1)
print(a)
print(a.random())