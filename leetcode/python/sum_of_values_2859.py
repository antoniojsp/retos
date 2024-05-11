# . https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        count = 0
        for i, j in enumerate(nums):
            n_of_ones = bin(i).count("1")
            # for i in bin(i)[2:]:
            #     if i == "1":
            #         n_of_ones+=1
            if n_of_ones == k:
                coun t+ =j

        return count
