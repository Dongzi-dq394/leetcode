class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # Solution by myself: MinHeap (588ms: 71.51%)
        h = []
        for slot in slots1:
            heappush(h, slot)
        for slot in slots2:
            heappush(h, slot)
        s, e = heappop(h)
        while h:
            news, newe = heappop(h)
            if news>=e:
                s, e = news, newe
            else:
                if min(e, newe)-news>=duration:
                    return [news, news+duration]
                else:
                    if e<newe:
                        s, e = news, newe
        return []