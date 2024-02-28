# https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n >= 1:
            count += n % 2
            n //= 2
        return count

# class Solution {
#     fun singleNumber(nums: IntArray): Int {
#         var result: Int = 0
#         for (i in nums) {
#             result = result xor i
#         }
#         return result
#     }
# }