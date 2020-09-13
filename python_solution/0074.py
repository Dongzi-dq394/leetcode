class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Solution 1: Binary Search for both column and row (60ms: 96.63%)
        if not matrix or not matrix[0]: return False
        
        up, down = 0, len(matrix)-1
        while up<=down:
            middle = (up+down)//2
            if target==matrix[middle][0]:
                return True
            elif target>matrix[middle][0]:
                up = middle+1
            else:
                down = middle-1
        
        left, right = 0, len(matrix[0])-1
        while left<=right:
            middle = (left+right)//2
            if matrix[down][middle]==target:
                return True
            elif target>matrix[down][middle]:
                left = middle+1
            else:
                right = middle-1
        
        return False