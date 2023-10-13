class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            temp =  self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert_list(self, arr:list):

        if self.head is None:
            self

    def print(self):
        temp = self.head
        if not temp:
            print("Empty")
            return

        while temp:
            print(temp.val, end="")
            temp = temp.next




a = [1,5,9,12]
b = [3,7,11,18]

ll_a = LinkedList()
lla_b = LinkedList()

pointer1, pointer2 = 0, 0

a = LinkedList()
for i in a:
    a.insert(i)

a.print()
