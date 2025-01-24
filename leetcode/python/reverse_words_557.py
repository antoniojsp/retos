class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        result = [i[::-1] for i in temp]
        return " ".join(result)
x2