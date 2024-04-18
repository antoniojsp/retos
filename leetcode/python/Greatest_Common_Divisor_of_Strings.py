import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        gcd_val = math.gcd(len(str1), len(str2))
        return str2[:gcd_val]





print(Solution().gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))

