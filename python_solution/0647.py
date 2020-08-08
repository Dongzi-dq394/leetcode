class Solution:
    def countSubstrings(self, s: str) -> int:
        # Solution 1: DP (420ms: 27.23%)
        res, length = 0, len(s)
        dp = [[False for i in range(length)] for j in range(length)]
        for i in range(length):
            dp[i][i] = True
            res += 1
        for i in range(length-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res += 1
        for j in range(2, length):
            for i in range(j-2, -1, -1):
                dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j]:
                    res += 1
        return res