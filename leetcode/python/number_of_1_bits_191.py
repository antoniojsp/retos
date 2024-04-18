from functools import reduce

class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = list(bin(n)[2:])
        # return sum(1 for i in temp if  i == "1")
        x = lambda i: i =="1"
        return  len(list(filter(x, temp)))


a = Solution().hammingWeight(10)

print(a)