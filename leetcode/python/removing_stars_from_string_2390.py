# https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def removeStars(self, s: str) -> str:
        # answer = ""

        # for i in s:
        #     if not answer:
        #         answer += i
        #     else:
        #         if i == "*":
        #             answer = answer[:len(answer) - 1]
        #         else:
        #             answer += i

        # return answer



        stack = []
        for i in s:
            if stack:
                if i == "*":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

        return "".join(stack)

