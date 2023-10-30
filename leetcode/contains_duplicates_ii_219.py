from typing import List

class Solution:


    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = {}

        for i, j in enumerate(nums):
            if j not in temp:
                temp[j] = [i]
            else:
                for x in temp[j]:
                    if abs(i-x) <= k:
                        return True
                temp[j].append(i)

        return False






print(Solution().containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))