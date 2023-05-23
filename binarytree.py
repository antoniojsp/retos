class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.head = None

    def insert(self, value:int) -> None:
        root = self.head
        def helper(node, val:int) -> Node:
            if node is None:
                return Node(val)

            if node.data <= val:
                node.right = helper(node.right, val)
            else:
                node.left = helper(node.left, val)

            return node

        self.head = helper(root, value)

    def print(self) -> None:
        root = self.head
        def helper(node) -> None:
            '''
            In Order
            '''
            if node:
                helper(node.left)
                print(node.data)
                helper(node.right)

        helper(root)

    def height(self):
        temp = self.head
        def helper(node):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            return max(left, right) + 1

        return helper(temp)


    def minimum(self):
        root = self.head
        def helper(node):
            if not node.left:
                return node.data

            return helper(node.left)

        return helper(root)

    def maximum(self):
        root = self.head
        def helper(node):
            if not node.right:
                return node.data

            return helper(node.right)

        return helper(root)

    # def search(self, looking_for):

    #     root = self.head
    #
    #     while root:
    #         if root.data == looking_for:
    #             return True
    #
    #         if root.data <= looking_for:
    #             root = root.right
    #         else:
    #             root = root.left
    #
    #     return False

    def search(self, looking_for):
        root = self.head
        def helper(node, val):
            if node is None:
                return False

            if node.data == val:
                return True

            if node.data <= val:
                return helper(node.right, val)

            return helper(node.left, val)

        return helper(root, looking_for)








a = BST()
a.insert(30)
a.insert(5)
a.insert(10)
a.insert(35)
a.insert(5)
a.insert(9)
a.insert(14)
a.insert(1)




# a.print()
# print(a.maximum())
print(a.height())
# print(a.search(9000))


