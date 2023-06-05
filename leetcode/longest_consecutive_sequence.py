
nums = [0,3,7,2,5,8,4,6,0,1]

def longestConsecutive(nums):

    hash_dict = {}

    for i in nums:
        if i not in hash_dict:
            hash_dict[i] = True
    maximum = float("-inf")
    for i in nums:


print(longestConsecutive(nums))



