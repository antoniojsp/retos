from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:

        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        result = self.q1.popleft()
        while self.q2:
            self.q1.append(self.q2.popleft())
        return result

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0