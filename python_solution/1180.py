class Solution:
    def countLetters(self, S: str) -> int:
        start = res = 0
        S += ' '
        for i in range(len(S)):
            if S[i]!=S[start]:
                res += (i-start)*(i-start+1)//2
                start = i
        return res