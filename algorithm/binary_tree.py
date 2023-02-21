class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def value(self):
        return self.val

    def left_child(self):
        return self.left

    def right_child(self):
        return self.right


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root =  Node(val)
        else:
            current = self.root
            new_node = Node(val)
            while True:
                if current.value() < val: #go right
                    if current.right_child():
                        current = current.right_child()
                    else:

                        break
                else: # go left
                    if current.left_child():
                        current = current.left_child()
                    else:
                        break



a  = Tree()