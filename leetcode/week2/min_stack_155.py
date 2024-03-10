class ListExtend(list):
    def peak(self):
        return self[-1]


class MinStack:

    def __init__(self):
        self.stack = ListExtend()

    def push(self, val: int) -> None:
        current_min = val
        if not self.stack:
            self.stack.append((val, current_min))
        else:
            last_entry = self.stack[-1]
            self.stack.append((val, min(last_entry[1], current_min)))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack.peak()[0]

    def getMin(self) -> int:
        return self.stack.peak()[1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()