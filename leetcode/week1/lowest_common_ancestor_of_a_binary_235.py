#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root

        while current:
            if p.value <= current.value <= q.value or p.value >= current.value >= q.value:
                return current
            elif p.value < current.value and q.value < current.value:
                current = current.left
            elif p.value > current.value and q.value > current.value:
                current = current.right

