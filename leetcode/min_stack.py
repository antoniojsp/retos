from dataclasses import dataclass

@dataclass
class State:
    val: int = None
    min: int = None

class MinStack:

    def __init__(self):
        self.state = []

    def push(self, val):
        if self.state:
            current_minimum = min(self.getMin(), val)
        else:
            current_minimum = val
        current_state = State(val=val, min=current_minimum)
        self.state.append(current_state)
    def pop(self):
        self.state.pop()

    def top(self):
        return self.state[-1].val
    def getMin(self):
        return self.state[-1].min

a = MinStack()
a.push(2147483646)
a.push(2147483646)
a.push(2147483646)
a.top()
a.pop()
a.getMin()
a.pop()
a.getMin()
print(a.__dict__)
a.pop()
