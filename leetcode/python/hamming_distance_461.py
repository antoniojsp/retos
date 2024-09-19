#https://leetcode.com/problems/hamming-distance/description/
from functools import reduce


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = bin( x ^y)[2:]
        if len(xor) == 1:
            return int(xor)
        times = reduce(lambda a, b :int(a ) +int(b), xor)
        return times

