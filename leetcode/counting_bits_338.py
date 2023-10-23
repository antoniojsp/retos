

from typing import List
class Solution:

    @staticmethod
    def to_binary(n: int):
        result = []
        i = n
        while i >= 1:
            r = i % 2
            i //= 2
            result.append(r)
        return list(reversed(result))
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n+1):
            result.append(sum(self.to_binary(i)))

        return result

a = Solution().countBits(5)
print(a)