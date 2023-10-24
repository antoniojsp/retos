
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        i = 0
        j = 2
        max_profit = prices[0] - prices[1]
        while j < len(prices):
            left = prices[i]
            right = prices[j]
            if left - right > max_profit:
                max_profit = left - right
                j+=1
            if left - right < max_profit:
                i+=1

        print(max_profit)


        # max_profit = 0
        # for i in range(len(prices)):
        #     current = prices[i]
        #     maximum = 0
        #     for j in range(i+1, len(prices)):
        #         maximum = max(maximum, prices[j])
        #
        #     max_profit = max(max_profit, maximum-current)
        #
        #
        # return max_profit






print(Solution().maxProfit([7,1,5,3,6,4]))