from math import floor


class Solution:
    @staticmethod
    def convert_base(num: int, base) -> str:
        result = ""
        while 1 <= num:
            reminder = num % base
            num /= base
            result += str(floor(reminder))

        return result[::-1]

    @staticmethod
    def check_palindrome(num: str) -> bool:
        for i in range(0, len(num) // 2):
            if num[i] != num[len(num) - i - 1]:
                return False
        return True

    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            if not self.check_palindrome(self.convert_base(n, i)):
                return False

        return True
