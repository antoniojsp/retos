# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
from typing import List


class Solution:
    @staticmethod
    def check_palindrome(word :str) -> bool:

        left = 0
        right = len(word ) -1

        while left < right:
            if word[left] != word[right]:
                return False
            left + =1
            right - =1

        return True

    def firstPalindrome(self, words: List[str]) -> str:

        for word in words:
            if self.check_palindrome(word):
                return word

        return ""
