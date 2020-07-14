class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        if length <= 1: return
        if length % 2 == 0:
            for i in range(length//2):
                for j in range(length//2):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[length-1-j][i]
                    matrix[length-1-j][i] = matrix[length-1-i][length-1-j]
                    matrix[length-1-i][length-1-j] = matrix[j][length-1-i]
                    matrix[j][length-1-i] = temp
        else:
            for i in range(length//2):
                for j in range(length//2 + 1):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[length-1-j][i]
                    matrix[length-1-j][i] = matrix[length-1-i][length-1-j]
                    matrix[length-1-i][length-1-j] = matrix[j][length-1-i]
                    matrix[j][length-1-i] = temp