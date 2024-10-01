#  https://leetcode.com/problems/hash-divided-string/description/
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        start = ord('a')
        result = []
        for i in range(0 ,len(s), k):
            temp = s[i: i +k]
            suma = sum([ord(j)-start for j in temp])

            result.append(chr((suma%26) + start))

        return "".join(result)
