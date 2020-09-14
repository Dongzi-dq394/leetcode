class Solution:
    def checkRecord(self, n: int) -> int:
        # Solution by myself: Memoization (TLE!!)
        '''
        memo = {}
        def checker(left, right, left_cont):
            if (left, left_cont) in memo:
                return memo[(left, left_cont)]
            if left==right:
                res = 1
                if left_cont<2:
                    res += 1
                memo[(left, left_cont)] = res
                return res
            res = checker(left+1, right, 0)
            if left_cont<2:
                res += checker(left+1, right, left_cont+1)
            memo[(left, left_cont)] = res
            return res
        def helper(left, right, A, left_cont):
            if (left, A, left_cont) in memo:
                return memo[(left, A, left_cont)]
            if A==0:
                return checker(left, right, left_cont)
            if left==right:
                res = 1
                if A:
                    res += 1
                if left_cont<2:
                    res += 1
                memo[(left, A, left_cont)] = res
                return res
            res = 0
            res += helper(left+1, right, A, 0)
            if A:
                res += helper(left+1, right, A-1, 0)
            if left_cont<2:
                res += helper(left+1, right, A, left_cont+1)
            memo[(left, A, left_cont)] = res
            return res
        return helper(1, n, 1, 0)%1000000007
        '''
        # Solution from discussion: DP (836ms: 84.04%)
        P = [0]*(n+1)
        PL = [0]*(n+1)
        P[0] = P[1] = 1
        PL[0], PL[1] = 1, 2
        for i in range(2, n+1):
            P[i] = PL[i-1]
            PL[i] = (P[i] + P[i-1] + P[i-2])%1000000007
        res = PL[n]
        for i in range(n):
            res += PL[i]*PL[n-i-1]
        return res%1000000007