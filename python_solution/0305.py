class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # Solution 1: Union Find (512ms: 72.02%)
        if m==0 or n==0: return [0 for _ in range(len(positions))]
        res = []
        parent = [[(j, i) for i in range(n)] for j in range(m)]
        rank = [[0 for _ in range(n)] for _ in range(m)]
        def find(i, j):
            x, y = parent[i][j]
            if not (x==i and y==j):
                xx, yy = find(x, y)
                parent[i][j] = (xx, yy)
            return parent[i][j]
        def union(x1, y1, x2, y2):
            px1, py1 = find(x1, y1)
            px2, py2 = find(x2, y2)
            if px1==px2 and py1==py2: return False
            if rank[px1][py1]<rank[px2][py2]:
                parent[px1][py1] = (px2, py2)
                rank[px2][py2] += rank[px1][py1]
            else:
                parent[px2][py2] = (px1, py1)
                rank[px1][py1] += rank[px2][py2]
            return True
        total_number = 0
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for x, y in positions:
            # Check whether there is the island on (x, y)
            if rank[x][y]!=0:
                res.append(total_number)
            else:
                rank[x][y] = 1
                total_number += 1
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n:
                        if rank[nx][ny] > 0:
                            if union(x, y, nx, ny):
                                total_number -= 1
                res.append(total_number)
        return res