class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        down = True
        up_num = 0
        buy_all = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                buy_all += (prices[i+1]-prices[i])
                if down:
                    up_num += 1
                    down = False
            else:
                down = True
        # This is very important!! --> to avoid TLE at the last two test cases
        # if k is large or equal than the whole increasing waves, then we will
        # treat this problem to the second version of stock problem because we
        # need to buy all the increasing to make the largest profit
        if k>=up_num:
            return buy_all
        if k==0: return 0
        dp = [float('Inf'), 0] * k
        for i in range(len(prices)):
            dp[0] = min(dp[0], prices[i])
            dp[1] = max(dp[1], prices[i]-dp[0])
            for j in range(1, k):
                dp[j*2] = min(dp[j*2], prices[i]-dp[j*2-1])
                dp[j*2+1] = max(dp[j*2+1], prices[i]-dp[j*2])
        return dp[-1]