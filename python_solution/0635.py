class LogSystem:
    
    # Solution 1: Hash Table (44ms: 96.51%)

    def __init__(self):
        self.record = {}

    def put(self, id: int, timestamp: str) -> None:
        self.record[timestamp] = id

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        mapping = {'Year':4, 'Month':7, 'Day':10, 'Hour':13, 'Minute':16, 'Second':19}
        length = mapping[granularity]
        left, right = start[:length], end[:length]
        res = []
        for key in self.record:
            if left<=key[:length]<=right:
                res.append(self.record[key])
        return res


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)