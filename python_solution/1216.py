class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # Solution from Hint: DP + Memo (528ms: 56.38%)
        # This is really a nice problem that we can reduce
        # it to a classic problem: remove some characters give
        # us a subsequence of s. So, we only need to find know
        # whether the longest palindrome subsequence is longer
        # then len(s)-k
        memo = {}
        def helper(l, r):
            if l>r: return 0
            if l==r:
                return 1
            if (l, r) in memo:
                return memo[(l, r)]
            if s[l]==s[r]:
                memo[(l, r)] = 2+helper(l+1, r-1)
            else:
                memo[(l, r)] = max(helper(l, r-1), helper(l+1, r))
            return memo[(l, r)]
        if helper(0, len(s)-1)>=len(s)-k:
            return True
        return False