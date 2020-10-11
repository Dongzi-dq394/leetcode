class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # Solution from Discussion: Sort + Queue (1032ms: 60.49%)
        # This method is smart than my first solution (TLE), because
        # each worker is separated here and we only need to sort for
        # each of them. Becasue, once a worker is assigned a bike, then
        # we don't need to worry about him any more.
        res = [0 for _ in range(len(workers))]
        dis = []
        used_bike = {}
        for i, (wi, wj) in enumerate(workers):
            dis.append([])
            for j, (bi, bj) in enumerate(bikes):
                temp = abs(wi-bi)+abs(wj-bj)
                dis[-1].append([temp, i, j])
            dis[-1].sort(reverse=True)
        h = []
        for i in range(len(workers)):
            heappush(h, dis[i].pop())
        while h:
            _, wind, bind = heappop(h)
            if bind not in used_bike:
                res[wind] = bind
                used_bike[bind] = True
            else:
                heappush(h, dis[wind].pop())
        return res