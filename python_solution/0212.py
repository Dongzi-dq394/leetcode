class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        res = []
        # Build the trie
        for item in words:
            temp = trie
            for cha in item:
                if cha not in temp:
                    temp[cha] = {}
                temp = temp[cha]
            temp['*'] = item
            
        def search(i, j, node):
            c = board[i][j]
            board[i][j] = None
            if c in node:
                if '*' in node[c]:
                    if node[c]['*'] not in res:
                        res.append(node[c]['*'])
                        # Don't return here or the board[i][j] is '*'!!!
                # Even we find '*' in node[c], we still need to search
                # Because there might be another word starts with the previous word
                if i-1>=0:
                    search(i-1, j, node[c])
                if i+1<len(board):
                    search(i+1, j, node[c])
                if j-1>=0:
                    search(i, j-1, node[c])
                if j+1<len(board[0]):
                    search(i, j+1, node[c])
            board[i][j] = c
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                search(i, j, trie)
        return res