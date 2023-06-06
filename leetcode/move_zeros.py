# https://leetcode.com/problems/move-zeroes/


def moveZeroes(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            j = i
            while j < len(nums)-1:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j+=1

            if i == len(nums):
                break
            continue
        i+=1
        print(*nums)
    return nums







nums = [0,1,0]
#[0,1,0]
#
print(moveZeroes(nums))