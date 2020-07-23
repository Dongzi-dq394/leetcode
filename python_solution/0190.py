class Solution:
    def reverseBits(self, n: int) -> int:
        # Solution 1: Bit by Bit
        res, exponent = 0, 31
        while n:
            res += (n&1)<<exponent
            n >>= 1
            exponent -= 1
        return res
        
        # Solution 2: Mask and Shift
        # More like the Divide and Conquer
        n = (n<<16) | (n>>16)
        n = ((n & 0xff00ff00)>>8) | ((n & 0x00ff00ff)<<8)
        n = ((n & 0xf0f0f0f0)>>4) | ((n & 0x0f0f0f0f)<<4)
        n = ((n & 0xcccccccc)>>2) | ((n & 0x33333333)<<2)
        n = ((n & 0xaaaaaaaa)>>1) | ((n & 0x55555555)<<1)
        return n