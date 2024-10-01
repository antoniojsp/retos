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

import unittest

class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree(10)

    def test_insert_left(self):
        self.tree.insert_left(5)
        self.assertEqual(self.tree.left.key, 5)
        self.tree.insert_left(3)
        self.assertEqual(self.tree.left.key, 3)
        self.assertEqual(self.tree.left.left.key, 5)

    def test_insert_right(self):
        self.tree.insert_right(20)
        self.assertEqual(self.tree.right.key, 20)
        self.tree.insert_right(25)
        self.assertEqual(self.tree.right.key, 25)
        self.assertEqual(self.tree.right.right.key, 20)

    def test_find_max(self):
        self.assertEqual(self.tree.find_max(), 10)
        self.tree.insert_right(20)
        self.assertEqual(self.tree.find_max(), 20)
        self.tree.insert_right(25)
        self.assertEqual(self.tree.find_max(), 25)

    def test_find_min(self):
        self.assertEqual(self.tree.find_min(), 10)
        self.tree.insert_left(3)
        self.assertEqual(self.tree.find_min(), 3)
        self.tree.insert_left(1)
        self.assertEqual(self.tree.find_min(), 1)

    def test_in_order_traversal(self):
        self.tree.insert_left(5)
        self.tree.insert_right(20)
        self.tree.insert_left(3)
        self.tree.insert_right(25)
        result = self.tree.in_order_traversal([])
        self.assertEqual(result, [3, 5, 10, 20, 25])

    def test_empty_tree(self):
        empty_tree = BinaryTree(None)
        self.assertEqual(empty_tree.find_max(), None)
        self.assertEqual(empty_tree.find_min(), None)
        result = empty_tree.in_order_traversal([])
        self.assertEqual(result, [None])

if __name__ == '__main__':
    unittest.main()