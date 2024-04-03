from typing import List


# https://leetcode.com/problems/search-insert-position/description/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        answer = 0 # keeps track where is the closer location
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                answer = mid
                break
            elif nums[mid] < target:
                start = mid + 1
                answer = mid+1
            else:
                end = mid - 1
                answer = mid

        return answer