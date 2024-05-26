#  https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
class Solution:
    @staticmethod
    def count_vowel(word :str) -> int:
        count = 0
        for i in word:
            if i in "aeiou":
                count+=1
        return count

    def halvesAreAlike(self, s: str) -> bool:
        first = s[0:len(s )//2].lower()
        second = s[len(s )//2:].lower()

        return self.count_vowel(first) == self.count_vowel(second)
