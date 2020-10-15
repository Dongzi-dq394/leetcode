class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        # Solution 1: Topological Sort (244ms: 100.00%)
        indeg = [0 for _ in range(N)]
        edges = defaultdict(list)
        for s, e in relations:
            edges[s].append(e)
            indeg[e-1] += 1
        res = 0
        course = 0
        queue = deque([])
        for i in range(N):
            if indeg[i]==0:
                queue.append(i+1)
        while queue:
            length = len(queue)
            res += 1
            course += length
            for i in range(length):
                node = queue.popleft()
                for v in edges[node]:
                    indeg[v-1] -= 1
                    if indeg[v-1]==0:
                        queue.append(v)
        return res if course==N else -1