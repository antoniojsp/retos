from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        result = s[:]
        j = len(result)-1
        for i in range(0, len(s)//2):
            result[i], result[j] = result[j], result[i]
            j-=1


s = ["h","e","l","l","o"]
a = Solution().reverseString(s)
print(a)