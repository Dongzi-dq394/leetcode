class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Solution by myself: DP (2548ms: 35.30%)
        p = s[::-1]
        length = len(s)
        dp = [0 for _ in range(length+1)]
        for i in range(length):
            new = [0 for _ in range(length+1)]
            for j in range(length):
                if p[i]==s[j]:
                    new[j+1] = dp[j]+1
                else:
                    new[j+1] = max(dp[j+1], new[j])
            dp = new
        return dp[length]
        
        # Solution from discussion: Memoization (1296ms: 81.37%)
        memo = {}
        def helper(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left>right:
                return 0
            if left==right:
                return 1
            if s[left]==s[right]:
                memo[(left, right)] = 2+helper(left+1, right-1)
                return memo[(left, right)]
            else:
                memo[(left, right)] = max(helper(left+1, right), helper(left, right-1))
                return memo[(left, right)]
        return helper(0, len(s)-1)