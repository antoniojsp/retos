#  https://leetcode.com/problems/hash-divided-string/description/
class Solution:
    def stringHash(self, s: str, k: int) -> str:

        result = ''
        for i in range(0 ,len(s), k):
            temp = s[i: i +k]
            suma = 0
            for j in temp:
                sum a+ =ord(j ) -ord('a')

            result += chr((sum a %26 ) +ord('a'))

        return result
