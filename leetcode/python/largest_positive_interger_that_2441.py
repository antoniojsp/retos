
class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        seen = {}

        for i in nums:
            if i < 0:
                seen[abs(i)] = True

        maxi = -1
        for i in nums:
            if i > 0 and i in seen:
                maxi = max(maxi, i)

        return maxi
