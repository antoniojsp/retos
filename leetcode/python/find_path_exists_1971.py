
from collections import deque
from typing import List

def pprint(arr):
    for i, j in enumerate(arr):
        print(i, j)
    print()
class Solution:


    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        matrix = [[0 for _ in range(n)]for i in range(n)]
        for i, j in edges:
            matrix[i][j] = 1
            matrix[j][i] = 1
        Q = [source]
        seen = set()
        pprint(matrix)
        while Q:
            node = Q.pop(0)

            for i, j in enumerate(matrix[node]):
                print(matrix[node])
                print("Q", Q)

                if node  == destination:
                    return True
                if j == 1 and i not in seen:
                    Q.append(i)
            seen.add(node)
        return False





print(Solution().validPath( n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5 ))


