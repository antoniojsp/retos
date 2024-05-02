#  https://leetcode.com/problems/find-if-path-exists-in-graph/description/
from collections import deque, defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        # conn = {i:[i] for i in range(n)}
        # for i, j in edges:
        #     conn[i].append(j)
        #     conn[j].append(i)
        conn = {}
        for i, j in edges:
            if i not in conn:
                conn[i] = set()
            conn[i].add(j)
            if j not in conn:
                conn[j] = set()
            conn[j].add(i)

        Q = deque([source])
        seen = set()

        while Q:
            node = Q.popleft()
            for i in  conn[node]:
                if i == destination:
                    return True
                if i in seen:
                    continue
                seen.add(i)
                Q.append(i)


        return False






