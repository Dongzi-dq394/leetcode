class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lens, lenp = len(s), len(p)
        if lenp == 0: return lens==0
        else:
            if lens == 0:
                return lenp%2==0 and p[1]=='*' and self.isMatch(s, p[2:])
            else:
                if lenp>=2 and p[1]=='*':
                    while s and (s[0]==p[0] or p[0]=='.'):
                        # very important!!
                        if self.isMatch(s, p[2:]):
                            return True
                        s = s[1:]
                    return self.isMatch(s, p[2:])
                else:
                    return (s[0]==p[0] or p[0]=='.') and self.isMatch(s[1:], p[1:])