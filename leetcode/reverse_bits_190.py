n = 00000010100101000001111010011100

class Solution:

    def reverseBits(self, n: int) -> int:
        temp = list(bin(n))[2:][::-1]

        return int("".join(temp),2)

a = Solution().reverseBits(n)

print(n)
print(a)
