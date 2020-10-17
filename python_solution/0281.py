class ZigzagIterator:
    # Solution 1: Array (40ms: 99.36%)
    def __init__(self, v1: List[int], v2: List[int]):
        self.arr = []
        for i in range(min(len(v1), len(v2))):
            self.arr.append(v1[i])
            self.arr.append(v2[i])
        if len(v1)>len(v2):
            self.arr += v1[len(v2):]
        if len(v1)<len(v2):
            self.arr += v2[len(v1):]
        self.pos = 0

    def next(self) -> int:
        ele = self.arr[self.pos]
        self.pos += 1
        return ele

    def hasNext(self) -> bool:
        return self.pos<len(self.arr)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())