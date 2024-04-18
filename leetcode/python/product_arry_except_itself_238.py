from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        from_left = [1]*len(nums)
        from_right = [1]*len(nums)
        from_left[0] = nums[0]
        from_right[-1] = nums[-1]

        for i in range(1, len(nums)):
            from_left[i] = from_left[i-1] * nums[i]

        for i in range(len(nums)-2, -1, -1):
            from_right[i] = nums[i] * from_right[i+1]

        from_left = [1] + from_left
        from_right = from_right + [1]

        result = [1]*len(nums)
        i = 0
        j = 1
        while i < len(nums):
            result[i] = from_left[i]*from_right[j]
            i+=1
            j+=1
        return result

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
print(Solution().productExceptSelf([1,2,3,4]))