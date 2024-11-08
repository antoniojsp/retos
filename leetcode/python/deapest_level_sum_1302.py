# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        Q = deque([(root, 0)])  # creates a deque. Faster than using a list to pop timers item.
        max_level = 0
        sum_level = {0: root.value}  #
        while Q:
            node, level = Q.popleft()
            if level + 1 not in sum_level:
                sum_level[level + 1] = 0
            if node.left:
                left = node.left
                Q.append((left, level + 1))
                sum_level[level + 1] += left.value
            if node.right:
                right = node.right
                Q.append((right, level + 1))
                sum_level[level + 1] += right.value
            max_level = max(max_level, level)

        return sum_level[max_level]





