class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = Node(val)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node:
            self._print_tree(node.left)
            print(node.val, end=" ")
            self._print_tree(node.right)

# Create two BSTs
bst1 = BST()
bst1.insert(5)
bst1.insert(2)
bst1.insert(8)
bst1.insert(3)
bst1.insert(9)

bst2 = BST()
bst2.insert(10)
bst2.insert(6)
bst2.insert(14)
bst2.insert(7)
bst2.insert(15)

# Print the original trees
print("BST 1:")
bst1.print_tree()
print("\nBST 2:")
bst2.print_tree()

# Merge the two trees
def merge(bst1, bst2):
    # Merge two trees
    root = bst1.root
    while bst1 and bst2 and bst1.val < bst2.val:
        bst1 = bst1.left
        root = bst1
        bst1 = bst1.right
    while bst2 and bst1.val < bst2.val:
        bst2 = bst2.right
        root = bst2
        bst2 = bst2.left
    if bst1:
        bst1.left = root
    bst2.right = root
    return root

merged_root = merge(bst1, bst2)

# Create a new BST with the merged root
merged_bst = BST()
merged_bst.root = merged_root

# Print the merged tree
print("\nMerged BST:")
merged_bst.print_tree()