class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = set([len(item) for item in wordDict])
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for l in length:
                if i-l+1>=0:
                    if s[i-l+1:i+1] in wordDict:
                        dp[i+1] = dp[i+1-l]
                        if dp[i+1] == True:
                            break
        return dp[-1]