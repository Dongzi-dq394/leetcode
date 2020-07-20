class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        height, width = len(board), len(board[0])
        
        def bfs():
            while stack:
                [x, y] = stack.pop(0)
                board[x][y] = '*'
                if x-1>=0 and board[x-1][y] == 'O':
                    stack.append([x-1, y])
                if x+1<height and board[x+1][y] == 'O':
                    stack.append([x+1, y])
                if y-1>=0 and board[x][y-1] == 'O':
                    stack.append([x, y-1])
                if y+1<width and board[x][y+1] == 'O':
                    stack.append([x, y+1])
            return
        
        stack = []
        for i in range(width):
            if board[0][i] == 'O':
                stack.append([0, i])
            if board[height-1][i] == 'O':
                stack.append([height-1, i])
        for i in range(height):
            if board[i][0] == 'O':
                stack.append([i, 0])
            if board[i][width-1] == 'O':
                stack.append([i, width-1])
        bfs()
        
        for i in range(height):
            for j in range(width):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'