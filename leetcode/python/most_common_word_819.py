# https://leetcode.com/problems/most-common-word/description/
import re
from string import ascii_letters


class Solution:

    def __init__(self):
        self.clean = {}

    def count_words(self, paragraph: str) -> dict:

        temp = re.split(r"[!?',;. ]", paragraph)
        count_word = {}
        for i in temp:
            if i == "":
                continue
            word = i.lower()
            if word not in count_word:
                count_word[word] = 0
            count_word[word] += 1
        return count_word

    def delete_banned(self, banned: dict) -> dict:
        for i in banned:
            if i in self.clean:
                del self.clean[i]

    def max_freq_word(self) -> str:
        maximum = (0, "")
        for i, j in self.clean.items():
            if j > maximum[0]:
                maximum = (j, i)
        return maximum

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # clean word from
        self.clean = self.count_words(paragraph)
        self.delete_banned(banned)
        most_common_word = self.max_freq_word()
        return most_common_word[1]