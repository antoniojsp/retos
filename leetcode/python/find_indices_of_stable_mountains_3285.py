#https://leetcode.com/problems/find-indices-of-stable-mountains/
from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:

        return [i for i in range(1, len(height)) if height[i-1]>threshold]
        # res = []
        # for i in range(1,len(height)):
        #     if height[i-1] > threshold:
        #         res.append(i)
        # return res




print(Solution().stableMountains(height = [1,2,3,4,5], threshold = 2))