class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Old Solution: DFS (448ms: 87.22%)
        def dfs(i, j):
            if dp[i][j]==0:
                temp = 0
                if i-1>=0 and matrix[i][j]>matrix[i-1][j]:
                    temp = max(temp, dfs(i-1, j))
                if i+1<len(matrix) and matrix[i][j]>matrix[i+1][j]:
                    temp = max(temp, dfs(i+1, j))
                if j-1>=0 and matrix[i][j]>matrix[i][j-1]:
                    temp = max(temp, dfs(i, j-1))
                if j+1<len(matrix[0]) and matrix[i][j]>matrix[i][j+1]:
                    temp = max(temp, dfs(i, j+1))
                dp[i][j] = temp+1
                return temp+1
            else:
                return dp[i][j]
        if not matrix or not matrix[0]: return 0
        height, width = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(width)] for _ in range(height)]
        for i in range(height):
            for j in range(width):
                dfs(i, j)
        res = 0
        for i in range(height):
            for j in range(width):
                res = max(res, dp[i][j])
        return res
        
        # New Solution: Topological Sort (588ms: 50.94%)
        if not matrix: return 0
        height, width = len(matrix), len(matrix[0])
        degree = [[0 for _ in range(width)] for _ in range(height)]
        path = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = deque()
        res = 0
        
        for i in range(height):
            for j in range(width):
                for dx, dy in path:
                    if 0<=i+dx<height and 0<=j+dy<width:
                        if matrix[i+dx][j+dy]>matrix[i][j]:
                            degree[i][j] += 1
        for i in range(height):
            for j in range(width):
                if degree[i][j] == 0:
                    queue.append([i, j])
        while queue:
            length = len(queue)
            for i in range(length):
                x, y = queue.popleft()
                for dx, dy in path:
                    if 0<=x+dx<height and 0<=y+dy<width:
                        if matrix[x+dx][y+dy]<matrix[x][y]:
                            degree[x+dx][y+dy] -= 1
                            if degree[x+dx][y+dy] == 0:
                                queue.append([x+dx, y+dy])
            res += 1
        return res