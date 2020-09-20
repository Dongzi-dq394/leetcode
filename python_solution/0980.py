class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        obstacles = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j]==1:
                    si, sj = i, j
                elif grid[i][j]==2:
                    ei, ej = i, j
                elif grid[i][j]==-1:
                    obstacles += 1
        res = 0
        def backtracking(i, j, num, target):
            nonlocal res
            if grid[i][j]==2:
                if len(num)==target:
                    res += 1
                return
            char = grid[i][j]
            grid[i][j] = '*'
            if i-1>=0 and grid[i-1][j] not in {'*', -1}:
                backtracking(i-1, j, num+[1], target)
            if i+1<len(grid) and grid[i+1][j] not in {'*', -1}:
                backtracking(i+1, j, num+[1], target)
            if j-1>=0 and grid[i][j-1] not in {'*', -1}:
                backtracking(i, j-1, num+[1], target)
            if j+1<len(grid[0]) and grid[i][j+1] not in {'*', -1}:
                backtracking(i, j+1, num+[1], target)
            grid[i][j] = char
        backtracking(si, sj, [], height*width-obstacles-1)
        return res