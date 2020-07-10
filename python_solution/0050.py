class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        while n>0:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
        return res