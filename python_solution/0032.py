class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Solution 1: DP (36ms: 97.55%)
        if not s: return 0
        dp = [0] * (len(s)+1)
        for i in range(2, len(s)+1):
            if s[i-1] == ')':
                if i-1-dp[i-1] > 0:
                    if s[i-2-dp[i-1]] == '(':
                        dp[i] = 2 + dp[i-1] + dp[i-2-dp[i-1]]
        return max(dp)
        
        # Solution 2: Stack from Solution (40ms: 92.20%)
        res = 0
        stack = [-1]
        for i, char in enumerate(s):
            if char=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i-stack[-1])
        return res
        
        # Solution 3: Adaption from previous one without extra space (56ms: 47.38%)
        # A little slower might due to two-way traverse --> very smart!!!
        left = right = 0
        res = 0
        for i in range(len(s)):
            if s[i]=='(':
                left += 1
            if s[i]==')':
                right += 1
            if left==right:
                res = max(res, right*2)
            elif left<right:
                left = right = 0
        left = right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i]=='(':
                left += 1
            if s[i]==')':
                right += 1
            if left==right:
                res = max(res, right*2)
            elif left>right:
                left = right = 0
        return res