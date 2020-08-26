class Solution:
    def integerBreak(self, n: int) -> int:
        # Solution 1: Normal DP (40ms: 48.21%)
        memo = {}
        def helper(n):
            if n==1:
                memo[n] = 1
                return 1
            if n in memo:
                return memo[n]
            temp = 0
            for i in range(1, n):
                temp = max(temp, i*helper(n-i))
            memo[n] = max(temp, n)
            return temp
        return helper(n)
        
        # Solution 2: from discussion --> Pure Math (28ms: 91.26%)
        # Only need to consider 2 and 3
        res = 1
        if n==2: return 1
        if n==3: return 2
        while n>4:
            n -= 3
            res *= 3
        return res*n