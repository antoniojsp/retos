from math import log, ceil, floor
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return 0
        # result = log(n, 3)
        # f, c = floor(result), ceil(result)
        # print(result)
        # return abs(f-result)<0.0001 or abs(c-result)<0.0001

        while n > 1 and n%3==0:
            n//=3

        return n == 1


Solution().isPowerOfThree(45)
