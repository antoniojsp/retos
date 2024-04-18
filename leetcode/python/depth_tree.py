#https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def helper(node):
            if node is None:
                return 0

            maxi = max(helper(node.left), helper(node.right))

            return 1 + maxi

        return helper(root)