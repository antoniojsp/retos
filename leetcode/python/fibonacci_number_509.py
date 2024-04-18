class Solution:

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        a, b  = 0, 1
        for i in range(2, n+1):
            a = a + b
            a, b = b, a
        return b


print(Solution().fib(3))