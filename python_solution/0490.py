class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # Solution from Solution: DFS (268ms: 97.01%)
        # Very Interesting!
        # The ball might move more than one steps until hit the walls.
        visited = {}
        def dfs(i, j):
            if (i, j) in visited: return False
            if i==destination[0] and j==destination[1]: return True
            visited[(i, j)] = True
            l, r, u, b = j-1, j+1, i-1, i+1
            while l>=0 and maze[i][l]==0:
                l -= 1
            if dfs(i, l+1): return True
            while r<len(maze[0]) and maze[i][r]==0:
                r += 1
            if dfs(i, r-1): return True
            while u>=0 and maze[u][j]==0:
                u -= 1
            if dfs(u+1, j): return True
            while b<len(maze) and maze[b][j]==0:
                b += 1
            if dfs(b-1, j): return True
            return False
        return dfs(start[0], start[1])