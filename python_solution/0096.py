class Solution:
    def numTrees(self, n: int) -> int:
        # Solution 1: Use DP (28ms: 75.55%)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]
        
        # Solution 2: Catalan Numberc(24ms: 92.42%)
        res = 1
        temp = 1
        for i in range(2, n+1):
            res *= (i+n)
        for i in range(1, n+1):
            temp *= i
        return res//temp