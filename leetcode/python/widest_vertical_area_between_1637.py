#https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        temp = [i[0] for i in sorted(points, key=lambda x: x[0])]
        maximum = 0
        for i in range(1, len(points)):
            diff = abs(temp[i - 1] - temp[i])
            if diff > maximum:
                maximum = diff
        return maximum