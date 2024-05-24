


# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp = sorted(set(nums), reverse=True)
        if len(temp) < 3:
            return temp[0]

        else:
            return temp[2]