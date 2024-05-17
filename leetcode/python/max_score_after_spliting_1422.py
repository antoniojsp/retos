


# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2024-05-17

class Solution:
    def maxScore(self, s: str) -> int:
        max_count = 0
        for i in range(1,len(s)):
            count_zero = s[:i].count("0")
            count_one = s[i:].count("1")
            max_count = max(max_count, count_zero+count_one)

        return max_count
