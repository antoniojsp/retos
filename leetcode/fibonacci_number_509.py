class Solution:

    def fib(self, n:int, cache=None) -> int:

        if not cache:
            cache = {0: 0, 1: 1}
        if n in cache:
            return cache[n]
        if n <= 1:
            return n

        cache[n] =  self.fib(n-1, cache) + self.fib(n-2, cache)

        return cache[n]


    def fib2(self, n: int) -> int:
        if n == 0:
            return 0
        result= [-1]*(n+1)
        result[0] = 0
        result[1] = 1

        for i in range(2, n+1):

            result[i] = result[i-1] + result[i-2]
        return result[n]


temp = Solution()

for i in range(100):
    print(temp.fib(i))
    assert temp.fib(i) == temp.fib2(i)