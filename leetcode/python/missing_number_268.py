from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total =  (n*(n+1))/2

        return int(total - sum(nums))


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         lenght = len(nums)  # values from 0 to lenght
#         nums.sort() #  sort array in ascending order
#         j = 0  # timers index
#         for i in range(lenght):
#             if i != nums[j]:  #. if timers index value and j are equal, means value present
#                 return i  # return value of i if it's not fun in nums.
#             j +=1  # check next element
#
#         return j  #check for the lenght value since range is  0. to lenght.


a = Solution().missingNumber([9,6,4,2,3,5,7,0,1])

print(a)