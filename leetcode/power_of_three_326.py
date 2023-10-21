from math import log, ceil, floor
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return 0
        result = log(n, 3)
        f, c = floor(result), ceil(result)
        print(result)
        return abs(f-result)<0.0001 or abs(c-result)<0.0001




print(Solution().isPowerOfThree(19682))

