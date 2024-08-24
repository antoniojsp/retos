class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count: int = 0
        for i in nums:
            if i % 3 != 0:
                count += 1

        return count
