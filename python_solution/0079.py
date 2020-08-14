class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # New Solution 1: Backtracking (248ms: 98.19%)
        def backtracking(index, i, j):
            if board[i][j] != word[index]:
                return False
            if index==len(word)-1:
                return word[-1]==board[i][j]
            temp = board[i][j]
            board[i][j] = '*'
            if i-1>=0 and board[i-1][j]!='*':
                if backtracking(index+1, i-1, j):
                    return True
            if i+1<len(board) and board[i+1][j]!='*':
                if backtracking(index+1, i+1, j):
                    return True
            if j-1>=0 and board[i][j-1]!='*':
                if backtracking(index+1, i, j-1):
                    return True
            if j+1<len(board[0]) and board[i][j+1]!='*':
                if backtracking(index+1, i, j+1):
                    return True
            board[i][j] = temp
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtracking(0, i, j):
                        return True
        return False