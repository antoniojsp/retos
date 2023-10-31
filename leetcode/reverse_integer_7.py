class Solution:
    def reverse(self, x: int) -> int:

        if x == 0:
            return 0

        negative = False
        if x < 0:
            x *= -1
            negative = True

        temp = x
        reversed_number = []
        while temp:
            n = temp % 10
            temp //= 10
            reversed_number.append(str(n))

        result = int("".join(reversed_number))

        limit = (2**31)-1

        if -limit > result or result > limit:
            return 0


        return -result if negative else result



print(Solution().reverse(-123))