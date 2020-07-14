class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        m, n = len(matrix), len(matrix[0])
        first_zero = other_zero = 0
        for i in range(n):
            if matrix[0][i] == 0:
                first_zero = 1
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    other_zero = 1
                    matrix[0][j] = 0
            if other_zero == 1:
                other_zero = 0
                for j in range(n):
                    matrix[i][j] = 0
        for i in range(n):
            if matrix[0][i] == 0:
                for j in range(1, m):
                    matrix[j][i] = 0
        if first_zero:
            for i in range(n):
                matrix[0][i] = 0