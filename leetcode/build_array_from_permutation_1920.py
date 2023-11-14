from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
        # ans = []
        # for i in range(len(nums)):
        #     ans.append(nums[nums[i]])
        #
        #
        # return ans





print(Solution().buildArray([0,2,1,5,3,4]))