class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        # We have to sort at first!
        intervals.sort()
        heap = [intervals[0][1]]
        res = 1
        for start, end in intervals[1:]:
            first_end = heappop(heap)
            if start>=first_end:
                heappush(heap, end)
            else:
                res += 1
                heappush(heap, first_end)
                heappush(heap, end)
        return res