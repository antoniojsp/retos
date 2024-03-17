import math

class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            x = 1/x
            n = -n

        if n == 0:
            return 1
        if n == 1:
            return x

        if n%2 == 0:
            result = x
            for i in range((n-1)//2):
                result = x * result

            return result*result
        else:
            result = x
            for i in range((n-1)//2):
                result = x * result

            return result*result*x

print(Solution().myPow(0.00001,2147483647))
# print(2.10**7)

# for i in range(0, 1000):
#     print(i)
#     assert round(2.10**i, 4) == round(Solution().myPow(2.10,i), 4)