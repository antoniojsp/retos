#https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/?envType=daily-question&envId=2024-04-04

class Solution:

    def maxDepth(self, s: str) -> int:

        stack = []
        count = 0
        for i in s:
            if i == "(":
                stack.append("(")
            elif i == ")":
                if stack[-1] == "(":
                    stack.pop()
            count = max(count, len(stack))

        return count



