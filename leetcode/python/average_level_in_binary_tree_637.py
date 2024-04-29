#https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        Q = deque([(root, 0)])
        values = {}
        while Q:
            node, level = Q.popleft()
            if level not in values:
                values[level] = (0 ,0)
            values[level] = (values[level][0 ] +node.val, values[level][1 ] +1)

            if node.left:
                Q.append((node.left, level +1))
            if node.right:
                Q.append((node.right, level +1))

        return [sum /times for sum, times in values.values()]

