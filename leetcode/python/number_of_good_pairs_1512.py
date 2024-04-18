from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        seen = {}
        count = 0
        for i, j in enumerate(nums):
            if j not in seen:
                seen[j] = [i]
            else:
                seen[j].append(i)
                count += len(seen[j])-1

        return count
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             count+=1
        #
        # return count

print(Solution().numIdenticalPairs(nums = [1,2,3]))