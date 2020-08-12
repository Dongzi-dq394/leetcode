class Solution:
    def mySqrt(self, x: int) -> int:
        # New Solution 1: Newton's way (28ms: 95.46%)
        if x==0: return 0
        old = 1
        while True:
            new = (old+x/old) / 2
            if abs(new-old)<1e-4:
                return int(new)
            old = new
        
        # New Solution 2: Binary Search(36ms: 75.57%)
        l, r = 0, x
        while l<=r:
            middle = (l+r)//2
            temp = middle*middle
            if temp==x:
                return middle
            elif temp>x:
                r = middle-1
            else:
                l = middle+1
        return r