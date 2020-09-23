class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Solution 1 by myself: Sort + Heap (56ms: 97.85%)
        trips.sort(key=lambda x: x[1])
        h = []
        remain = capacity
        for people, start, end in trips:
            if not h:
                if people>remain:
                    return False
                remain -= people
                heappush(h, [end, people])
            else:
                while h and h[0][0]<=start:
                    end_temp, people_temp = heappop(h)
                    remain += people_temp
                if people>remain:
                    return False
                remain -= people
                heappush(h, [end, people])
        return True
        
        # Solution 2 from Solution: (60ms: 89.81%)
        time = []
        for people, start, end in trips:
            time.append([start, people])
            time.append([end, -people])
        time.sort()
        cur_people = 0
        for _, people in time:
            cur_people += people
            if cur_people > capacity:
                return False
        return True