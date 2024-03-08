# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        mex_sub = nums[0]
        current = 0

        for i in nums:
            if current < 0:
                current = 0
            current+=i
            mex_sub = max(mex_sub, current)

        return mex_sub






print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))