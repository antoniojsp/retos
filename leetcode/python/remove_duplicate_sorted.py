nums = [0,0,0,1,1,1,2,2,3,3,4]
length = len(nums)-1
temp = None
i = 0
while i < length:
    if temp is None or temp != nums[i]:
        temp = nums[i]
        i+=1
    else:
        del nums[i]
        i -= 1
        length -=1

print(nums)

