class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Solution 1: Slicing (388ms)
        s[:] = s[::-1]
        
        # Solution 2: iterative (212ms: 73.24%)
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]
        
        # Solution 3: Built-in function (228ms: 30%)
        s.reverse()