class DoublyLinkedNode:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def test(self):
        print("### ASCENDING ###")
        self.print_values()
        print()
        print("\n### INVERSE ###")
        self.print_inverse()

    def insert(self, val):
        if self.head == None:
            self.head = DoublyLinkedNode(val)
        else:
            new_node = DoublyLinkedNode(val)
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def print_values(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def print_inverse(self):
        temp = self.head
        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" ")
            temp = temp.prev


    def insert_val(self, val):
        new_node = DoublyLinkedNode(val)
        #edge case: value is less than self.head.data
        if val <= self.head.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        #search for a place
        temp = self.head
        previous = None
        while temp:
            if val < temp.data:
                new_node.prev = temp.prev
                new_node.next = temp
                temp.prev.next = new_node
                temp.prev = new_node
                return
            previous = temp
            temp = temp.next
        new_node.prev = previous
        previous.next = new_node






a = DoublyLinkedList()
a.insert(3)
a.insert(5)
a.insert(7)
a.insert(6)
a.insert(9)
# a.insert_val(1)
a.insert_val(12)
a.test()

