# https://leetcode.com/problems/binary-search/

nums = [5]
target = 5


def binary_search(arr:list, value:int) -> int:

    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start+end)//2# overflow bug in some languages
        # mid = start+ (end -start)//2
        if arr[mid] == value:
            return mid

        if arr[mid] > value:
            end = mid - 1
        else:
            start =  mid + 1

    return -1

print(binary_search(nums, target))
