class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = start ^ goal
        return bin(flips).count("1")