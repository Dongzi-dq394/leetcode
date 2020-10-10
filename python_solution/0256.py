class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        for i in range(1, len(costs)):
            for j in range(3):
                last = float('Inf')
                for k in range(3):
                    if k!=j:
                        last = min(last, costs[i-1][k])
                costs[i][j] += last
        return min(costs[-1])