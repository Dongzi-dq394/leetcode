class Solution:
    def titleToNumber(self, s: str) -> int:
        digit = 0
        res = 0
        for i in range(len(s)-1, -1, -1):
            res += (ord(s[i])-64) * (26 ** digit)
            digit += 1
        return res