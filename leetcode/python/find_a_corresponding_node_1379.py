#https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from idlelib.tree import TreeNode


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        q = deque([(original, cloned)])

        while q:
            temp = q.popleft()
            if temp[0] == target:
                return temp[1]

            if temp[0].left:
                q.append((temp[0].left, temp[1].left))
            if temp[0].right:
                q.append((temp[0].right, temp[1].right))


