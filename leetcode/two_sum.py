#https://leetcode.com/problems/two-sum/
nums = [3,3]
target = 6

# print(nums[0:0]+nums[1:len(nums)])

def dict_index(arr:list)->dict:
    indexes = {}
    for i, j in enumerate(arr):
        i
        indexes[j] = i
    return indexes

# print(dict_index(nums))

def twoSum(nums:list, target:int)->list:
    indexes = dict_index(nums)
    print(indexes)
    for i, j in enumerate(nums):
        remainder = abs(target-j)
        if remainder in indexes and remainder != j:
            return [i, indexes[remainder]]

print(twoSum(nums, target))



