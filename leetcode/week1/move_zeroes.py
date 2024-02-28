# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for zeroes in range(len(nums)):
            if nums[zeroes] == 0:
                move = zeroes+1
                while move < len(nums):
                    if nums[move] != 0:
                        nums[zeroes], nums[move] = nums[move], nums[zeroes]
                        break
                    move +=1

        return nums