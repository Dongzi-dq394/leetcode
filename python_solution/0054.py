class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        directions = [1, 1, -1, -1]
        s_y, s_x = -1, 0
        choice = 0
        while len(res) < len(matrix)*len(matrix[0]):
            choice = choice % 4
            if choice == 0 or choice == 2:
                while 0 <= s_y+directions[choice] < len(matrix[0]):
                    if matrix[s_x][s_y+directions[choice]] != 'v':
                        s_y = s_y + directions[choice]
                        res.append(matrix[s_x][s_y])
                        matrix[s_x][s_y] = 'v'
                    else:
                        break
            else:
                while 0 <= s_x+directions[choice] < len(matrix):
                    if matrix[s_x+directions[choice]][s_y] != 'v':
                        s_x = s_x + directions[choice]
                        res.append(matrix[s_x][s_y])
                        matrix[s_x][s_y] = 'v'
                    else:
                        break
            choice += 1
        return res