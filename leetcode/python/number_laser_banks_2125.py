#  https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # counts the number of "1" in each row, and ignore the rowz with zero "1"
        beams = [i.count("1") for i in bank if i.count("1")]

        res = 0
        for i in range(len(beams ) -1):
            res += beams[i ] *beams[ i +1]

        return res