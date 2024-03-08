# https://leetcode.com/problems/left-and-right-sum-differences/description/
from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        total = sum(nums)
        left = 0
        right = total

        for i in range(len(nums)):
            right = right - nums[i]
            temp = abs(left - right)
            left = left + nums[i]
            nums[i] = temp

        # for i in nums:
        #     right = right - i
        #     temp = abs(left - right)
        #     left = left + i
        #     answer.append(temp)

        return nums

print(Solution().leftRightDifference([10,4,8,3]))