# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = deque([(root, 0)])
        res = []
        while Q:
            node, level = Q.popleft()
            if level < len(res):
                res[level].append(node.val)
            else:
                res.append([node.val])

            if node.left:
                Q.append((node.left, level+1))
            if node.right:
                Q.append((node.right, level+1))

        return res
        # res = []

        # def helper(node, level):
        #     if node:
        #         if level < len(res):
        #             res[level].append(node.val)
        #         else:
        #             res.append([node.val])
        #         helper(node.left, level+1)
        #         helper(node.right, level+1)
        # helper(root, 0)
        # return res