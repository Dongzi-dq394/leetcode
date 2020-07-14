class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)
        if length < 2: return intervals
        intervals.sort(key=lambda x: x[0])
        res = []
        short, long = intervals[0][0], intervals[0][1]
        for i in range(1, length):
            if long >= intervals[i][0]:
                long = max(long, intervals[i][1])
            else:
                res.append([short, long])
                short, long = intervals[i][0], intervals[i][1]
        res.append([short, long])
        return res