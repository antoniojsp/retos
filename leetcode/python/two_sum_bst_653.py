
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        seen = {}
        Q = [root]
        left = 0

        while left < len(Q):
            node = Q[left]
            left += 1

            if k- node.val in seen:
                return True

            seen[node.val] = True

            if node.left:
                Q.append(node.left)

            if node.right:
                Q.append(node.right)

        return False
