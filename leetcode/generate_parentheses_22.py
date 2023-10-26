from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def helper(open, close):

            if open == close == 0:
                return []

            if open > close:
                return []

            if open < close:


            helper(open-1,close-1)


        helper(3,3)




print(Solution().generateParenthesis(3))