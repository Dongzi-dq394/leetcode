class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Solution 1: Recursion and Divide_Conquer (108ms: 5.84%)
        if not matrix or not matrix[0]: return False
        height, width = len(matrix), len(matrix[0])
        if height == 1 and width == 1: return matrix[0][0] == target
        mid_h, mid_w = (height-1)//2, (width-1)//2
        
        matrix1 = [[matrix[i][j] for j in range(mid_w+1)] for i in range(mid_h+1)]
        matrix2 = [[matrix[i][j] for j in range(mid_w+1, width)] for i in range(mid_h+1)]
        matrix3 = [[matrix[i][j] for j in range(mid_w+1)] for i in range(mid_h+1, height)]
        matrix4 = [[matrix[i][j] for j in range(mid_w+1, width)] for i in range(mid_h+1, height)]
        
        if matrix[mid_h][mid_w] == target: return True
        elif matrix[mid_h][mid_w] > target:
            return self.searchMatrix(matrix1, target) or self.searchMatrix(matrix2, target) or self.searchMatrix(matrix3, target)
        else:
            return self.searchMatrix(matrix2, target) or self.searchMatrix(matrix3, target) or self.searchMatrix(matrix4, target)
        
        # Solution 2: Zig-Zag --> from discussion (O(M+N), 40ms: 70%)
        if not matrix: return False
        i, j = 0, len(matrix[0])-1
        while i<len(matrix) and j>=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False