# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/


class Solution:
    def minimumSum(self, num: int) -> int:
        digits_list = sorted(list(str(num)))
        first = int(digits_list[0] + digits_list[2])  # we use lowerst digit as tens.
        second = int(digits_list[1] +digits_list[3])

        return first+second