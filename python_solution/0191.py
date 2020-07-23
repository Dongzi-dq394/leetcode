class Solution:
    def hammingWeight(self, n: int) -> int:
        # Solution 1: Loop and Count
        res = 0
        while n:
            res += (n&1)
            n >>= 1
        return res
        
        # Solution 2: Bit Manipulation Trick
        # Each time n%(n-1), the right most 1 of n will be flipped to 0
        res = 0
        while n:
            res += 1
            n &= (n-1)
        return res