class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        if ch not in word:
            return word

        result = ""
        i = 1
        while word[i - 1] != ch:
            result = word[i - 1] + result
            i += 1

        result += word[i:]
        return ch + result
