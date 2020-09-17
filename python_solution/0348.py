class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.total = n
        self.COL = [0]*n
        self.ROW = [0]*n
        self.diagonal_left = 0
        self.diagonal_right = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player==1:
            self.ROW[row] += 1
            if self.ROW[row] == self.total:
                return 1
            self.COL[col] += 1
            if self.COL[col] == self.total:
                return 1
            if row==col:
                self.diagonal_left += 1
            if row+col==self.total-1:
                self.diagonal_right += 1
            if self.diagonal_left==self.total or self.diagonal_right==self.total:
                return 1
        else:
            self.ROW[row] -= 1
            if self.ROW[row] == -self.total:
                return 2
            self.COL[col] -= 1
            if self.COL[col] == -self.total:
                return 2
            if row==col:
                self.diagonal_left -= 1
            if row+col==self.total-1:
                self.diagonal_right -= 1
            if self.diagonal_left==-self.total or self.diagonal_right==-self.total:
                return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)