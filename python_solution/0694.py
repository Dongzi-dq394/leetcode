class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # Solution from hint: DFS/BFS + Hash Table (208ms: 92.74%)
        dic = defaultdict(int)
        height, width = len(grid), len(grid[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        def dfs(i, j):
            res = []
            queue = deque([(i, j)])
            while queue:
                curi, curj = queue.popleft()
                if grid[curi][curj]==1:
                    grid[curi][curj] = '*'
                    # This is important!
                    # Translate each island to the top-left corner!
                    res.append((curi-i, curj-j))
                    for di, dj in directions:
                        newi, newj = curi+di, curj+dj
                        if 0<=newi<len(grid) and 0<=newj<len(grid[0]) and grid[newi][newj]==1:
                            queue.append((newi, newj))
            res = tuple(res)
            dic[res] += 1
        for i in range(height):
            for j in range(width):
                if grid[i][j]==1:
                    dfs(i, j)
        return len(list(dic.keys()))