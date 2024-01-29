from typing import List

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

def move(arr:list, atIndex:int, value:int) -> None:
    insert = value
    for i in range(atIndex,len(nums1)):
        temp = nums1[i]
        nums1[i] = insert
        insert = temp

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = 0
        j = 0


