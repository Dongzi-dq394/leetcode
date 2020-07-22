class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        temp = 5
        while n >= temp:
            res += (n//temp)
            temp *= 5
        return res