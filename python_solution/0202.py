class Solution:
    def calculate(self, n):
        res = 0
        while n:
            res += (n%10)**2
            n //= 10
        return res
    def isHappy(self, n: int) -> bool:
        dic = {}
        while True:
            n = self.calculate(n)
            if n==1:
                return True
            if n in dic:
                return False
            dic[n] = True
            