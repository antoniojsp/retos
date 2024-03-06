# https://leetcode.com/problems/insert-interval/description/
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        for i in intervals:
            print(i[0])





print(Solution().insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))