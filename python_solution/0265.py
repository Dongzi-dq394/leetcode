class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # Solution 1: DP with trick (100ms: 94.91%)
        if not costs or not costs[0]: return 0
        m1, m2 = 0, None
        height, width = len(costs), len(costs[0])
        for i in range(1, width):
            if costs[0][i]<costs[0][m1]:
                m1, m2 = i, m1
            else:
                if m2 == None:
                    m2 = i
                else:
                    if costs[0][i]<costs[0][m2]:
                        m2 = i
        for i in range(1, height):
            for j in range(width):
                if j!=m1:
                    costs[i][j] += costs[i-1][m1]
                else:
                    costs[i][j] += costs[i-1][m2]
            t1, t2 = 0, None
            for j in range(1, width):
                if costs[i][j]<costs[i][t1]:
                    t1, t2 = j, t1
                else:
                    if t2==None:
                        t2 = j
                    else:
                        if costs[i][j]<costs[i][t2]:
                            t2 = j
            m1, m2 = t1, t2
        return min(costs[-1])