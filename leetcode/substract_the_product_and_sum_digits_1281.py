#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        suma = 0
        product = 1

        while 1 <= n:
            suma += n% 10
            product *= n % 10
            n //= 10

        return product - suma
