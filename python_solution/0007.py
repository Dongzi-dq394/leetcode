class Solution:
    def reverse(self, x: int) -> int:
        # solution 1:
        # this solution is using the built-in function of python
        '''
        sign = 1
        if x < 0:
            sign = -1
        up, down = (1 << 31) - 1, -(1 << 31)
        result = sign * int(str(abs(x))[::-1])
        return result if down <= result <= up else 0
        '''
        # solution 2:
        # this solution uses the normal math method
        up, down = (1 << 31) - 1, -(1 << 31)
        temp, result = abs(x), 0
        while temp != 0:
            result = result * 10 + temp % 10
            temp //= 10
        if x >= 0 and result <= up: return result
        if x < 0 and -result >= down: return -result
        return 0