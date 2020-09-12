class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # Solution from discussion: Very different DP (92ms: 75%)
        # Very tricky to avoid the repeat counting
        if not p: return 0
        dic = defaultdict(int)
        cont = 1
        dic[p[0]] = 1
        for i in range(1, len(p)):
            if (p[i-1]=='z' and p[i]=='a') or ord(p[i-1])+1==ord(p[i]):
                cont += 1
            else:
                cont = 1
            dic[p[i]] = max(dic[p[i]], cont)
        return sum(dic.values())