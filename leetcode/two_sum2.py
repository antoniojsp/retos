"""
Two sum but without extra space. Space complexity O(1)
"""

arr = [2,7,11,15]
target = 9
def  twoSum(numbers, target):

    left = 0
    right = len(numbers) -1

    while True:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left+1, right+1]
        elif current_sum > target:
            right -=1
        else:
            left +=1





print(twoSum(arr, target))