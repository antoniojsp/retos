# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                temp = nums.pop()
                if len(nums) == i:
                    return len(nums)
                nums[i] = temp
            else:
                i += 1
        return len(nums)