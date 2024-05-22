#https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        for i in nums:
            res^=i

        res = res ^ k
        return bin(res).count("1")
