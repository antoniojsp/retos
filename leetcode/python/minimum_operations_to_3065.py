
#  https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/description/


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        # We don't need to delete any value, just count the elements that need to be deleted.
        smaller_than_k = 0
        for val in nums:
            if val < k:
                smaller_than_ k+ =1

        return smaller_than_k
