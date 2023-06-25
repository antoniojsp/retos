nums = [0,0,0,1,1,1,2,2,3,3,4]


i = 0
prev = None
while i < len(nums):
    if prev is None:
        prev = nums[i]
        i += 1
    elif prev == nums[i]:
        k = i
        print(nums)
        while k <len(nums)-1:
            nums[k] = nums[k+1]
            k += 1
        prev = nums[i]
        i += 1

    else:
        prev = nums[i]
        i += 1

print(nums)
