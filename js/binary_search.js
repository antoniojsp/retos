class Solution:
    def search(self, arr: List[int], value: int) -> int:
        start = 0
        end = len(arr)-1

        while start <= end:
            mid = (end+start)//2

            if arr[mid] == value:
                return mid

            if arr[mid] > value:
                end = mid - 1
            else:
                start =  mid + 1

        return -1