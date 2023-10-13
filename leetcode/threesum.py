# https://leetcode.com/problems/3sum/


arr = [0,0,0,0]

tar = 3


def  twoSum(numbers, target):

    if not numbers:
        return []
    left = 0
    right = len(numbers) - 1
    result = []
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            result.append([numbers[left], numbers[right]])
            right -= 1
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    return result


def threeSum(nums):
    '''
    Find three elements that add to 0
    '''
    seen = {}
    nums.sort()
    result = []
    for i, j in enumerate(nums):
        needed = j
        print(needed)
        if partial_sum := twoSum(nums[i + 1:], needed):
            if partial_sum:
                print(partial_sum)
                for k in partial_sum:
                    temp = [k]
                    temp += k
                    unique = str(temp)
                    if unique not in seen:
                        result.append(temp)
                        seen[unique] = True

    return result


# print(twoSum([0, 1, 1, 2], 2))
print(threeSum([-1,0,1,2,-1,-4]))

#edge case all zeros 0
