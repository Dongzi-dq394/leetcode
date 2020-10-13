class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Solution by myself: BFS (84ms: 99.95%)
        vertice = defaultdict(list)
        for s, e in edges:
            vertice[s].append(e)
            vertice[e].append(s)
        res = 0
        visited = {}
        def bfs(node):
            queue = deque([node])
            while queue:
                node = queue.popleft()
                for v in vertice[node]:
                    if v not in visited:
                        queue.append(v)
                        visited[v] = True
        for i in range(n):
            if i not in visited:
                visited[i] = True
                bfs(i)
                res += 1
        return res