# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # Solution 1: Binary Search (100ms: 81.08%)
        height, width = binaryMatrix.dimensions()
        l, r = 0, width-1
        while l<=r:
            mid = (l+r)//2
            flag = False
            for i in range(height):
                if binaryMatrix.get(i, mid)==1:
                    flag = True
                    r = mid - 1
                    break
            if not flag:
                l = mid + 1
        return -1 if r==width-1 else r+1
        
        # Solution from Discussion: Linear-walk (100ms)
        h, w = binaryMatrix.dimensions()
        i, j = 0, w-1
        res = -1
        while i<h and j>=0:
            if binaryMatrix.get(i, j)==1:
                res = j
                j -= 1
            else:
                i += 1
        return res