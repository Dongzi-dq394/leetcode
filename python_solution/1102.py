class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        # Solution 1 from discussion: Heap + Sort (1288ms: 70.41%)
        height, width = len(A), len(A[0])
        res = A[0][0]
        h = []
        heappush(h, (-A[0][0], 0, 0))
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        while h:
            cost, i, j = heappop(h)
            res = min(res, -cost)
            if i==height-1 and j==width-1:
                break
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<height and 0<=nj<width:
                    heappush(h, (-A[ni][nj], ni, nj))
                    A[ni][nj] = -1
        return res