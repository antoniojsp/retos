# https://leetcode.com/problems/design-hashset/description/
class MyHashSet:

    def __init__(self):
        self.SIZE = 1000
        self.arr = [[] for i in range(self.SIZE)]

    def add(self, key: int) -> None:
        key_location = key %self.SIZE
        if key not in self.arr[key_location]:
            self.arr[key_location].append(key)


    def remove(self, key: int) -> None:
        key_location = key %self.SIZE
        if key in self.arr[key_location]:
            self.arr[key_location].remove(key)

    def contains(self, key: int) -> bool:
        key_location = key %self.SIZE
        if key in self.arr[key_location]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)