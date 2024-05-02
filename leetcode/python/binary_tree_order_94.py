
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def helper(node, arr=None):
            if arr is None:
                arr = []
            if node:
                helper(node.left, arr)
                arr.append(node.val)
                helper(node.right, arr)
            return arr
        return helper(root)

