class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False
        i = n
        while i > 0:
            if i%2 != 0:
                return False
            i//= 2

        return True

a = Solution().isPowerOfTwo(122)
print(a)
