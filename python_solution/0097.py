class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Solution 1: DP (48ms: 47.28%)
        # We can reduce 2D array to 1D to save space
        # This DP is same to the recursion with memoization
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1+l2!=l3: return False
        dp = [[False for _ in range(l1+1)] for _ in range(l2+1)]
        dp[0][0] = True
        for i in range(1, l1+1):
            dp[0][i] = (s1[i-1]==s3[i-1] and dp[0][i-1])
            if not dp[0][i]:
                break
        for i in range(1, l2+1):
            dp[i][0] = (s2[i-1]==s3[i-1] and dp[i-1][0])
            if not dp[i][0]:
                break
        for i in range(1, l2+1):
            for j in range(1, l1+1):
                dp[i][j] = (s1[j-1]==s3[i+j-1] and dp[i][j-1]) or (s2[i-1]==s3[i+j-1] and dp[i-1][j])
        return dp[l2][l1]