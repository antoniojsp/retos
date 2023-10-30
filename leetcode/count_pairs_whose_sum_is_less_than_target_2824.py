from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        temp = 0
        print(nums)
        for i in range(len(nums)):


            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    temp += 1
                else:
                    break
        # temp = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] < target:
        #             temp.append((i, j))


        return temp

print(Solution().countPairs(nums = [-5,0,-7,-1,9,8,-9,9], target = -14))