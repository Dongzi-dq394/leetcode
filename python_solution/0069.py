class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        res = x / 2
        while True:
            temp = (res + x/res) / 2
            if abs(res-temp) < 1e-4:
                res = temp
                break
            else:
                res = temp
        return int(res)