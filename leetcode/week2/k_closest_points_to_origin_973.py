from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        calculate_distance = lambda x: x[0]**2 + x[1]**2
        dict_distance = {}
        for i in points:
            distance = calculate_distance(i)
            if distance not in dict_distance:
                dict_distance[distance] = []
            dict_distance[distance].append(i)
        sorted_keys = sorted(dict_distance.keys())
        result = []
        for i in sorted_keys:
            for j in dict_distance[i]:
                result.append(j)

        return result[:k]


print(Solution().kClosest(points = [[1,3],[-2,2]], k = 1))