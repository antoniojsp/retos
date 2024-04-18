"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        Q = deque([(root, 0)])
        # Q = deque([(root)])
        result = {}
        # resultado = []
        while Q:
            #     length = len(Q)
            #     temp = [Q.popleft() for _ in range(length)]
            #     resultado.append([i.val for i in temp])
            #     for i in temp:
            #         for j in i.children:
            #             Q.append(j)
            node, level = Q.popleft()
            if node:
                if level not in result:
                    result[level] = []
                result[level].append(node.val)
                for i in node.children:
                    Q.append((i, level + 1))

        return list(result.values())


