from collections import Counter
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        for i in range(0, len(nums)-1):
            count = 0
            for j in (i+1, len(nums)-1):
                if nums[i] > nums[j]:
                    count+=1

            print(count)





nums = [8, 1, 2, 2, 3]
print(Solution().smallerNumbersThanCurrent(nums))