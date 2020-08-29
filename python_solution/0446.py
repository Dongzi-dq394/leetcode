class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # Solution from Solution: DP + Hash Table (900ms: 64.47%)
        # can use: dp=[defaultdict(int) for _ in range(len(A))]
        
        # Something to learn:
        # [{}]*n != [{} for _ in range(n)]
        
        dp = [None]*len(A)
        res = 0
        for i in range(len(A)):
            dp[i] = defaultdict(int)
            for j in range(i):
                diff = A[i]-A[j]
                pre = dp[j][diff]
                res += pre
                dp[i][diff] += (pre+1)
        return res