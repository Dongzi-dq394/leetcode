class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        # Solution 1: Array + Brute Force (320ms: 87.53%)
        if not grid or not grid[0]: return 0
        height, width = len(grid), len(grid[0])
        res = [[0 for _ in range(width)] for _ in range(height)]
        for i in range(height):
            numE = 0
            start = 0
            for j in range(width):
                if grid[i][j]=='E':
                    numE += 1
                if grid[i][j]=='W':
                    for k in range(start, j):
                        if grid[i][k]=='0':
                            res[i][k] += numE
                    numE = 0
                    start = j+1
            for k in range(start, width):
                if grid[i][k]=='0':
                    res[i][k] += numE
        for j in range(width):
            numE = 0
            start = 0
            for i in range(height):
                if grid[i][j]=='E':
                    numE += 1
                if grid[i][j]=='W':
                    for k in range(start, i):
                        if grid[k][j]=='0':
                            res[k][j] += numE
                    numE = 0
                    start = i+1
            for k in range(start, height):
                if grid[k][j]=='0':
                    res[k][j] += numE
        ans = 0
        for i in range(height):
            for j in range(width):
                ans = max(ans, res[i][j])
        return ans