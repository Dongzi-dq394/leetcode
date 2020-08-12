class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Solution 1: DP (168ms: 58.32%)
        ls, lt = len(s), len(t)
        if ls<=lt:
            return 1 if s==t else 0
        dp = [[0 for _ in range(ls+1)] for _ in range(lt+1)]
        dp[0][0] = 1
        for i in range(1, lt+1):
            for j in range(i, ls+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = sum(dp[i-1][:j])
        return sum(dp[lt])