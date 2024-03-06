from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        color = [0]*3
        for i in nums:
            color[i] += 1

        current = 0
        for i in range(len(color)):
            for j in range(color[i]):
                nums[current] = i
                current += 1

        return nums





print(Solution().sortColors(nums = [2,0,1]))