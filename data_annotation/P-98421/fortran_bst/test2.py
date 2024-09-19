# Define TreeNode class to represent each node of the tree
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Helper function to perform in-order traversal to see the merged result
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

# Function to merge two BSTs (your provided function)
def mergeBSTs(bst1, bst2):
    if not bst1:
        return bst2
    if not bst2:
        return bst1

    # Merge based on values
    if bst1.value < bst2.value:
        # Merge bst1's right subtree with bst2
        bst1.right = mergeBSTs(bst1.right, bst2)
        return bst1
    else:
        # Merge bst2's left subtree with bst1
        bst2.right = mergeBSTs(bst1, bst2.right)
        return bst2


bst1 = TreeNode(5)
bst1.left = TreeNode(3)
bst1.right = TreeNode(7)

bst2 = TreeNode(4)
bst2.left = TreeNode(2)
bst2.right = TreeNode(6)

merged_root = mergeBSTs(bst1, bst2)

def printTree(node, level=0, is_last=True):
    indent = '    ' * (level - 1)
    connector = '└── ' if is_last else '├── '
    if level > 0:
        print(indent + connector, end='')
    if node:
        print(node.value)
        children = [child for child in [node.left, node.right] if child]
        for i, child in enumerate(children):
            is_last_child = i == len(children) - 1
            printTree(child, level + 1, is_last_child)

printTree(merged_root)