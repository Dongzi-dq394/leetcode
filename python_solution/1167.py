class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # Solution by myself: Heap + Greedy (316ms: 95.66%)
        if len(sticks)<=1: return 0
        h = []
        res = 0
        for s in sticks:
            heappush(h, s)
        while len(h)>=2:
            t1 = heappop(h)
            t2 = heappop(h)
            res += (t1+t2)
            heappush(h, t1+t2)
        return res