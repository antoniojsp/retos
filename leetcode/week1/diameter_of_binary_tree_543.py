from typing import Optional


# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self,root) -> int:
        var = 12
        def helper(sum):
            print(var)

        helper(15)

print(Solution().diameterOfBinaryTree(12))