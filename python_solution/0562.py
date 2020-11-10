class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        # Solution 1: Brute-force to the array (612ms: 26.17%)
        if not M or not M[0]: return 0
        height, width = len(M), len(M[0])
        flag = [[[0, 0, 0, 0] for _ in range(width)] for _ in range(height)]
        res = 0
        # There should be four directions!!
        directions = [[0, 1], [1, 0], [1, 1], [1, -1]]
        def helper(i, j, k):
            nonlocal res
            di, dj = directions[k]
            ans = 0
            while 0<=i<height and 0<=j<width:
                if M[i][j]==1:
                    ans += 1
                    flag[i][j][k] = 1
                    i, j = i+di, j+dj
                else:
                    break
            res = max(res, ans)
        for i in range(height):
            for j in range(width):
                if M[i][j]==1:
                    for k in range(4):
                        if flag[i][j][k]==0:
                            helper(i, j, k)
        return res
        
        # Solution 2 from Hint: DP (444ms: 71.35%)
        if not M or not M[0]: return 0
        res = 0
        height, width = len(M), len(M[0])
        dp = [[[0, 0, 0, 0] for _ in range(width+1)] for _ in range(height+1)]
        for i in range(1, height+1):
            for j in range(1, width+1):
                if M[i-1][j-1]==1:
                    dp[i][j][0] = dp[i][j-1][0]+1
                    dp[i][j][1] = dp[i-1][j][1]+1
                    dp[i][j][2] = dp[i-1][j-1][2]+1
                    if j<width:
                        dp[i][j][3] = dp[i-1][j+1][3]+1
                    else:
                        dp[i][j][3] = 1
                    res = max(res, max(dp[i][j]))
        return res