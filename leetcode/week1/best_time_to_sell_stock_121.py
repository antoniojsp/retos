from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        buy = 0
        sell = 1

        while sell < len(prices)-1:
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            elif prices[sell] - prices[buy] > profit:
                profit = prices[sell] - prices[buy]
                sell += 1
            elif prices[sell] - prices[buy] <= profit:
                sell += 1

        return profit

print(Solution().maxProfit([2,2,5]))
