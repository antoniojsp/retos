from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        temp = set(nums)

        while original in temp:
            original *= 2

        return original