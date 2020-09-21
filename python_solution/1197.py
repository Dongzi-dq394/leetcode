class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        memo = {}
        def helper(x, y):
            x, y = abs(x), abs(y)
            if (x, y) in memo:
                return memo[(x, y)]
            if x+y==0:
                return 0
            if x+y==2:
                return 2
            temp = min(helper(x-1, y-2), helper(x-2, y-1)) + 1
            memo[(x, y)] = temp
            return temp
        return helper(x, y)