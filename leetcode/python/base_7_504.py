class Solution:

    def convertToBase7(self, num: int) -> str:

        if num == 0:  # if num is zero, then the result is always zero
            return "0"

        partial_result = ""
        is_negative = False

        if num < 0:
            num = abs(num)
            is_negative = True

        while num > 0:
            partial_result += str(num % 7)
            num //= 7

        result = int(partial_result[::-1])

        if is_negative:
            result *= -1

        return str(result)