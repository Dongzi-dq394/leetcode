class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Solution 1: from discussion DP very complex!! (240ms: 57.18%)
        res = 0
        if not matrix: return res
        height, width = len(matrix), len(matrix[0])
        h = [0]*width
        l = [0]*width
        r = [width-1]*width
        for i in range(height):
            cur_l, cur_r = 0, width-1
            for j in range(width):
                if matrix[i][j] == '1':
                    h[j] += 1
                    l[j] = max(l[j], cur_l)
                else:
                    h[j] = 0
                    l[j] = 0
                    cur_l = j+1
            for j in range(width-1, -1, -1):
                if matrix[i][j] == '1':
                    r[j] = min(r[j], cur_r)
                else:
                    r[j] = width-1
                    cur_r = j-1
            for j in range(width):
                res = max(res, h[j]*(r[j]-l[j]+1))
        return res
        
        # Solution 2: Bit Manipulation (208ms: 86.29%)
        if not matrix: return 0
        number = [int(''.join(row), base=2) for row in matrix]
        res = 0
        for i in range(len(matrix)):
            start = -1
            for j in range(i, len(matrix)):
                start &= number[j]
                if start==0:
                    break
                width = 0
                temp = start
                while temp:
                    width += 1
                    temp &= (temp>>1)
                res = max(res, width*(j-i+1))
        return res
        
        # Solution 3: Adapted from 84 (240ms: 57.18%)
        if not matrix: return 0
        h = [0]*(len(matrix[0])+1)
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                h[j] = h[j]+1 if matrix[i][j]=='1' else 0
            stack = [-1]
            for j in range(len(matrix[0])+1):
                while stack and h[j]<h[stack[-1]]:
                    height = h[stack.pop()]
                    res = max(res, height*(j-1-stack[-1]))
                stack.append(j)
        return res