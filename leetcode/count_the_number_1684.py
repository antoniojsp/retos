# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        answer = 0
        allowed_set = set(list(allowed))
        for i in words:
            temp = set(list(i))
            if temp.issubset(allowed_set):
                answer+=1

        return answer