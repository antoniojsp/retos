# https://leetcode.com/problems/design-an-ordered-stream/description/
class OrderedStream:

    def __init__(self, n: int):
        self.arr = ["" ] *(n) # create a map using a list
        self.start = 0 # keep track where the self.arr starts


    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey -1] = value
        answer = []
        for i in range(self.start, len(self.arr)):
            if self.arr[i] == "":
                break
            else:
                answer.append(self.arr[i])
                self.start += 1

        return answer


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


class OrderedStream:

    def __init__(self, n: int):
        self.arr = [""] * (n)  # create a map using a list
        self.start = 0  # keep track where the self.arr starts
        self.end = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey - 1] = value
        for i in range(self.start, len(self.arr)):
            if self.arr[i] == "":
                break
            else:
                self.end += 1

        answer = self.arr[self.start:self.end]
        self.start = self.end
        return answer

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)