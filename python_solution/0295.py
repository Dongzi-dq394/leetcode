class MedianFinder:
    
    # Solution 1: Binary Search (244ms: 59.98%)
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ele = []
        

    def addNum(self, num: int) -> None:
        index = bisect.bisect_left(self.ele, num)
        self.ele.insert(index, num)

    def findMedian(self) -> float:
        length = len(self.ele)
        if length%2==1:
            return self.ele[length//2]
        else:
            return (self.ele[length//2-1]+self.ele[length//2]) / 2
    
    # Solution 2: Two Heaps from discussion (216ms: 73.81%)
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)
        temp = -heappop(self.max_heap)
        heappush(self.min_heap, temp)
        if len(self.min_heap) > len(self.max_heap):
            temp = heappop(self.min_heap)
            heappush(self.max_heap, -temp)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()