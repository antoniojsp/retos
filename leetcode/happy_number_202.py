class Solution:
    def isHappy(self, n: int) -> bool:

        i = 0
        while n > 0:
            temp = []
            while n > 0:
                digit = n%10
                n = n - digit
                n//=10
                temp.append(digit)

            result = 0
            for i in temp:
                result+= i**2

            n = result




a = Solution().isHappy(19)
print(a)