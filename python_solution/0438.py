class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        total = len(p)
        start = 0
        res = []
        for i in range(len(s)):
            if s[i] not in count:
                total += (i-start)
                for j in range(start, i):
                    count[s[j]] += 1
                start = i+1
            else:
                if count[s[i]]>0:
                    count[s[i]] -= 1
                    total -= 1
                    if total==0:
                        res.append(start)
                        count[s[start]] += 1
                        total += 1
                        start += 1
                else:
                    j = start
                    while j<i:
                        if s[j]!=s[i]:
                            count[s[j]] += 1
                            total += 1
                            j += 1
                        else:
                            break
                    start = j+1
        return res
                    