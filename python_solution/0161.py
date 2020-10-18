class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s==t: return False
        if abs(len(s)-len(t))>1: return False
        if len(s)==len(t):
            for i in range(len(s)):
                if s[i]!=t[i]:
                    start = i
                    break
            for i in range(start+1, len(s)):
                if s[i]!=t[i]:
                    return False
            return True
        else:
            if len(s)==0 or len(t)==0: return True
            if s[0]==t[0]:
                return self.isOneEditDistance(s[1:], t[1:])
            if s[-1]==t[-1]:
                return self.isOneEditDistance(s[:-1], t[:-1])
            return False