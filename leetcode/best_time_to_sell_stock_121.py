
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # try to find the lowest price and the highest one but the buying happens before than selling.
        buy = 0
        maximum = 0
        sell = 1
        if len(prices) == 0:
            return 0
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return 0 if prices[0] > prices[1] else prices[1]-prices[0]

        while sell <= len(prices)-1:
            if prices[buy] > prices[sell]:
                buy = sell
                sell = sell + 1

            if prices[buy] <= prices[sell]:
                maximum = max(maximum, prices[sell] - prices[buy])
                sell += 1

        return maximum




print(Solution().maxProfit([1,2,4]))