import unittest

class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.left = self.left
            self.left = temp

    def insert_right(self, new_node):
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.right = self.right
            self.right = temp

    def find_max(self):
        if self.right is None:
            return self.key
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.key
        return self.left.find_min()

    def in_order_traversal(self, result):
        if self.left:
            self.left.in_order_traversal(result)
        result.append(self.key)
        if self.right:
            self.right.in_order_traversal(result)
        return result

class TestBinaryTree(unittest.TestCase):

    def test_insert_left_empty(self):
        tree = BinaryTree(1)
        tree.insert_left(2)
        self.assertEqual(tree.left.key, 2)

    def test_insert_left_non_empty(self):
        tree = BinaryTree(1)
        tree.insert_left(2)
        tree.insert_left(3)
        self.assertEqual(tree.left.key, 3)
        self.assertEqual(tree.left.left.key, 2)

    def test_insert_right_empty(self):
        tree = BinaryTree(1)
        tree.insert_right(2)
        self.assertEqual(tree.right.key, 2)

    def test_insert_right_non_empty(self):
        tree = BinaryTree(1)
        tree.insert_right(2)
        tree.insert_right(3)
        self.assertEqual(tree.right.key, 3)
        self.assertEqual(tree.right.right.key, 2)

    def test_find_max_empty(self):
        tree = BinaryTree(1)
        self.assertEqual(tree.find_max(), 1)

    def test_find_max_non_empty(self):
        tree = BinaryTree(1)
        tree.insert_left(2)
        tree.insert_right(3)
        tree.insert_right(4)
        self.assertEqual(tree.find_max(), 4)

    def test_find_min_empty(self):
        tree = BinaryTree(1)
        self.assertEqual(tree.find_min(), 1)

    def test_find_min_non_empty(self):
        tree = BinaryTree(1)
        tree.insert_left(2)
        tree.insert_left(-1)
        tree.insert_right(3)
        self.assertEqual(tree.find_min(), -1)


    def test_in_order_traversal_empty(self):
        tree = BinaryTree(1)
        self.assertEqual(tree.in_order_traversal([]), [1])

    def test_in_order_traversal_non_empty(self):
        tree = BinaryTree(1)
        tree.insert_left(2)
        tree.insert_right(3)
        tree.insert_left(-1)  # Inserting to the already existing left node (2)
        self.assertEqual(tree.in_order_traversal([]), [-1, 2, 1, 3])

if __name__ == '__main__':
    unittest.main()