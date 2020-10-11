class Solution:
    def encode(self, s: str) -> str:
        # Solution from Discussion: DP (348ms: 34.40%)
        length = len(s)
        dp = [['' for _ in range(length)] for _ in range(length)]
        for j in range(length):
            for i in range(j, -1, -1):
                if j-i<4:
                    dp[i][j] = s[i:j+1]
                else:
                    dp[i][j] = s[i:j+1]
                    for k in range(i, j):
                        if len(dp[i][k])+len(dp[k+1][j])<len(dp[i][j]):
                            dp[i][j] = dp[i][k] + dp[k+1][j]
                    for k in range(i, j):
                        if (j-i+1)%(k-i+1)==0 and s[i:j+1].replace(s[i:k+1],'')=='':
                            temp = (j-i+1)//(k-i+1)
                            temp_res = str(temp)+'['+dp[i][k]+']'
                            if len(temp_res)<len(dp[i][j]):
                                dp[i][j] = temp_res
        return dp[0][length-1]