'''
Change array in situ and return the number of unique elements

First approach, use swap elements and keep a counter
'''
test = [1,1,2]

def move_left(arr:list, index):
    for i in range(index, len(arr)-1):
        arr[i] = arr[i+1]

def remove_duplicates(nums:list):

    count = 0
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            move_left(nums, i)
            count+=1
        i+=1

    return count


print(remove_duplicates(test))
print(test)