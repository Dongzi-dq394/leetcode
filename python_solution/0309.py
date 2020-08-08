class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1: DP from discussion (40ms: 83.41%)
        profit_free = 0
        stock_have = cool = -float('Inf')
        for price in prices:
            profit_free, stock_have, cool = max(profit_free, cool), max(profit_free-price, stock_have), stock_have+price
        return max(profit_free, cool)