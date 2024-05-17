#  https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area_maxima = 0
        while left < right:
            h = height[left] if height[left] < height[right] else height[right]
            area = h * (right - left)




print