class Solution:
    def __init__(self):
        self.cache= {}
    def fib(self, n: int) -> int:
        result= [-1]*(n+1)
        result[0] = 0
        result[1] = 1

        for i in range(2, n+1):

            result[i] = result[i-1] + result[i-2]
        print(result)
        return result[n]


print(Solution().fib(3))