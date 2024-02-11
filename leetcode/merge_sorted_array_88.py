from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ...



print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))

def move_right(arr:list, from_index:int) -> None:
    for i in range(from_index, len(arr)-1):
        temp = arr[i+1]
        arr[i+1] = arr[i]


arr1 = [1,2,3,4,5,0]
move_right(arr1, 1)
print(arr1)
