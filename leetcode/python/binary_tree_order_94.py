
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#
#         def helper(node, arr=None):
#             if arr is None:
#                 arr = []
#             if node:
#                 helper(node.left, arr)
#                 arr.append(node.val)
#                 helper(node.right, arr)
#             return arr
#         return helper(root)

import time
current = 1
while True:
    review = current
    arr = []
    while review > 1 and current != 1:
        arr.append(review)
        if review%2==0:
            review//=2
        else:
            review = review*3+1
    arr.append(1)
    current+=1
    print(arr)
    time.sleep(1) # Sleep for 3 seconds