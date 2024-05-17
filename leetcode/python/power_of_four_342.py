

#https://leetcode.com/problems/power-of-four/description/

from math import sqrt, log2


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0 or n == 2:
            return False
        else:
            temp = bin(n)[2:]
            re = sum(list(map(int, temp[1:])))

            # re = temp[1:].count("1")
            if temp[0] == "1" and len(temp[1:]) % 2 == 0 and re == 0:
                return True

        return False
        # if n == 1:
        #     return True
        # elif n > 0:
        #     if n%4 != 0:
        #         return False
        #     n //= 4
        #     temp = log2(n)
        #     return temp%2==0
        # return False
