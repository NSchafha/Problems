from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        buy = prices[0]
        for sell in prices:
            best = max(best, sell - buy)
            buy = min(buy, sell)
        return best