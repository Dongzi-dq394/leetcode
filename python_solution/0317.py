class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # Solution by myself: BFS (892ms: 40.21%)
        height, width = len(grid), len(grid[0])
        one_set = []
        distance = defaultdict(dict)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        def bfs(ci, cj):
            queue = deque([(ci, cj, 0)])
            visited = {(ci, cj):True}
            while queue:
                cur_i, cur_j, cur_dis = queue.popleft()
                distance[(ci, cj)][(cur_i, cur_j)] = cur_dis
                for di, dj in directions:
                    new_i, new_j = cur_i+di, cur_j+dj
                    if 0<=new_i<len(grid) and 0<=new_j<len(grid[0]) and grid[new_i][new_j]==0 and (new_i, new_j) not in visited:
                        visited[(new_i, new_j)] = True
                        queue.append((new_i, new_j, cur_dis+1))
        for i in range(height):
            for j in range(width):
                if grid[i][j]==1:
                    one_set.append((i, j))
                    bfs(i, j)
        
        res = float('Inf')
        for i in range(height):
            for j in range(width):
                if grid[i][j]==0:
                    temp = 0
                    flag = True
                    for ci, cj in one_set:
                        if (i, j) not in distance[(ci, cj)]:
                            flag = False
                            break
                        temp += distance[(ci, cj)][(i, j)]
                    #print(i, j, temp)
                    if flag:
                        res = min(res, temp)
        return res if res!=float('Inf') else -1