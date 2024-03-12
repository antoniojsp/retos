from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]

        for i in range(len(newInterval)):
            interval_start = intervals[i][0]
            interval_end = intervals[i][1]
            if interval_start < start < interval_end:
                print(start)
            elif




print(Solution().insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))