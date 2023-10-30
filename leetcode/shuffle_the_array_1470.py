from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i, j in zip(nums[:n], nums[n:]):
            result.append(i)
            result.append(j)
        return result
        # temp = []
        # i = 0
        # j = n
        # while j < len(nums):
        #     temp.append(nums[i])
        #     temp.append(nums[j])
        #     i += 1
        #     j += 1
        #
        # return temp


print(Solution().shuffle([1,2,3,4,4,3,2,1], n = 4))