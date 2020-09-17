class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.ele = []
        self.pre_stamp = None

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.pre_stamp==None:
            self.pre_stamp = timestamp
            self.dic[timestamp] = 0
            self.ele.append(1)
        else:
            if self.pre_stamp==timestamp:
                self.ele[-1] += 1
            else:
                self.dic[timestamp] = len(self.ele)
                self.pre_time = timestamp
                self.ele.append(1+self.ele[-1])

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        start = max(timestamp-300, 0)
        all_time = list(self.dic.keys())
        #print(start, all_time)
        #print(self.dic)
        #print(self.ele)
        if timestamp in self.dic:
            right = self.ele[self.dic[timestamp]]
        else:
            index = bisect.bisect_left(all_time, timestamp)
            #print(index)
            right = 0 if index==0 else self.ele[self.dic[all_time[index-1]]]
        if start in self.dic:
            left = self.ele[self.dic[start]]
        else:
            index = bisect.bisect_left(all_time, start)
            if index==0 or start==0:
                left = 0
            else:
                left = self.ele[self.dic[all_time[index-1]]]
        return right-left
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)