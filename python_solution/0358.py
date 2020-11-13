class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # Solution from discussion: Heap (100ms: 65.36%)
        if k<=1: return s
        count = Counter(s)
        h = []
        for key in count:
            heappush(h, (-count[key], key))
        res = ''
        temp = []
        for i in range(len(s)):
            if i%k==0:
                for item in temp:
                    heappush(h, item)
                temp = []
            if not h:
                return ''
            times, char = heappop(h)
            res += char
            if times<-1:
                temp.append((times+1, char))
        return res