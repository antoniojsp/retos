#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        temp = sorted(nums, reverse=True)
        answer = {}

        i = 0
        while i < len(temp):
            j = i
            count = 0
            current = temp[i]
            while j < len(temp):
                if current > temp[j]:
                    count+=1
                j+=1
            answer[temp[i]] = count
            i+=1

        for i in range(len(nums)):
            nums[i] = answer[nums[i]]

        return nums





print(Solution().smallerNumbersThanCurrent(nums = [8,1,2,2,3]))