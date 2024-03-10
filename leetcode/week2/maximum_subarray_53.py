# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maz_sub = nums[0]
        current = 0

        for i in nums:
            if current < 0:
                current = 0
            current+=i
            maz_sub = max(maz_sub, current)

        return maz_sub






print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))