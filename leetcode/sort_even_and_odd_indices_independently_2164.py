from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        #sort odd
        for i in range(1, len(nums),2):
            print(nums[i])

        #sort even
        for i in range(0, len(nums)-1,2):
            print(nums[i])





print(Solution().sortEvenOdd([4,1,2,3]))