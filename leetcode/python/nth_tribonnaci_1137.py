
#https://leetcode.com/problems/n-th-tribonacci-number/?envType=daily-question&envId=2024-04-24

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0,1,1]
        for i in range(2, n):
            dp.append(dp[i]+dp[i-1]+dp[i-2])
        return dp[n]
