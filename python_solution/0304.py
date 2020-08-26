class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.ele = []
            return
        height, width = len(matrix), len(matrix[0])
        self.ele = [[0 for _ in range(width+1)] for _ in range(height+1)]
        for i in range(1, height+1):
            for j in range(1, width+1):
                self.ele[i][j] = self.ele[i-1][j]+self.ele[i][j-1]-self.ele[i-1][j-1]+matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.ele[row2+1][col2+1]-self.ele[row1][col2+1]-self.ele[row2+1][col1]+self.ele[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)