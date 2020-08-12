class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # New Solution: iteratively (24ms: 94.98%)
        if not matrix: return []
        height, width = len(matrix), len(matrix[0])
        total_num = height*width
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = []
        cur_num = i = 0
        si, sj = 0, -1
        while cur_num<total_num:
            [chi, chj] = directions[i]
            i = (i+1)%4
            while 0<=si+chi<height and 0<=sj+chj<width and matrix[si+chi][sj+chj] != '*':
                si += chi
                sj += chj
                res.append(matrix[si][sj])
                matrix[si][sj] = '*'
                cur_num += 1
        return res