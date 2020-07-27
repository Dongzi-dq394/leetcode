class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def count_one(i, j):
            res = 0
            if i-1>=0:
                if board[i-1][j] in {1, '#'}: res += 1
                if j-1>=0:
                    if board[i-1][j-1] in {1, '#'}: res += 1
                if j+1<len(board[0]):
                    if board[i-1][j+1] in {1, '#'}: res += 1
            if j-1>=0:
                if board[i][j-1] in {1, '#'}: res += 1
            if j+1<len(board[0]):
                if board[i][j+1] in {1, '#'}: res += 1
            if i+1<len(board):
                if board[i+1][j] in {1, '#'}: res += 1
                if j-1>=0:
                    if board[i+1][j-1] in {1, '#'}: res += 1
                if j+1<len(board[0]):
                    if board[i+1][j+1] in {1, '#'}: res += 1
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    if count_one(i, j) == 3:
                        board[i][j] = '*'
                else:
                    temp = count_one(i, j)
                    if temp < 2 or temp > 3:
                        board[i][j] = '#'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '*':
                    board[i][j] = 1
                elif board[i][j] == '#':
                    board[i][j] = 0
            