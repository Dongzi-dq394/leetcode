class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # New Solution 1: Use Memo!!! (44ms: 78.20%)
        # If I use the normal DP adapted from the previous problem, then TLE
        # The reason is when we use DP, we need to traverse all the length of s
        # While, when we use memo, then only some of them are useful.
        count = Counter(wordDict)
        memo = {}
        def helper(s):
            if not s:
                memo[s] = [""]
                return memo[s]
            if s in memo:
                return memo[s]
            res = []
            for i in range(1, len(s)+1):
                if s[:i] in count:
                    sub_res = helper(s[i:])
                    for item in sub_res:
                        temp = (s[:i]+' '+item).rstrip(' ')
                        res.append(temp)
            memo[s] = res
            return memo[s]
        return helper(s)