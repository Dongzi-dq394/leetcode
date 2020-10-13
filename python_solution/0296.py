class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # Solution by myself: BFS (TLE at the last case)
        '''
        height, width = len(grid), len(grid[0])
        dis = [[0 for _ in range(width)] for _ in range(height)]
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        def bfs(i, j):
            visited = {(i, j):True}
            queue = deque([(i, j, 0)])
            while queue:
                oi, oj, distance = queue.popleft()
                dis[oi][oj] += distance
                for di, dj in directions:
                    ni, nj = oi+di, oj+dj
                    if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and (ni, nj) not in visited:
                        queue.append((ni, nj, distance+1))
                        visited[(ni, nj)] = True
        for i in range(height):
            for j in range(width):
                if grid[i][j]==1:
                    bfs(i, j)
        #print(dis)
        res = float('Inf')
        for i in range(height):
            for j in range(width):
                res = min(res, dis[i][j])
        return res
        '''
        # Solution from Solution: Math + Sort (56ms: 98.45%)
        # Very tricky: take use of median
        rows = []
        cols = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    rows.append(i)
                    cols.append(j)
        row_center = rows[len(rows)//2]
        cols.sort()
        col_center = cols[len(cols)//2]
        res = 0
        for r in rows:
            res += abs(r-row_center)
        for c in cols:
            res += abs(c-col_center)
        return res