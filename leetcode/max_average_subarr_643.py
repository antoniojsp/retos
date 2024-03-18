from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start_sum = sum(nums[:k])
        max_subarr_average = start_sum/k

        for i in range(1, len(nums)-k+1):
            start_sum = start_sum - nums[i-1] + nums[i+k-1]
            max_subarr_average = max(max_subarr_average, start_sum/k)

        return max_subarr_average


print(Solution().findMaxAverage(nums = [0,1,1,3,3], k = 4))