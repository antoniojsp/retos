from idlelib.tree import TreeNode
from typing import Optional, List


# https://leetcode.com/problems/binary-tree-paths/description/?
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        S = [(root, f"{root.val}")]
        result = []
        while S:
            node, path = S.pop()
            if node.left:
                S.append((node.left, path + f"->{node.left.val}"))

            if node.right:
                S.append((node.right, path + f"->{node.right.val}"))

            if not node.left and not node.right:
                result.append(path)


        return result



