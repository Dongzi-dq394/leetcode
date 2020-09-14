class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # Solution by myself: Memoization (192ms: 47.69%)
        memo = {}
        def helper(m, n, remain, i, j):
            if (remain, i, j) in memo:
                return memo[(remain, i, j)]
            if remain==0:
                if i>=0 and i<m and j>=0 and j<n:
                    return 0
                else:
                    return 1
            if i<0 or j<0 or i>=m or j>=n:
                return 1
            res = 0
            res += helper(m, n, remain-1, i-1, j)
            res += helper(m, n, remain-1, i+1, j)
            res += helper(m, n, remain-1, i, j-1)
            res += helper(m, n, remain-1, i, j+1)
            memo[(remain, i, j)] = res
            return res
        return helper(m, n, N, i, j)%1000000007