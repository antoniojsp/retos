# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_index = len(nums) - 1
        result = [0] * len(nums)
        current_index = k
        for i in nums:
            result[current_index] = i
            current_index += 1
            if current_index > last_index:
                current_index = 0
        nums = result



print(Solution().rotate(nums = [1,2,3,4,5,6,7], k = 3))