
def twoSum_brute_force(nums: list[int], target: int) -> list[int]:
    '''
    0(n^2) time complexity
    '''
    last_seen = None
    for i in range(0,len(nums)):
        current = nums[i]
        if last_seen is None or current != last_seen:
            last_seen = current
            for j in range(i+1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]

    return []


def twoSum_binary_search(nums: list[int], target: int) -> list[int]:
    '''
    binary search
    '''
    last_seen = None
    for i in range(0,len(nums)):
        remainder = target - nums[i]

        if last_seen is None or remainder != last_seen:
            last_seen = remainder
            start = i+1
            end = len(nums) - 1
            while start <= end:
                mid = (start + end)//2
                if remainder == nums[mid]:
                    return [i+1, mid+1]

                if remainder < nums[mid]:
                    end = mid -1
                elif remainder > nums[mid]:
                    start = mid + 1
    return []


nums =[2,7,11,15]
target = 9

print(twoSum_binary_search(nums, target))




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