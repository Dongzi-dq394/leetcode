class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Solution 1: DP/DFS/Recursion + Memo (132ms: 79.88%)
        dic = set(stones)
        if stones[1]!=1: return False
        memo = {}
        def helper(pos, k):
            if pos==stones[-1]:
                memo[(pos, k)] = True
                return True
            if (pos, k) in memo:
                return memo[(pos, k)]
            for i in {1, 0, -1}:
                if k+i>0 and pos+k+i in dic:
                    if helper(pos+k+i, k+i):
                        memo[(pos, k)] = True # Important!
                        return True
            memo[(pos, k)] = False # Important!
            return False
        return helper(1, 1)