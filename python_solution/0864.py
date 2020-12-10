class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # Solution from Discussion: BFS + MEMO (280ms: 86.44%)
        hei, wid = len(grid), len(grid[0])
        si = sj = state = 0
        for i in range(hei):
            for j in range(wid):
                if grid[i][j] == '@':
                    si, sj = i, j
                if grid[i][j] in 'abcdef':
                    state |= 1<<(ord(grid[i][j])-97)
        queue = deque([(si, sj, 0)])
        visited = {(si, sj, 0):True}
        level = 0
        while queue:
            length = len(queue)
            for k in range(length):
                i, j, temp = queue.popleft()
                if temp==state:
                    return level
                for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if 0<=ni<hei and 0<=nj<wid and grid[ni][nj] != '#':
                        if grid[ni][nj] in '.@':
                            if (ni, nj, temp) not in visited:
                                visited[(ni, nj, temp)] = True
                                queue.append((ni, nj, temp))
                        elif grid[ni][nj] in 'abcdef':
                            new_temp = temp | 1<<(ord(grid[ni][nj])-97)
                            if (ni, nj, new_temp) not in visited:
                                visited[(ni, nj, new_temp)] = True
                                queue.append((ni, nj, new_temp))
                        else:
                            if temp & 1<<(ord(grid[ni][nj])-65) != 0:
                                if (ni, nj, temp) not in visited:
                                    visited[(ni, nj, temp)] = True
                                    queue.append((ni, nj, temp))
            level += 1
        return -1