

# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for i in sentences:
            result = max(len(i.split(" ")), result)

        return result