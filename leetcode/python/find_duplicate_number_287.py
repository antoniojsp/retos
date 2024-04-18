from typing import List
from functools import reduce
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(0, len(nums)):
            current = nums[i]
            for j in range(i+1, len(nums)):
                if current == nums[j]:
                    return current



a = Solution().findDuplicate([1,3,4,2,2])
# print(a)
