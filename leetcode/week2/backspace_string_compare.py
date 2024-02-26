#https://leetcode.com/problems/backspace-string-compare/description/

class Solution:

    @staticmethod
    def clean_string(string: str) -> str:
        result = []
        for i in string:
            if i == "#":
                if not result:
                    continue
                else:
                    result.pop()
            else:
                result.append(i)
        return "".join(result)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.clean_string(s) == self.clean_string(t)
