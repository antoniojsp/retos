
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        j = 1
        print(prices)
        max_profit = 0
        buy = 0  # look for smaller
        sell = 1  # look for bigger
        while j < len(prices):
            if






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