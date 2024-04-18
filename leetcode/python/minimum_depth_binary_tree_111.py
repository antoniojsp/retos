#https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        Q = [(root, 1)]

        while Q:
            node, level = Q.pop(0)
            if node:
                if not node.left and not node.right:
                    return level

                if node.left:
                    Q.append((node.left, level + 1))
                if node.right:
                    Q.append((node.right, level + 1))



