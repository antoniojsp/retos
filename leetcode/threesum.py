# https://leetcode.com/problems/3sum/





# def  twoSum2(numbers, target):
#     '''
#     Original twoSum function modified to return all the possible combinations that add up to the target.
#     '''
#     if len(numbers) <= 1:  # If the array has less than 2 elements, then it's not possible to find to elements
#         # that add to "target".
#         return []
#
#     numbers.sort()
#     left = 0
#     right = len(numbers) - 1
#     result = []
#     while left < right:
#         current_sum = numbers[left] + numbers[right]
#         if current_sum == target:
#             result.append([numbers[left], numbers[right]])
#             right -= 1
#             left += 1
#         elif current_sum > target:
#             right -= 1
#         else:
#             left += 1
#
#     return result

def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    result = []
    for i, val in enumerate(nums):
        remainder = target - val

        if remainder not in seen:
            seen[val] = True
        else:
            result.append([val, remainder])

    return result


# print(twoSum2([1,2,3,4,5], 6), "    ", twoSum([1,2,3,4,5], 6))


def threeSum(nums):
    '''
    Find three elements that add to 0
    '''
    if len(nums) < 3:
        return []

    seen = {}
    nums.sort()
    result = []
    for i, j in enumerate(nums):
        needed = -j
        if partial_sum := twoSum(nums[i + 1:], needed):
            for k in partial_sum:
                temp = [j]
                temp += k
                unique = str(temp)
                if unique not in seen:
                    result.append(temp)
                    seen[unique] = True

    return result


print(threeSum([-1,0,1,2,-1,-4]))

