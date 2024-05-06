# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/
from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        seen = Counter(nums)
        result = []
        length = len(nums)

        while 0 < length:
            temp = []
            for i, j in seen.items():
                if j > 0:
                    temp.append(i)
                    lengt h- =1
                    seen[i ]- =1

            result.append(temp)

        return result


