class Stack:
    def __init__(self):
        self.arr = []

    def __repr__(self):
        return str(self.arr)
    def push(self, val):
        self.arr.append(val)
    def pop(self):
        return self.arr.pop()
    def is_empty(self):
        return True if len(self.arr) == 0 else False
    def peek(self):
        if self.is_empty():
            return -1
        else:
            return self.arr[-1]

a = "aaabccddd"
s = Stack()
for i in a:
    if s.peek() == i:
        s.pop()
    else:
        s.push(i)

print(s)


