# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        Q = [(p, q)]

        if p.val != q.val:
            return False

        while Q:
            temp = Q.pop(0)
            p_node, p_val = temp[0], temp[0].val
            q_node, q_val = temp[1], temp[1].val

            if p_val != q_val:
                return False

            if p_node and q_node:
                if p_node.left and not q_node.left or not p_node.left and q_node.left:
                    return False

                if p_node.right and not q_node.right or not p_node.right and q_node.right:
                    return False

                if p_node.left and q_node.left:
                    Q.append((p_node.left, q_node.left))

                if p_node.right and q_node.right:
                    Q.append((p_node.right, q_node.right))
            else:
                return False

        return True