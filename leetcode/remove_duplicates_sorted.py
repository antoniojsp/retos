'''
Change array in situ and return the number of unique elements

First approach, use swap elements and keep a counter
'''
test = [0,0,0,0,1,1,1,2,2,3,3,4]
#from 4 to 1
def move_left(arr:list, from_index, to_index):
    move = from_index - to_index
    for i in range(from_index, len(arr)):
        arr[i-move] = arr[i]
    return arr

print(test)
print(move_left(test, 4, 1))
print(move_left(test, 4, 2))
print(move_left(test, 4, 3))
print(move_left(test, 5, 4))



def remove_duplicates(nums:list):

    count = 0
    i = 1
    while i + count != len(nums):

        if nums[i-1] == nums[i]:
            move_left(nums, i)
            count+=1
        else:
            i+=1

    return len(nums) - count


# print("final", remove_duplicates(test))
# print(test)