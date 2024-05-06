

# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        stack = []

        for i in s:
            if not stack:
                stack.append(i)
            else:
                peek = stack[-1]
                if peek == "R" and i == "L":
                    stack.pop()
                elif peek == "L" and i == "R":
                    stack.pop()
                else:
                    stack.append(i)

                if not stack:
                    count+= 1

        return count
