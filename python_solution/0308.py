class NumMatrix:
    
    # Solution 1: DP for O(n^2) (1052ms: 23.30%)
    
    # From discussion, we can also use each row to store the 
    # cumulative sum to reach the O(n) time.

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]: return
        height, width = len(matrix), len(matrix[0])
        self.dp = [[0 for _ in range(width+1)] for _ in range(height+1)]
        self.record = [[0 for _ in range(width)] for _ in range(height)]
        for i in range(height):
            for j in range(width):
                self.record[i][j] = matrix[i][j]
                self.dp[i+1][j+1] = self.dp[i][j+1]+self.dp[i+1][j]-self.dp[i][j]+matrix[i][j]

    def update(self, row: int, col: int, val: int) -> None:
        origin = self.record[row][col]
        diff = val - origin
        self.record[row][col] = val
        for i in range(row, len(self.record)):
            for j in range(col, len(self.record[0])):
                self.dp[i+1][j+1] += diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1]-self.dp[row1][col2+1]-self.dp[row2+1][col1]+self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)