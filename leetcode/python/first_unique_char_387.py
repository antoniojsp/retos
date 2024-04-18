from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        order = Counter(s)
        for i, j in enumerate(s):
            if order[j] == 1:
                return i
        return -1



a = Solution().firstUniqChar("leetcode")
print(a)

