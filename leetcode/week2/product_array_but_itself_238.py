# https://leetcode.com/problems/product-of-array-except-self/description/
from functools import reduce
from typing import List


class Solution:

    def array_product(self, arr:list) -> int:
        ...

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = self.array_product(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = total
            else:
                nums[i] = int(total/nums[i])
        return nums




print(Solution().productExceptSelf([-1,1,0,-3,3]))

# multiply(24)
# divide by index 1: 1 = 24
# divide by index 2: 2 = 12
# divide by index 3: 3 = 8
# divide by index 4: 4 = 6