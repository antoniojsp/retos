#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        original_position = nums[:]
        max_value = max(nums)
        hash_map = [0] * (max_value + 2)
        for i in nums:
            hash_map[i + 1] += 1
        print(hash_map)
        for i in range(1, len(hash_map)):
            hash_map[i] += hash_map[i - 1]
        print(hash_map)
        return [hash_map[i] for i in original_position]


print(Solution().smallerNumbersThanCurrent(nums = [8,1,2,2,3]))