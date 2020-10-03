class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Solution by myself: BFS in each GATE (TLE!!!)
        '''
        if not rooms: return
        height, width = len(rooms), len(rooms[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        def bfs(i, j):
            visited = {(i, j):True}
            queue = deque([(i, j, 0)])
            while queue:
                curi, curj, dis = queue.popleft()
                rooms[curi][curj] = min(rooms[curi][curj], dis)
                for di, dj in directions:
                    newi, newj = curi+di, curj+dj
                    if 0<=newi<len(rooms) and 0<=newj<len(rooms[0]) and (newi, newj) not in visited and rooms[newi][newj]!=-1:
                        visited[(newi, newj)] = True
                        queue.append((newi, newj, dis+1))
        for i in range(height):
            for j in range(width):
                if rooms[i][j]==0:
                    bfs(i, j)
        '''
        # Solution from Solution: BFS for all the GATE together!! (260ms: 91.85%)
        if not rooms: return
        INF = (1<<31)-1
        height, width = len(rooms), len(rooms[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        queue = deque([])
        for i in range(height):
            for j in range(width):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        while queue:
            curi, curj = queue.popleft()
            for di, dj in directions:
                newi, newj = curi+di, curj+dj
                if 0<=newi<len(rooms) and 0<=newj<len(rooms[0]) and rooms[newi][newj]==INF:
                    rooms[newi][newj] = rooms[curi][curj]+1
                    queue.append((newi, newj))