# https://leetcode.com/problems/valid-boomerang/description/
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:

        first_slope = None

        for i in range(len(points ) -1):
            x1, y1 = points[i]
            x2, y2 = points[ i +1]

            if (points[i] == points[ i +1]): # If two points are the same, then cannot be a boomerang
                return False

            curr_slope = float("inf") if x1 == x2  else (y1 -y2 ) /(x1 -x2)

            if first_slope == None: # setting up timers slope
                first_slope = curr_slope
            else: # if two slopes are the same, then it cannot be a boomerang
                if first_slope == curr_slope :
                    return False

        return True

