class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        # Solution by myself: Bruteforce (264ms: 26.56%)
        if not s or not dict: return s
        l = r = None
        res = []
        for i in range(len(s)):
            for item in dict:
                length = len(item)
                if length+i<=len(s) and s[i:length+i]==item:
                    if r==None:
                        l, r = i, length+i
                    else:
                        if i>r:
                            res.append((l, r))
                            l, r = i, length+i
                        else:
                            r = max(r, length+i)
        if r!=None:
            res.append((l, r))
        if not res: return s
        ans = s[:res[0][0]]
        for i in range(len(res)-1):
            l, r = res[i]
            ans += '<b>'
            ans += s[l:r]
            ans += '</b>'
            ans += s[r:res[i+1][0]]
        ans += '<b>'
        ans += s[res[-1][0]:res[-1][1]]
        ans += '</b>'
        ans += s[res[-1][1]:]
        return ans
        
        # Solution from discussion: More tricky bruteforce (48ms: 95.60%)
        # Take advantage of find() function in Python.
        # Also use masked!!
        masked = [0]*len(s)
        for item in dict:
            pos = s.find(item)
            while pos!=-1:
                for i in range(pos, pos+len(item)):
                    masked[i] = 1
                pos = s.find(item, pos+1)
        masked = [0]+masked+[0]
        res = ''
        for i in range(1, len(masked)-1):
            if masked[i]==1 and masked[i-1]==0:
                res += '<b>'
            res += s[i-1]
            if masked[i]==1 and masked[i+1]==0:
                res += '</b>'
        return res