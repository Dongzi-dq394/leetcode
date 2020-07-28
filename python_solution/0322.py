class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Solution 1: DP (2376ms: 17.80%) --> can be improved to 1816ms: 40.36%
        dp = [float('Inf')]*(amount+1)
        dp[0] = 0
        #for i in range(1, amount+1):
        #    for value in coins:
        #        if i-value >= 0:
        #            dp[i] = min(dp[i], dp[i-value]+1)
        for value in coins:
            for i in range(value, amount+1):
                dp[i] = min(dp[i], dp[i-value]+1)
        return dp[amount] if dp[amount]!=float('Inf') else -1
        
        # Solution 2: DFS from discussion (624ms: 95.31%)
        # Try from the large value
        coins = sorted(coins, reverse=True)
        res = amount+1
        def dfs(index, cur_amount, number):
            nonlocal res
            if number + cur_amount//coins[index] > res:
                return
            if cur_amount%coins[index] == 0:
                res = number + cur_amount//coins[index]
                return
            # If the index for current coin is the last one and it can't make up
            # the cur_amount, then there is no possibility for success
            if index == len(coins)-1:
                return
            times = cur_amount//coins[index]
            remain = cur_amount%coins[index]
            for i in range(times+1):
                dfs(index+1, remain+i*coins[index], number+times-i)
        dfs(0, amount, 0)
        return -1 if res>amount else res
        