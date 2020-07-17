class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        dp = [0]*len(s)
        dp.append(1)
        if s[-1] != '0':
            dp[-2] = 1
        for i in range(len(s)-2,-1,-1):
            if dp[i+1] == 0:
                if s[i] != '1' and s[i] != '2':
                    return 0
                else:
                    dp[i] = dp[i+2]
            else:
                if s[i] == '0':
                    dp[i] = 0
                else:
                    if 26>=int(s[i:i+2])>=10:
                        dp[i] = dp[i+1] + dp[i+2]
                    else:
                        dp[i] = dp[i+1]
        return dp[0]