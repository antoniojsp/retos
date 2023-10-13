'''
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
'''
nums1 = [1,2,3,0,0,0]
num2 = [2,5,6]
def move_right(arr, start, ending):
    for i in range(ending, start, -1):
        arr[i], arr[i-1] =arr[i-1], arr[i]
    print(arr)

# move_right(a, 0, 3)
# move_right(a, 1, 4)

i = 0
j = 0
ending = 2
while i < len(nums1):
    if nums1[i] <= nums2[j]:
