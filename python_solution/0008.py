class Solution:
    def myAtoi(self, str: str) -> int:
        # Solution 1: (32ms: 86.94%)
        str = str.lstrip(' ')
        if not str:
            return 0
        start = 0 if (str[0]!='-' and str[0]!='+') else 1
        res = 0
        while start < len(str):
            if not str[start].isdigit():
                break
            res = res*10 + int(str[start])
            start += 1
        res = -res if str[0]=='-' else res
        if res>=(1<<31):
            return (1<<31)-1
        if res<-(1<<31):
            return -(1<<31)
        return res