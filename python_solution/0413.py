class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # Solution from myself: 2D DP (2988ms: 5.22%)
        # So Slow!!!
        length = len(A)
        if length<3: return 0
        res = 0
        dp = [[False for _ in range(length)] for _ in range(length)]
        for i in range(length-2):
            if A[i]+A[i+2] == 2*A[i+1]:
                dp[i][i+2] = True
                res += 1
        for j in range(3, length):
            for i in range(j-3, -1, -1):
                dp[i][j] = (dp[i+1][j] and dp[i][j-1])
                if dp[i][j]:
                    res += 1
        return res
        
        # Solution from discussion: 1D DP (36ms: 86.14%)
        dp = [0]*len(A)
        for i in range(2, len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i] = dp[i-1]+1
        return sum(dp)