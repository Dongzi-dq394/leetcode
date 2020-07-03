class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            neg = 1
        else:
            neg = -1
        dividend, divisor = abs(dividend), abs(divisor)
        res, adv = 0, 1
        left, right = -(1<<31), (1<<31)-1
        
        while dividend >= divisor + divisor:
            temp = divisor
            while dividend >= temp + temp:
                adv += adv
                temp += temp
            res += adv
            adv = 1
            dividend -= temp
        
        if dividend >= divisor:
            res += 1
        return neg*res if right>=neg*res>=left else right