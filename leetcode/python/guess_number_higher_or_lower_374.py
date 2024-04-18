# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        start = 1
        end = n
        answer = -1
        while start <= end:
            mid = (start + end) // 2
            value = guess(mid)

            if value == 0:
                answer = mid
                break
            elif value == 1:
                start = mid + 1
            elif value == -1:
                end = mid - 1

        return answer
