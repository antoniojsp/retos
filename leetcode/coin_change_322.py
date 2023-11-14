from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def helper(c, a):

            if a == 0:
                return 1
            if a < 0:
                return  0
            total = 0
            for i in range(len(c)):
                coin = c[i]
                if coin > a:
                    continue
                else:
                    return 1 +  helper(coins[i:],a - coin)



        return 1 + helper(coins, amount)

print(Solution().coinChange(coins = [1,2,5], amount = 11))