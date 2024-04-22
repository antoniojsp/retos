# https://leetcode.com/problems/longest-uploaded-prefix/
class LUPrefix:

    def __init__(self, n: int):
        self.arr = [False ] *n
        self.largest = 0

    def upload(self, video: int) -> None:
        self.arr[vide o -1] = True

    def longest(self) -> int:
        print(self.arr)
        largest = 0
        for i in range(self.largest, len(self.arr)):
            if not self.arr[i]:
                break
            else:
                self.larges t+ =1

        return self.largest



# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()