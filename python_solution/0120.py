class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Solution 1: DP --> from top to bottom (56ms: 94.65%)
        if not triangle: return 0
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][i] += triangle[i-1][i-1]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])
        
        # Solution 2: DP --> from bottom to top (60ms: 85.70%)
        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]