class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # New Solution: Hash Table for the numerator (24ms: 95.85%)
        if numerator%denominator==0:
            return str(numerator//denominator)
        neg = (numerator>=0) != (denominator>=0)
        numerator, denominator = abs(numerator), abs(denominator)
        res = str(numerator//denominator)+'.'
        remain = ''
        numerator %= denominator
        dic = {}
        start = 0
        while numerator:
            if numerator not in dic:
                dic[numerator] = start
                start += 1
                numerator *= 10
                remain += str(numerator//denominator)
                numerator %= denominator
            else:
                remain = remain[:dic[numerator]] + '(' + remain[dic[numerator]:] + ')'
                break
        return res + remain if not neg else '-' + res + remain