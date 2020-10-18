class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # Solution from Hint: BFS * 2 (184ms: 76.27%)
        if not edges: return 0
        dic = defaultdict(list)
        for s, e in edges:
            dic[s].append(e)
            dic[e].append(s)
        visited = {edges[0][0]:True}
        queue = deque([edges[0][0]])
        start = None
        while queue:
            length = len(queue)
            start = queue[0]
            for i in range(length):
                node = queue.popleft()
                for j in dic[node]:
                    if j not in visited:
                        visited[j] = True
                        queue.append(j)
        queue = deque([(start, 0)])
        temp = {start:True}
        res = 0
        while queue:
            length = len(queue)
            for i in range(length):
                node, dis = queue.popleft()
                res = max(res, dis)
                for j in dic[node]:
                    if j not in temp:
                        temp[j] = True
                        queue.append((j, dis+1))
        return res