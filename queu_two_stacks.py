class Stacks:
    def __init__(self):
        self.arr = []
        self.count = 0

    def __repr__(self):
        return str(self.arr)
    def push(self, val):
        self.arr.append(val)
        self.count += 1

    def pop(self):
        self.count -=1
        return self.arr.pop()

    def print_first(self):
        return self.arr[0]

    def size(self):
        return self.count

    def isEmpty(self):
        return True if self.count == 0 else False

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

b = Queue()
b.enqueue(10)
b.enqueue(11)
b.enqueue(12)
b.enqueue(13)
print(b)
b.dequeue()
print(b)
print(b.print_first())


