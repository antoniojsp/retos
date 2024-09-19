#https://leetcode.com/problems/path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        stack = [(root, root.value)]
        while stack:
            node, val = stack.pop()

            if not node.left and not node.right and val == targetSum:
                return True

            if node.left:
                stack.append((node.left, val + node.left.value))
            if node.right:
                stack.append((node.right, val + node.right.value))

        return False


