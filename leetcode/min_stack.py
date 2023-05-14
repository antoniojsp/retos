from dataclasses import dataclass


class Lista(list):
    def peek(self):
        return super().__getitem__(-1)


# a = Lista()
# a.append(0)
# a.append(1)
# a.append(2)
# a.append(3)
#
# print(a)
#
# print(a.peek())

@dataclass
class State:
    val: int = None
    min: int = None


class MinStack:

    def __init__(self):
        self.state = Lista()

    def __repr__(self):
        return str(self.state)

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
        return self.state.peek().val

    def getMin(self):
        return self.state.peek().min


a = MinStack()
a.push(2147483646)
a.push(2147483646)
a.push(2147483646)
print(a)

a.top()
a.pop()
a.getMin()
a.pop()
a.getMin()
print(a)
a.pop()
