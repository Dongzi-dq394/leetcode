class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Solution 1: Basic DP (2172ms: 26.54%)
        dp = [float("Inf")]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount]!=float('Inf') else -1
        
        # Solution 2: DP adapt to Memo (2136ms: 28.20%)
        dp = {}
        def dfs(money):
            if money == 0:
                dp[0] = 0
                return dp[0]
            if money in dp:
                return dp[money]
            dp[money] = float('Inf')
            for coin in coins:
                if coin<=money:
                    dp[money] = min(dp[money], dfs(money-coin)+1)
            return dp[money]
        res = dfs(amount)
        return res if res!=float('Inf') else -1
        
        # Solution 3: Backtracking (TLE!!)
        def backtracking(i, remain):
            if i==0 and remain==0:
                return True
            if i==0 or remain<0:
                return False
            for j in range(len(coins)):
                if backtracking(i-1, remain-coins[j]):
                    return True
            return False
        coins.sort(reverse=True)
        left, right = amount//coins[0], (amount//coins[-1])+1
        for i in range(left, right+1):
            if backtracking(i, amount):
                return i
        return -1
        
        # Solution 4: DFS (660ms: 96.45%)
        coins.sort(reverse=True)
        res = float('Inf')
        def dfs(index, pre_num, remain):
            nonlocal res
            if pre_num+int(remain/coins[index])>res:
                return
            if remain%coins[index]==0:
                res = pre_num + remain//coins[index]
                return
            if index==len(coins)-1:
                return
            total_num = int(remain/coins[index])
            for i in range(total_num, -1, -1):
                dfs(index+1, pre_num+i, remain-coins[index]*i)
        dfs(0, 0, amount)
        return res if res!=float('Inf') else -1