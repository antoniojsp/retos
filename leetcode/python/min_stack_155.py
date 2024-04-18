class MinStack:

    def __init__(self):
        self.history = []

    def push(self, val: int) -> None:
        if not self.history:
            self.history.append((val, val))
        else:
            top, minimum = self.history[-1]
            self.history.append((val, min(val, minimum)))

    def pop(self) -> None:
        return self.history.pop()[0]

    def top(self) -> int:
        return self.history[-1][0]

    def getMin(self) -> int:
        return self.history[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()