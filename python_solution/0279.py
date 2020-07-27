class Solution:
    def numSquares(self, n: int) -> int:
        # Solution 1 by meself: Backtracking (2040ms: 60%)
        candidates = {ele**2 for ele in range(1, int(math.sqrt(n))+1)}
        if n in candidates: return 1
        def backtrack(number, total):
            if total == 0 and number == 0:
                return True
            if total == 0 or number <= 0:
                return
            if number and total:
                for item in candidates:
                    if backtrack(number-1, total-item):
                        return True
        for i in range(2, n+1):
            if backtrack(i, n):
                return i
        
        # Solution 2: DP from discussion (4648ms: 36.17%) --> (4168ms: 48.20%)
        # Can be improved using candidates, don't need to calculate the math.sqrt(i)
        dp = [i for i in range(n+1)]
        candidates = [1]
        for i in range(1, n+1):
            if int(math.sqrt(i))**2 == i:
                dp[i] = 1
                candidates.append(i)
            else:
                # Logic when no candidates:
                # for j in range(1, int(math.sqrt(i))+1):
                #     dp[i] = min(dp[i], dp[i-j*j]+1)
                for j in candidates:
                    dp[i] = min(dp[i], dp[i-j]+1)
        return dp[n]
        
        # Solution 3: Math Using Lagrange 4 square theory (32ms: 97.71%)
        # Based on this theory, the result can only be 1,2,3,4
        # This is the most effective method!!!
        # 1. Check the 1 first
        # 2. Check n == 4^k * (8m+7) or not
        # 3. Check the 2
        # 4. The remaining cases are 3
        if int(math.sqrt(n))**2 == n:
            return 1
        temp = n
        while temp % 4 == 0:
            temp >>= 2
        if temp % 8 == 7:
            return 4
        for i in range(1, int(math.sqrt(n))+1):
            if int(math.sqrt(n-i*i))**2 == n-i*i:
                return 2
        return 3