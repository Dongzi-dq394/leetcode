class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return '0'
        if numerator % denominator == 0: return str(numerator//denominator)
        res = ''
        if (numerator>=0) != (denominator>=0):
            res += '-'
        numerator, denominator = abs(numerator), abs(denominator)
        res += str(numerator//denominator)
        res += '.'
        length = len(res)
        dic = {}
        
        numerator %= denominator
        while numerator > 0:
            if numerator in dic:
                res = res[:dic[numerator]] + '(' + res[dic[numerator]:length] + ')'
                return res
            else:
                dic[numerator] = length
                length += 1
                numerator *= 10
                res += str(numerator//denominator)
                numerator %= denominator
        return res