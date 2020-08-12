class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # New Solution: from discussion (36ms: 75.85%)
        length = len(matrix)
        for i in range(length-1):
            for j in range(length-i-1):
                change = length-1-(i+j)
                matrix[i][j], matrix[i+change][j+change] = matrix[i+change][j+change], matrix[i][j]
        for i in range(length//2):
            for j in range(length):
                matrix[i][j], matrix[length-1-i][j] = matrix[length-1-i][j], matrix[i][j]