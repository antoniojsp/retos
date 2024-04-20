# https://leetcode.com/problems/minimum-time-visiting-all-points/
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        i = 0
        while i < len(points ) -1:
            x1, y1 = points[i]
            x2, y2 = points[ i +1]

            time += max(abs(x1 - x2), abs(y 1 -y2)) i+=1
        return time