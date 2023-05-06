
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(0,len(nums)):
        remainder = target - nums[i]
        for j in range(i+1, len(nums)):
            if remainder == nums[j]:
                return [i, j]

    return []

nums =[3,2,4]
target = 6

