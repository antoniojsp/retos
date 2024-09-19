#  https://leetcode.com/problems/sum-of-left-leaves/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        Q = [root]
        start = 0
        left_sum = 0
        while start < len(Q):
            node = Q[start]
            start +=1
            if node.left:
                Q.append(node.left)
                if node.left.left is None and node.left.right is None:
                    left_sum += node.left.value
            if node.right:
                Q.append(node.right)

        return left_sum

