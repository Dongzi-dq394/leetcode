class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # Solution by myself: Two Pointers for each column and each row + Hash Table (216ms: 60.33%)
        height, width = len(board), len(board[0])
        new = [[0 for _ in range(width)] for _ in range(height)]
        zero_ind = defaultdict(dict)
        flag = False
        
        for i in range(height):
            l, r = 0, width-1
            while True:
                temp = 1
                while l<r and board[i][l]==board[i][l+1] and board[i][l]!=0:
                    temp += 1
                    l += 1
                l += 1
                if temp>=3:
                    flag = True
                    for j in range(l-temp, l):
                        zero_ind[j][i] = True
                temp = 1
                while l<r and board[i][r]==board[i][r-1] and board[i][r]!=0:
                    r -= 1
                    temp += 1
                r -= 1
                if temp>=3:
                    flag = True
                    for j in range(r+1, r+temp+1):
                        zero_ind[j][i] = True
                if r-l<2:
                    break
        for i in range(width):
            l, r = 0, height-1
            while True:
                temp = 1
                while l<r and board[l][i]==board[l+1][i] and board[l][i]!=0:
                    temp += 1
                    l += 1
                l += 1
                if temp>=3:
                    flag = True
                    for j in range(l-temp, l):
                        zero_ind[i][j] = True
                temp = 1
                while l<r and board[r][i]==board[r-1][i] and board[r][i]!=0:
                    temp += 1
                    r -= 1
                r -= 1
                if temp>=3:
                    flag = True
                    for j in range(r+1, r+temp+1):
                        zero_ind[i][j] = True
                if r-l<2:
                    break
        if not flag:
            return board
        for j in range(width):
            ind = height-1
            for i in range(height-1, -1, -1):
                if i not in zero_ind[j]:
                    new[ind][j] = board[i][j]
                    ind -= 1
        return self.candyCrush(new)