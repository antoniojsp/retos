class Stacks:
    def __init__(self):
        self.arr = []

    def __repr__(self):
        return str(self.arr)

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        return self.arr.pop()

    def print_first(self):
        return self.arr[0]

    def size(self):
        return len(self.arr)

    def isEmpty(self):
        return True if self.size() == 0 else False

    def peek(self):
        return self.arr[-1]


class Queue:
    def __init__(self):
        self.stack1 = Stacks()
        self.stack2 = Stacks()
        self.count = 0

    def __repr__(self):
        return str(self.stack1) + str(self.stack2)

    def enqueue(self, val):
        self.stack1.push(val)

    def dequeue(self):
        if self.stack2.isEmpty():
            for i in range(self.stack1.size()):
                self.stack2.push(self.stack1.pop())

            self.stack2.pop()
        else:
            self.stack2.pop()

    def print_first(self):
        if self.stack2.isEmpty():
            val = self.stack1.print_first()
        else:
            val = self.stack2.peek()
        return val

a = Queue()

a.enqueue(10)
a.enqueue(20)
print(a)
a.dequeue()
print(a)