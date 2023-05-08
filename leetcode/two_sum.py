
def twoSum_brute_force(nums: list[int], target: int) -> list[int]:
    '''
    0(n^2) time complexity
    '''
    current = None
    for i in range(0,len(nums)):
        if current
        for j in range(i+1, len(nums)):
            if target - nums[i] == nums[j]:
                return [i, j]

    return []

nums =[-2,7,11,15]
target = 9

print(twoSum_brute_force(nums, target))




def twoSum(nums: list[int], target: int) -> list[int]:
    dict = {}

    for i, val in enumerate(nums):
        remainder = target-val

        if remainder not in dict:
            dict[val] = i
        else:
            return [i, dict[remainder]]

    return []

# nums =[-2,7,11,15]
# target = 9
#
# print(twoSum(nums, target))