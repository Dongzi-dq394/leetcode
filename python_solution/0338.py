class Solution:
    def countBits(self, num: int) -> List[int]:
        # Solution 1 by myself: find the pattern (88ms: 72.54%)
        res = []
        start = 2
        while start-1<=num:
            if start==2:
                res.append(1)
            else:
                temp = []
                for i in res:
                    temp.append(i+1)
                res = res + [1] + temp
            start <<= 1
        remain = num-(start>>1)
        if remain < 0: return [0]+res
        temp = []
        for i in range(remain):
            temp.append(res[i]+1)
        res = res + [1] + temp
        return [0]+res
        
        # Solution 2: DP from discussion (60ms)
        dp = [0]*(num+1)
        for i in range(1, num+1):
            dp[i] = dp[i>>1] + (1 if i&1==1 else 0)
        return dp
        
        # Solution 3: More simple pattern from discussion (104ms: 51.13%)
        res = [0]
        while len(res)<num+1:
            length = len(res)
            for i in range(length):
                res.append(res[i]+1)
        return res[:num+1]