class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        Min, Max = prices[0], 0
        for i in range(1, len(prices)):
            Max = max(Max, prices[i]-Min)
            Min = min(Min, prices[i])
        return Max