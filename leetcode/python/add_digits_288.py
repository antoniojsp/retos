#  https://leetcode.com/problems/add-digits/description/
class Solution:
    def addDigits(self, num: int) -> int:

        value = str(num)
        while len(value) > 1:
            digits = list(value)
            value = str(sum([int(i) for i in digits] ))

        return int(value)