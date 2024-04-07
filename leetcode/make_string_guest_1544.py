# https://leetcode.com/problems/make-the-string-great/description/
class Solution:
    def makeGood(self, s: str) -> str:

        stack = [s[0]]

        for i in range(1, len(s)):
            if stack and abs(ord(s[i] ) -ord(stack[-1])) == ord("a" ) -ord("A"):
                temp = stack.pop()
                continue
            else:
                stack.append(s[i])


        return "".join(stack)






