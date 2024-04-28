# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from idlelib.tree import TreeNode


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def helper(node_original: TreeNode, node_cloned: TreeNode, target):
            if node_original is None:
                return None
            if node_original == target:
                return node_cloned

            a = helper(node_original.left, node_cloned.left, target)
            b = helper(node_original.right, node_cloned.right, target)

            return a or b

        return helper(original, cloned, target)

        # q = deque([(original, cloned)])

        # while q:
        #     original_node, clone_node = q.popleft()
        #     if original_node == target:
        #         return clone_node
        #     if original_node.left:
        #         q.append((original_node.left, clone_node.left))
        #     if original_node.right:
        #         q.append((original_node.right, clone_node.right))


