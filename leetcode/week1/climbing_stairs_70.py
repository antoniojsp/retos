# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n: int) -> int:

        # dp = [0]*(n+1)

        # dp[0], dp[1] = 1, 1

        # for i in range(2,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[-1]

        def helper(current ,goal, memo=None):

            if memo is None:
                memo = {}

            if current > goal :
                return 0
            elif current == goal:
                return 1
            elif current in memo:
                return memo[current]

            memo[current] = helper(current +1, goal, memo) + helper(current +2, goal, memo)

            return memo[current]

        return helper(0, n)

