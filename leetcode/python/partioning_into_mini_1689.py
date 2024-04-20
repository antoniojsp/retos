
#https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/


class Solution:
    def minPartitions(self, n: str) -> int:

        max_digit = 0
        for i in n:
            val = int(i)
            max_digit = val if max_digit < val else max_digit
        return max_digit