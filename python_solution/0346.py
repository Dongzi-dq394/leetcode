class MovingAverage:
    
    # Solution by myself: Queue (52ms: 99.64%)

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.SUM = 0
        self.arr = []
        self.size = size

    def next(self, val: int) -> float:
        if len(self.arr)<self.size:
            self.SUM += val
            self.arr.append(val)
            return self.SUM/len(self.arr)
        else:
            self.SUM -= self.arr.pop(0)
            self.SUM += val
            self.arr.append(val)
            return self.SUM/len(self.arr)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)