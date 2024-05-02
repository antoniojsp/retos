# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        Q = [(root, 1)]
        max_level = 1
        while Q:
            node, level = Q.pop(0)
            max_level = max(max_level, level)
            for i in node.children:
                Q.append((i, level +1))

        return max_level


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        maxi = 0
        for i in root.children:
            maxi = max(self.maxDepth(i), maxi)

        return 1 + maxi

