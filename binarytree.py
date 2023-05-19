class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.head = None

    def insert(self, value):
        root = self.head
        def helper(node, val):
            if node is None:
                return Node(val)

            if node.data <= val:
                node.right = helper(node.right, val)
            else:
                node.left = helper(node.left, val)

            return node

        self.head = helper(root, value)

    def print(self):
        root = self.head
        def helper(node):
            if node:
                helper(node.left)
                print(node.data)
                helper(node.right)

        helper(root)

    # def height(self):
    #     temp = self.head
    #     def helper(node):
    #         if not node:
    #             return 1

    def minimum(self):
        root = self.head
        def helper(node):
            if not node.left:
                return node.data

            return helper(node.left)

        return helper(root)





a = BST()
a.insert(10)
a.insert(5)
a.insert(10)
a.insert(3)
a.insert(5)
a.insert(9)
a.insert(14)
a.insert(1)

a.print()
print(a.minimum())

