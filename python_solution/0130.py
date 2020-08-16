class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # New Solution: DFS on boarder (140ms: 89.07%)
        if not board or not board[0]: return
        def dfs(i, j):
            if board[i][j]=='O':
                board[i][j] = '*'
                if i-1>=0:
                    dfs(i-1, j)
                if i+1<len(board):
                    dfs(i+1, j)
                if j-1>=0:
                    dfs(i, j-1)
                if j+1<len(board[0]):
                    dfs(i, j+1)
        height, width = len(board), len(board[0])
        for i in range(width):
            if board[0][i]=='O':
                dfs(0, i)
            if board[height-1][i]=='O':
                dfs(height-1, i)
        for i in range(height):
            if board[i][0]=='O':
                dfs(i, 0)
            if board[i][width-1]=='O':
                dfs(i, width-1)
        for i in range(height):
            for j in range(width):
                if board[i][j]=='O':
                    board[i][j] = 'X'
                elif board[i][j]=='*':
                    board[i][j] = 'O'