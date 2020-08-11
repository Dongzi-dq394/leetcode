class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # New Solution: Binary Search (36ms: 61.20%)
        neg = (dividend>=0) != (divisor>=0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp = divisor
            pos = -1
            while dividend>=temp:
                pos += 1
                temp += temp
            res += (1<<pos)
            dividend -= (temp>>1)
        if neg:
            res = -res
        return (1<<31)-1 if res >= (1<<31) else res