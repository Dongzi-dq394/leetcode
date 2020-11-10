class Solution:
    def numWays(self, n: int, k: int) -> int:
        # Solution 1: 1D DP (28ms: 72.65%)
        if n==0: return 0
        memo = {}
        def helper(n):
            if n==1: return k
            if n==2: return k*k
            if n in memo:
                return memo[n]
            memo[n] = (k-1)*(helper(n-1)+helper(n-2))
            return memo[n]
        return helper(n)
        
        # Solution 2: 1D DP from bottom up (24ms: 90.88%)
        if n==0: return 0
        if n==1: return k
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = k, k*k
        for i in range(2, n):
            dp[i] = (k-1)*(dp[i-1]+dp[i-2])
        return dp[-1]