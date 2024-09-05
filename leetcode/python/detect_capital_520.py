#  https://leetcode.com/problems/detect-capital/description/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # if word is the same than the word itself after any of the following transformation, then it's true.
        if word in [word.upper(), word.capitalize(), word.lower()]:
            return True

        return False

