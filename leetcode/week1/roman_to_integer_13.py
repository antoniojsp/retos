#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        decode = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}
        count = decode[s[-1]]
        i = len(s) - 2
        while i >= 0:
            if decode[s[i]] >= decode[s[i + 1]]:
                count += decode[s[i]]
            else:
                count -= decode[s[i]]
            i -= 1
        return count


print(Solution().romanToInt(s = "LVIII"))