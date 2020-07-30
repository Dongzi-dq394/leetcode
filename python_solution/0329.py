class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        def dfs(i, j):
            # This is important!
            # If dp[i][j]!=0, then the longest result from matrix[i][j] has been calculated
            if not dp[i][j]:
                temp = matrix[i][j]
                temp1 = dfs(i-1, j) if i>0 and matrix[i-1][j]>temp else 0
                temp2 = dfs(i+1, j) if i<len(matrix)-1 and matrix[i+1][j]>temp else 0
                temp3 = dfs(i, j-1) if j>0 and matrix[i][j-1]>temp else 0
                temp4 = dfs(i, j+1) if j<len(matrix[0])-1 and matrix[i][j+1]>temp else 0
                dp[i][j] = 1 + max(temp1, temp2, temp3, temp4)
            return dp[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(result, dp[i][j])
        return result