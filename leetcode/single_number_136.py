# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104

from typing import List
import functools


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        xor = lambda total, current: total ^ current
        return functools.reduce(xor, nums)

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#
#         result = 0
#         for i in nums:
#             result ^= i
#
#         return result


a = Solution().singleNumber([0,0,1,1,2,2,3,3,4,4,7])
print(a)