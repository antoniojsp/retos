
class Solution:
    def isUgly(self, n: int) -> bool:

        d = [2,3,5]
        for i in d:
            while n%i == 0:
                n //=i


        return n == 1




a = Solution().isUgly(1)

print(a)