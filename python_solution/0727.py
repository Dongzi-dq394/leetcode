class Solution:
    def minWindow(self, S: str, T: str) -> str:
        # Solution from Discussion: DP (160ms: 86.79%)
        ls, lt = len(S), len(T)
        
        dic = defaultdict(list)
        for i, char in enumerate(T):
            dic[char].append(i)
        
        dp = [-1 for _ in range(lt)]
        
        length = ls+1
        start = -1
        
        for ind, char in enumerate(S):
            if char in dic:
                for pos in dic[char][::-1]:
                    if pos == 0:
                        dp[pos]=ind
                    else:
                        dp[pos] = dp[pos-1]
                    if pos==lt-1 and dp[pos]!=-1 and ind-dp[pos]+1<length:
                        length = ind-dp[pos]+1
                        start = dp[pos]
        if dp[lt-1]==-1:
            return ''
        return S[start:start+length]