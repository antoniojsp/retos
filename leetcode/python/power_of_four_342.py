

#https://leetcode.com/problems/power-of-four/description/

from math import sqrt, log2
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n > 0:
            if n%4 != 0:
                return False
            n //= 4
            temp = log2(n)
            return temp%2==0
        return False
