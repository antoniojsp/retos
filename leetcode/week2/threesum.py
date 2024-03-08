# https://leetcode.com/problems/3sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target, ignore):
        seen = {}
        for i in range(0, len(nums)):
            if i != ignore:
                complement = target-nums[i]
                if complement in seen:
                    return [nums[i], complement]
                seen[nums[i]] = i
        return []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        result = []
        for i in range(len(nums)):
            reach_zero = -nums[i]
            two_sum = self.twoSum(nums, reach_zero, i)
            if two_sum:
                two_sum.append(nums[i])
                two_sum.sort()

                if str(two_sum) not in seen:
                    seen.add(str(two_sum))
                    result.append(two_sum)

        return result


print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))