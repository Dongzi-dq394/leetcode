class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Something to learn from this problem:
        # 1. Using recursive method might be faster than the iterative way
        def bfs(i, j):
            stack = [[i, j]]
            while stack:
                # May not use pop(0) because it's so slow!!
                # TLE if using stack.pop(0)
                [x, y] = stack.pop()
                grid[x][y] = '0'
                if x-1>=0 and grid[x-1][y] == '1':
                    stack.append([x-1, y])
                if x+1<len(grid) and grid[x+1][y] == '1':
                    stack.append([x+1, y])
                if y-1>=0 and grid[x][y-1] == '1':
                    stack.append([x, y-1])
                if y+1<len(grid[0]) and grid[x][y+1] == '1':
                    stack.append([x, y+1])
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    bfs(i, j)
        return res
    